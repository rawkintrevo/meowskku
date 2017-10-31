## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

from flask import Flask, request

import pandas as pd

import json
import swiftclient

app = Flask(__name__)

"""
# get port
$ kubectl describe service sklearn-service
...
Node Port:     31124
...

# get ip
$ bx cs workers $KUBE_CLUSTER_NAME
184.172.234.215:31124

"""

def loadVCAP(service_name):
    with open("/etc/%s/binding" % service_name, 'rb') as f:
        vcap = json.load(f)
    return vcap

def downloadFromObjectStoreToClasspath(credinfo, file_names, container_name):
    """
    A function to copy jars from an ObjectStore to the local classpath
    :param credinfo: a dict from the VCAP_SERVICES json of the corresponding ObjectStore
    :param jars_of_interest: a list of strings of the file names of the interesting jars
    :return: None
    """
    authurl = credinfo["auth_url"]  + '/v3'  #authorization URL
    project = credinfo['project']
    projectId = credinfo['projectId']
    region = credinfo['region']
    userId = credinfo['userId']
    username = credinfo['username']
    password = credinfo['password']
    domanId = credinfo['domainId']
    domanname = credinfo['domainName']
    # Create Swift Connection
    conn = swiftclient.Connection(key=password,authurl=authurl,auth_version='3', os_options={"project_id": projectId,"user_id": userId,"region_name": region})
    target_dir = "/tmp/"

    for fname in file_names:
        print "Copying %s to %s" % (fname, target_dir)
        with open(target_dir + fname, 'w') as my_copy:
            my_copy.write(conn.get_object(container_name, fname)[1])
    conn.close()


def createMongoConnection(vcap):
    from base64 import standard_b64decode
    from pymongo import MongoClient
    URI = vcap['uri']
    CA_CERT_BASE_64 = vcap['ca_certificate_base64']
    f = open("./ca.pem", 'wb')
    f.write( standard_b64decode(CA_CERT_BASE_64))
    f.close()
    mc = MongoClient(URI, ssl_ca_certs="./ca.pem")
    return mc

@app.route('/check_object_store_conn')
def check_object_store_conn():
    vcap = loadVCAP("objstore-vcap")
    downloadFromObjectStoreToClasspath(vcap, ["creditcard.csv"] , "BoWShowCase")
    return "great success"


@app.route('/train/RandomForrestClassifier')
def trainRFC():
    """

    Example: http://184.172.234.215:31124/train/RandomForrestClassifier?fileName=creditcard.csv&container=BoWShowCase&yColName=Class&xColNames=V1,V2,V3&jobName=test1
    :return:
    """
    ## Todo: A smarter thing to do would be to move this to another script and kick it off as its own thread
    ## Todo: lots of logging- you're flying blind here

    from sklearn.ensemble import RandomForestClassifier

    ## Should check to see if file exists first
    objstore_vcap = loadVCAP("objstore-vcap")
    mongo_vcap = loadVCAP("mongo-vcap")

    mc = createMongoConnection(mongo_vcap)
    db = mc["meowskku"]
    col = db[request.args.get("jobName", )]

    file_name = request.args.get("fileName", )
    container = request.args.get("container", )
    ## need a try-catch here
    downloadFromObjectStoreToClasspath(objstore_vcap, [file_name] , container)

    ## try-catch here
    data = pd.DataFrame.from_csv("/tmp/%s" % file_name)

    ## try-catch here
    yColName = request.args.get("yColName", )
    y = data[yColName]

    ## try-catch here
    """ A comma seperated string of names"""
    xColNames = request.args.get("xColNames", ).split(",")
    X = data[xColNames]


    ## Init model based on API calls
    maxDepth = request.args.get("maxDepth", 2)
    maxFeatures = request.args.get("maxFeatures", "auto")
    nEstimators = request.args.get("nEstimators", 10)
    # ... fill all of these out.

    clf = RandomForestClassifier(max_depth= maxDepth,
                                 n_estimators= nEstimators,
                                 max_features= maxFeatures,
                                 random_state=0)

    ## Prob ought to have some try-catch or logging around this guy too
    clf.fit(X, y)

    ## Todo load doc on fn call, update status as it progresses through until finished.
    ## Pickle CLF and save it to MongoDB
    from bson.binary import Binary
    import pickle
    doc = {
        "clfName"   : "RandomForrestClassifier",
        "clf"       : Binary(pickle.dumps(clf))
    }
    col.insert(doc)
    return str(clf.estimators_)

if __name__ == "__main__":
    print "I live!"
    app.run(host="0.0.0.0")