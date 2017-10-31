


### Build new container

1. Bump version tag

```bash
echo $VERSION_TAG
```

```bash
export VERSION_TAG=v_0.1.19
```

```bash 
cd docker
sudo docker build -t registry.ng.bluemix.net/$MY_KUBE_NAMESPACE/sklearn-flask:$VERSION_TAG .
sudo docker push registry.ng.bluemix.net/$MY_KUBE_NAMESPACE/sklearn-flask:$VERSION_TAG
```

to delete

`sudo bx cr image-rm registry.ng.bluemix.net/meowskku/sklearn-flask:v_0.1.13`

### Update

```bash
kubectl edit deployment/sklearn-deployment
```

OR

```bash
kubectl set image deployment/sklearn-deployment sklearn-deployment=registry.ng.bluemix.net/$MY_KUBE_NAMESPACE/sklearn-flask:$VERSION_TAG
```

Edit line with Image
(it's vim, so make sure you know what you're doing. 
`x` to delete `a` to append new version number, or `r` to replace character at position)

Check update
```bash
kubectl rollout status deployment/sklearn-deployment
```

A handy tool:

```bash
kubectl exec -it sklearn-deployment-1009283929-qbfff  bash
```