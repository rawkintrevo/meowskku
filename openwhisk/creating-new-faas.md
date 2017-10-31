

```bash
cd openwhisk
mkdir <new-faas>
cd <new-fass>
virtualenv virtualenv
```

http://jamesthom.as/blog/2017/04/27/python-packages-in-openwhisk/

```bash
source virtualenv/bin/activate
```

you're now in the virtualenv
```bash
pip install pymongo
```

create `__main__.py` in <new-faas> directory

edit

```bash
zip -r listjobs.zip virtualenv/bin/activate_this.py virtualenv/lib/python2.7/site-packages/pymongo __main__.py
```


Submit new action
```bash
bx wsk action create listjobs --kind python:2 --main listjobs listjobs.zip --web true
```

```bash
bx wsk api create /meowskku /listjobs get listjobs --response-type json
```

Write down the endpoint which is returned

**coming soon, able to pick these up within bluemix**

```bash
export MONGO_URI= 
export CA_CERT=
curl https://service.us.apiconnect.ibmcloud.com/gws/apigateway/api/15eec0b641f5a394352ad2f0394ae48ace9b8464167ff1b051e5f7e98b6a5599/meowskku/listjobs?uri=$MONGO_URI&ca_certificate_base64=$CA_CERT
```



Update existing app
```bash
zip -r listjobs.zip virtualenv/bin/activate_this.py virtualenv/lib/python2.7/site-packages/pymongo __main__.py
bx wsk action update listjobs --kind python:2 --main listjobs listjobs.zip --web true
```