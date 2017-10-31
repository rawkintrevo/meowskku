

We want to connect an object store to our Cluster.
(And Mongo)

```bash
bx target -o $MY_ORG -s $MY_SPACE
bx service list
```

You'll see something like this

```bash
name                            service                      plan                             bound apps                               last operation
availability-monitoring-auto    AvailabilityMonitoring       Lite                             MongoPlay                                create succeeded
Compose for MongoDB-dp-tester   compose-for-mongodb          Standard                         rawkintrevo-zeppelin                     create succeeded
rawkintrevo-bi                  BigInsightsForApacheHadoop   Basic                                                                     create succeeded
rawkintrevo-mongo-compose       compose-for-mongodb          Standard                         MongoPlay                                update succeeded
rawkintrevo-object-storage      Object-Storage               Free                                                                      create succeeded
rawkintrevo-postgres            compose-for-postgresql       Standard                         rawkintrevo-zeppelin, rawkintrevo-nifi   create succeeded
rawkintrevo-saas                spark                        ibm.SparkService.PayGoPersonal   rawkintrevo-zeppelin                     update succeeded

```


```bash
export OBJECTSTORE_SERVICE_NAME=rawkintrevo-object-storage
export MONGODB_SERVICE_NAME=rawkintrevo-mongo-compose
bx cs cluster-service-bind $KUBE_CLUSTER_NAME $KUBE_NAMESPACE $OBJECTSTORE_SERVICE_NAME
bx cs cluster-service-bind $KUBE_CLUSTER_NAME $KUBE_NAMESPACE $MONGODB_SERVICE_NAME
```

Note the secret names- you'll need them in next section

Check for success
```bash
bx cs cluster-services mycluster
```

### Update Kube Config

https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod

Edit
```bash
kubectl edit deployment/sklearn-deployment
```

edit `spec:template:spec`

add towards the bottom (update with your secret name, you'll find in the webui)

        volumeMounts:
        - name: objstore-vcap
          mountPath: "/etc/objstore-vcap"
          readOnly: true
        - mountPath: /etc/mongo-vcap
          name: mongo-vcap
          readOnly: true

      volumes:
      - name: objstore-vcap
        secret: 
          secretName: binding-rawkintrevo-object-storage
      - name: mongo-vcap
        secret: 
          secretName: binding-rawkintrevo-mongo-compose



binding-rawkintrevo-mongo-compose