from base64 import standard_b64decode
from pymongo import MongoClient

def countclfsinjob(params):
    URI = params.vcap['uri']
    CA_CERT_BASE_64 = params.vcap['ca_certificate_base64']
    JOB_NAME = params.jobname
    f = open("./ca.pem", 'wb')
    f.write( standard_b64decode(CA_CERT_BASE_64))
    f.close()
    mc = MongoClient(URI, ssl_ca_certs="./ca.pem")
    return {"message" : "There are %i clfs in job %s" % (mc['meowskku'][JOB_NAME].count(), JOB_NAME) }

