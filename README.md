# Minikube/K8s: Deploy and test unprivileged alpine-nginx container
## Tasks:
1. Create Dockerfile that packages:
 * An index.html file that outputs current date and time using JavaScript.
 * Nginx web server that serves that file and nginx execution is the default process for the resulting Docker image.
 * The container has to run as unprivilege user.
2. Prepare deployment code to deploy the image to K8s.
 * In K8s network the service should listen on port 80
3. Create a test script that verifies that container works as expected:
 * the web page is served correctly
 * what is getting returned is a date
 * the returned date is correct

## Prerequisites
1. Docker engine
* follow the installation instructions depending on your OS [docker docs](https://docs.docker.com/engine/install/)
2. Minikube
 * install minikube
  * follow the installation instructions on [Install Minikube](https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/)
3. Kubectl
 * verify kubectl is installed: **kubectl version --short**
 * if kubectl is not automaticaly configured, install kubectl depending on your OS [how to install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
4. Python 3.6
 * if not installed, install python3.6 or later version
 * install Python modules: **pip install requests datetime**

-----------------------------------------------------------
## How to use this project:
* clone this project
* run minikube: **minikube start driver=docker**
* create and run container on k8s:
  * run k8s deployment: **kubectl apply -f deployment.yaml**
  * run k8s service: **kubectl apply -f service.yaml**
  * run in terminal: **kubectl get pods / && kubectl get svc**
* open minikube dashboard to check the pod: 
  * run in new terminal: **minikube dashboard**
* test js application runnig:
  * run in terminal:**python3 test_container/main.py** 

