
# MeOwSkKu

- **M**ongoDB
- **E**xperimental
- **O**pen
- **W**hisk
- **Sk**-learn
- **Ku**bernetes




## Recipe

1. Find [Docker Image with SkLearn](https://hub.docker.com/r/buildo/docker-python2.7-scikit-learn/~/dockerfile/)

Steps 2-3 [Source](https://console.bluemix.net/containers-kubernetes/home/registryGettingStarted?env_id=ibm%3Ayp%3Aus-south)
2. Pull Docker Image: `sudo docker pull buildo/docker-python2.7-scikit-learn`
3. Tag the image: 
	`docker tag hello-world registry.ng.bluemix.net/<KUBE_NAMESPACE>/hello-private-registry:my_first_tag`
                   
`