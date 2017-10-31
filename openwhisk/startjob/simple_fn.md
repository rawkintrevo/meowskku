
To submit a simple fn:

```bash
bx wsk action create startjobtest1 startjob.py --web true
bx wsk api create /test /startjob get startjobtest1 --response-type json
```


to update simply:

```bash
bx wsk action update startjobtest1 startjob.py --web true
```

to test:

```bash
curl https://service.us.apiconnect.ibmcloud.com/gws/apigateway/api/15eec0b641f5a394352ad2f0394ae48ace9b8464167ff1b051e5f7e98b6a5599/test/startjob?
```
