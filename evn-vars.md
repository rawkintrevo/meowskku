

```bash
export MY_KUBE_NAMESPACE=meowskku
export KUBE_NAMESPACE=default
export MY_ORG=trevor.grant@ibm.com 
export MY_SPACE=open-source-evangelism
export VERSION_TAG=v_0.1.2
export OBJECTSTORE_SERVICE_NAME=rawkintrevo-object-storage
export MONGODB_SERVICE_NAME=rawkintrevo-mongo-compose 
export KUBE_CLUSTER_NAME=mycluster
```


```bash
bx cs cluster-config mycluster
```

Copy and paste the last line of out put, e.g. 

```bash
export KUBECONFIG=/home/rawkintrevo/.bluemix/plugins/container-service/clusters/mycluster/kube-config-hou02-mycluster.yml
```



### Notes

Note: to find spaces/orgs available
```bash
bx account orgs
bx account spaces
```

(you'll need to `bx target -o $MY_ORG` before you can `bx account spaces`)