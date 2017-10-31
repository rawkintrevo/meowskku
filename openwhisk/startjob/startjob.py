
import requests
import itertools

def main(args):
    # name = args.get("name", "stranger")
    #
    targetIP = "184.172.234.215"
    targetPort = "31124"
    problemType = "classify"
    fileName = 'creditcard.csv'
    container = "BoWShowCase"
    yColName = "Class"
    xColNames = "V1,V2,V3"
    jobName = "test1" # generate this automatically

    if problemType == 'classify':
        clfs = [
            {'name': "RandomForrestClassifier",
             'nEstimators': [1, 10, 100, 500],
             'maxDepth'   : [2, 5, 10],
             'maxFeatures': ['sqrt', 'log2' ]
             }
            ]


    for clf in clfs:
        url = "http://%s:%s/train/%s" % (targetIP, targetPort, clf.pop('name'))
        payload = {"filename" : fileName,
                  "container": container,
                  "yColName" : yColName,
                  "xColNames": xColNames,
                  "jobName"  : jobName}

    for hyperparams in itertools.product(*[[{k: v} for v in clf[k]] for k in clf.keys()]):
        new_params = {k: v for d in [t for t in hyperparams] for k,v in d.items()}
        requests.get(url, params= payload.update(new_params))
    #
    return {"status": "success", "jobId" : jobName}
