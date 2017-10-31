
# Getting Started


### Install pre-requisites (one time)
- prerequisite: install [bluemix cli](https://clis.ng.bluemix.net/ui/home.html)
- OR: 
```$bash
wget http://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-cli/Bluemix_CLI_0.6.1_amd64.tar.gz
tar -zxf Bluemix_CLI_0.6.1_amd64.tar.gz
cd Bluemix_CLI
./install_bluemix_cli
``` 

- Follow [this tutorial](https://console.bluemix.net/docs/containers/cs_tutorials.html#cs_cluster_tutorial)
1. Quick version, pt1:
```$bash
bx plugin install container-service -r Bluemix
wget https://storage.googleapis.com/kubernetes-release/release/v1.7.4/bin/linux/amd64/kubectl
sudo mv mv ./kubectl /usr/local/bin/kubectl
bx plugin install container-registry -r Bluemix
```
2. Quick version, pt2:
```$bash
bx login -a api.ng.bluemix.net --sso
```
`--sso` Needed for IBM federated login- normy's should drop this part

Come up with a unique name for your namespace
```$xslt
export MY_KUBE_NAMESPACE=meowskku
```

```$xslt
bx cr namespace-add $MY_KUBE_NAMESPACE
bx cs workers mycluster
```

```$xslt
bx cs cluster-config mycluster
```

Copy /Paste output of last line

3. Build the Docker container.

**Important** Missing in the tutorial one must login to something or other with
`bx cr login` (perhaps a sudo in front of that if you need sudo to start dockers on your machine).
You'll know you need to do this if the following commands produce an error: `unauthorized: authentication required
`


```$xslt
cd docker
export VERSION_TAG=v_0.1.2
sudo docker build -t registry.ng.bluemix.net/$MY_KUBE_NAMESPACE/sklearn-flask:$VERSION_TAG .
sudo docker push registry.ng.bluemix.net/$MY_KUBE_NAMESPACE/sklearn-flask:$VERSION_TAG
```

4. Deploy 

```$xslt
kubectl run sklearn-deployment --image=registry.ng.bluemix.net/$MY_KUBE_NAMESPACE/sklearn-flask:$VERSION_TAG
```

```$xslt
kubectl expose deployment/sklearn-deployment --type=NodePort --port=5000 --name=sklearn-service --target-port=5000
```

```$xslt
kubectl describe service sklearn-service
```
Note the node port ^^, mine is 32183

Get public address of worker
```$xslt
export KUBE_CLUSTER_NAME=mycluster
bx cs workers $KUBE_CLUSTER_NAME
```

Surf to http://[PUBLIC_IP]:[NODE_PORT]/train


4a. Kubenetes UI

```$xslt
kubectl proxy
```

Then go to [http://localhost:8001/ui](http://localhost:8001/ui)
