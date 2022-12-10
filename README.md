# Flask Replace App
I created this repo in order to practice basic flask development and explore the possible ways to deploy the app on AWS.

## Tools used in this project

 - Python and Flask - Building the project
 - Insomnia - Api testing
 - Zappa - Deploying to AWS Lambda
 - Docker - Containerization

## The app

The application is very simple, we have two routes:

    /
The homepage of the app that was first created as a base for my flask journey

    /repalce
The **POST** path for the project. requests sent to this route must contain a string of plaintext, the app then returns the string adding copyright © to certain words.
Replaceable words: 

 - Google
 - Oracle
 - Amazon
 - Deloitte
 - Microsoft

## Deployment methods

The project is simple but that only means it has less restrictions when deploying, the possibilities are varied and depend on the desired scale.

### Lambda - or any serverless function service

Lambda was my choice for this project since it is the simplest, since the application does not require a database or any sort of side services (Redis, RabbitMQ, etc.. ) I chose to deploy to lambda since it is also the cheapest option.
Using the [Zappa](https://github.com/Zappa/Zappa#custom-aws-iam-roles-and-policies-for-deployment) Serverless python library the deployment was very simple and created all that was needed for the application to be deployed on AWS, including an API Gateway endpoint that can be found [here](https://sd2il6t1ba.execute-api.us-east-1.amazonaws.com/dev/replace).
Unfortunately Zappa still does not have support for lambda@edge which would have been the best choice for this deployment, but after trying and researching I realized that for lambda@edge to work, another build would be needed.

### Kubernetes

To deploy to kubernetes (My personal favorite although it requires much more overhead) You will need to create a kubernetes cluster and set up an [ingress controller](https://docs.nginx.com/nginx-ingress-controller/) on it then you can use my helm chart found [here](https://github.com/fmubaidien/flask-helm-chart)

The docker image has already been created and is available on DockerHub under [fasoolya/flask-replace-app](https://hub.docker.com/r/fasoolya/flask-replace-app)  The image has already been set in the values files so all you need is to cd into the directory and `helm upgrade --install release . --values values.yaml

I have also created IaC files using terraform for AWS EKS you can find them [here](https://github.com/fmubaidien/EKS-Terraform)

The IaC creates a vpc with 6 subnets, 3 public and 3 private and then creates an EKS cluster within the VPC.

### ECS

Since ECS makes it simple to deploy a containerized app it is also a very good option for deployment

### EC2 - Any VM
The application can also be deployed to any VM, the requirements.txt file includes any needed libraries (its just flask) and a simple system.d file can be added and then enabled allowing the application to run on a bare metal deployment. A load balancer can later be added, in addition to an autoscaling group that uses a custom made image to allow for scalability. 