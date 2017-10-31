

```bash
bx login -a api.ng.bluemix.net --sso
```

```bash
sudo bx cr login
bx cs cluster-config mycluster
```

copy last line
```bash
export KUBECONFIG=/home/rawkintrevo/.bluemix/plugins/container-service/clusters/mycluster/kube-config-hou02-mycluster.yml
```
kubectl proxy
```