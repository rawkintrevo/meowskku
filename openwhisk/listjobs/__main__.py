# from base64 import standard_b64decode
# from pymongo import MongoClient

def listjobs(params):
    URI = params.uri
    CA_CERT_BASE_64 = params.ca_certificate_base64
    # f = open("./ca.pem", 'wb')
    # f.write( standard_b64decode(CA_CERT_BASE_64))
    # f.close()
    # mc = MongoClient(URI, ssl_ca_certs="./ca.pem")
    # message = {"message" : "Available jobs: %s" % ",".join(mc['meowskku'].collection_names()) }
    # mc.close()
    message = {"foo": "bar"}
    return message