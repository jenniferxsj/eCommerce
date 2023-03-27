# ECommerce Website
Authod: Shujun Xiao (Jennifer)

## Project Objective
The objective of this project is to create a basic eCommerce application using Django, Python, and MySQL. Additionally, the project aims to establish the Infrastructure-as-a-Service (IaaS) environment for a three-tier application. This involves configuring the Virtual Private Cloud (VPC), network connections, and security groups for various subnets to ensure a secure network environment. It also includes setting up subnets in different availability zones, Elastic Load Balancer (ELB), and Auto Scaling Group (ASG) to ensure the application's availability and scalability. Finally, the eCommerce app is successfully deployed on the cloud.

## Models in the Project
![image](https://drive.google.com/uc?export=view&id=1UjCkau8irmsLIKWO3_OCrqw0ERjn4UL0)

## Steps to Deploy the app
1. Follow the instruction from the article to set up the IaaS environment in AWS. 
   [Link to the article](https://medium.com/the-andela-way/designing-a-three-tier-architecture-in-aws-e5c24671f124)
2. Create an EC2 instance in AWS and connect to it use SSH. 
3. Create virtual environment for the project.
4. Install all the necessary packages including Django and poll the project code from github.
5. Install and set up Gunicorn and Nginx. Nginx is a reverse proxy which can accept incoming connections. If it’s static file, Nginx serves it, otherwise, it redirects the request to the Gunicorn which is an application server to run python application.
6. Install and set up Supervisor to allow make sure the app can up and run in the background.
7. Create a MySQL database in AWS RDS and connect it with the above EC2 instance.
8. Create AMIs with the above EC2 instance and set up autoscaling group.
