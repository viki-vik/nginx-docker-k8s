# Deploy docker alpine container with nginx to k8s
## Tasks:
1. Create Dockerfile that packages:
 * An index.html file that outputs current date and time using JavaScript.
 * Nginx web server that serves that file and nginx execution is the default process for the resulting Docker image.
 * The init process of the resulting container has to run as non-root user.
2. Prepare deployment code to deploy the image to K8s.
 * In K8s network the service should listen on port 80
3. Create a test script that verifies that container works as expected:
 * the web page is served correctly
 * what is getting returned is a date
 * the returned date is correct

## Prerequisites
1. Docker engine
* follow the installation instructions depending on OS [docker docs](https://docs.docker.com/engine/install/)
3. Minikube
* use for testing [playground to learn Kubernetes](https://labs.play-with-k8s.com/)
* OR install minikube
  * follow the installation instructions on [Install Minikube](https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/)
  * kubectl will be automaticaly configured
  * minikube addons enable ingress
4. Python 3.6
* install python3.6 or later version, depending on OS
* install Python modules: **pip install requests datetime**

-----------------------------------------------------------
## How to use this project:
* clone this project
* run minikube: **minikube start driver=docker**
* create and run container on k8s:
  * run k8s deployment: **kubectl apply -f deployment.yaml**
  * run k8s service: **kubectl apply -f service.yaml**
  * run k8s service: **kubectl apply -f ingress.yaml**
* open minikube dashboard to check the pod: 
  * open new terminal and run this command: **minikube dashboard**
  * run in terminal: **kubectl get pods / && kubectl get svc**
* test js application runnig:
  * with python script:**run test_container/main.py**
  * OR with the following bash commands: 
  * **ping -c3 172.17.0.2** (check yours using docker container inspect ContainerID | grep "IPAddress")
  * **curl** http://172.17.0.2:8080

-----------------------------------------------------------
### SPECIAL THANKS: 
Dockerfile for unprivileged user and shell scripts were taken from [here](https://github.com/nginxinc/docker-nginx-unprivileged/tree/main/stable/alpine)
