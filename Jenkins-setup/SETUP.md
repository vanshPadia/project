# 🛠️ Detailed Jenkins AWS Setup Guide

This document provides comprehensive instructions for deploying Jenkins on AWS using the CloudFormation templates in this repository.

## 📑 Table of Contents
- [Prerequisites](#prerequisites)
- [Template Details](#template-details)
- [Step-by-Step Deployment Guide](#step-by-step-deployment-guide)
- [Post-Deployment Configuration](#post-deployment-configuration)
- [Troubleshooting](#troubleshooting)
- [Customization Options](#customization-options)

## 🔒 Prerequisites

Before deploying the CloudFormation templates, ensure you have:

- **☁️ AWS Account**: Active AWS account with sufficient permissions
- **⚙️ AWS CLI**: Installed and configured with appropriate credentials
  ```bash
  aws configure
  ```
- **🔑 EC2 Key Pair**: Created in the AWS region where you'll deploy
- **👮 IAM Permissions**: Permissions to create/modify:
  - VPC and related networking components
  - EC2 instances
  - Security groups
  - CloudFormation stacks

## 📝 Template Details

### 🌐 VPC Template (`vpc-templet.yaml`)
Creates a complete networking environment:
- VPC with CIDR block 10.0.0.0/16
- Public subnet with CIDR 10.0.1.0/24
- Internet Gateway with proper attachments
- Route table with default route to Internet

### 💻 Jenkins EC2 Template (`Jenkins-ec2.yaml`)
Deploys an EC2 instance with Jenkins:
- Ubuntu-based EC2 instance
- Security group allowing Jenkins access (port 8080)
- UserData script that:
  - Installs Java 17
  - Installs Jenkins
  - Configures Jenkins to start automatically

## 🚶 Step-by-Step Deployment Guide

### 1️⃣ Deploy the VPC Stack

```bash
aws cloudformation create-stack \
  --stack-name jenkins-vpc \
  --template-body file://Jenkins-setup/vpc-templet.yaml \
  --parameters ParameterKey=environment,ParameterValue=Dev
```

Monitor the stack creation:
```bash
aws cloudformation describe-stacks --stack-name jenkins-vpc --query "Stacks[0].StackStatus"
```

### 2️⃣ Deploy the Jenkins EC2 Stack

After the VPC stack shows `CREATE_COMPLETE`, deploy the Jenkins EC2 stack:

```bash
aws cloudformation create-stack \
  --stack-name jenkins-ec2 \
  --template-body file://Jenkins-setup/Jenkins-ec2.yaml \
  --parameters \
    ParameterKey=environment,ParameterValue=Dev \
    ParameterKey=keyName,ParameterValue=YOUR_EC2_KEY_PAIR \
    ParameterKey=instanceType,ParameterValue=t2.micro \
    ParameterKey=amiId,ParameterValue=ami-0dee22c13ea7a9a67
```

Monitor the stack creation:
```bash
aws cloudformation describe-stacks --stack-name jenkins-ec2 --query "Stacks[0].StackStatus"
```

### 3️⃣ Get Jenkins Instance Details

Once complete, retrieve the public IP of your Jenkins instance:

```bash
aws cloudformation describe-stacks \
  --stack-name jenkins-ec2 \
  --query "Stacks[0].Outputs[?OutputKey=='publicIP'].OutputValue" \
  --output text
```

## ⚙️ Post-Deployment Configuration

### 🚀 Initial Jenkins Setup

1. **🌐 Access Jenkins Web Interface**
   Open your browser and navigate to:
   ```
   http://<EC2-Public-IP>:8080
   ```

2. **🔑 Retrieve the Initial Admin Password**
   SSH into your EC2 instance:
   ```bash
   ssh -i /path/to/your-key.pem ubuntu@<EC2-Public-IP>
   ```
   
   Then retrieve the initial password:
   ```bash
   sudo cat /var/lib/jenkins/secrets/initialAdminPassword
   ```

3. **✅ Complete the Jenkins Setup Wizard**
   - Install suggested plugins
   - Create an admin user
   - Configure Jenkins URL

### 💻 SSH Access to Jenkins Instance

Use the EC2 key pair you specified during stack creation:
```bash
ssh -i /path/to/your-key.pem ubuntu@<EC2-Public-IP>
```

## 🔧 Troubleshooting

### ❗ Common Issues and Solutions

1. **❌ Stack Creation Fails**
   - Check the CloudFormation events for error details:
     ```bash
     aws cloudformation describe-stack-events --stack-name jenkins-ec2
     ```
   - Validate your templates:
     ```bash
     aws cloudformation validate-template --template-body file://Jenkins-setup/vpc-templet.yaml
     aws cloudformation validate-template --template-body file://Jenkins-setup/Jenkins-ec2.yaml
     ```

2. **🚫 Can't Access Jenkins**
   - Verify the security group allows port 8080 traffic
   - Check if Jenkins service is running:
     ```bash
     ssh -i key.pem ubuntu@<EC2-IP>
     sudo systemctl status jenkins
     ```
   - Check Jenkins logs:
     ```bash
     sudo cat /var/log/jenkins/jenkins.log
     ```

3. **💥 Jenkins Installation Failed**
   - Review the EC2 instance system logs:
     ```bash
     sudo cat /var/log/cloud-init-output.log
     ```

## 🎨 Customization Options

### 🌍 Environment-Specific Deployments

For production environments:
```bash
aws cloudformation create-stack \
  --stack-name jenkins-vpc-prod \
  --template-body file://Jenkins-setup/vpc-templet.yaml \
  --parameters ParameterKey=environment,ParameterValue=Prod
```

### 💪 Instance Type Selection

For more powerful instances:
```bash
aws cloudformation create-stack \
  --stack-name jenkins-ec2 \
  --template-body file://Jenkins-setup/Jenkins-ec2.yaml \
  --parameters \
    ParameterKey=environment,ParameterValue=Dev \
    ParameterKey=keyName,ParameterValue=YOUR_EC2_KEY_PAIR \
    ParameterKey=instanceType,ParameterValue=t2.medium
```

### 🖼️ Custom AMI

If you need to use a specific AMI:
```bash
aws cloudformation create-stack \
  --stack-name jenkins-ec2 \
  --template-body file://Jenkins-setup/Jenkins-ec2.yaml \
  --parameters \
    ParameterKey=environment,ParameterValue=Dev \
    ParameterKey=keyName,ParameterValue=YOUR_EC2_KEY_PAIR \
    ParameterKey=amiId,ParameterValue=YOUR_CUSTOM_AMI
```

### 🔒 Additional Security Configuration

To modify the security group after creation:
```bash
aws ec2 authorize-security-group-ingress \
  --group-id <your-security-group-id> \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0
```
