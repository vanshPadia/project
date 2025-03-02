# 🚀 Jenkins AWS Deployment

## ✨ Overview
This project provides CloudFormation templates to automatically deploy Jenkins on AWS infrastructure. It creates a complete environment including VPC, subnet, security group, and an EC2 instance with Jenkins pre-installed and configured.

## 🔥 Features
- 🤖 Fully automated Jenkins deployment on AWS
- 🌐 Complete networking setup with VPC, subnet, and internet gateway 
- 🔒 Security group configuration for Jenkins access
- ⚙️ Parameterized templates for customization (Dev/Prod environments)
- 💻 EC2 instance with Jenkins installation and auto-start configuration

## 🏃‍♂️ Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/jenkins-aws-deployment.git

# Navigate to the project directory
cd jenkins-aws-deployment

# Deploy the VPC stack first
aws cloudformation create-stack \
  --stack-name jenkins-vpc \
  --template-body file://Jenkins-setup/vpc-templet.yaml \
  --parameters ParameterKey=environment,ParameterValue=Dev

# Wait for the VPC stack to complete
aws cloudformation wait stack-create-complete --stack-name jenkins-vpc

# Deploy the Jenkins EC2 stack
aws cloudformation create-stack \
  --stack-name jenkins-ec2 \
  --template-body file://Jenkins-setup/Jenkins-ec2.yaml \
  --parameters \
    ParameterKey=environment,ParameterValue=Dev \
    ParameterKey=keyName,ParameterValue=YOUR_EC2_KEY_PAIR \
    ParameterKey=instanceType,ParameterValue=t2.micro
```

## 📋 Requirements
- 💼 AWS CLI installed and configured
- 🔑 Valid EC2 Key Pair for SSH access
- ☁️ AWS account with permissions to create VPC, EC2, SecurityGroups, etc.

## 🏗️ Architecture
The deployment consists of two CloudFormation stacks:
1. **VPC Stack**: Creates the network infrastructure
2. **Jenkins EC2 Stack**: Deploys the EC2 instance with Jenkins

## 🔍 Accessing Jenkins
Once deployment is complete, you can access Jenkins at:
```
http://<EC2-Public-IP>:8080
```

Get your EC2 public IP from the CloudFormation stack outputs:
```bash
aws cloudformation describe-stacks --stack-name jenkins-ec2 --query "Stacks[0].Outputs[?OutputKey=='publicIP'].OutputValue" --output text
```

## ⚙️ Parameters
Both templates support customization through parameters:

### VPC Template Parameters
| Parameter | Description | Default | Options |
|-----------|-------------|---------|---------|
| environment | Environment designation | Dev | Dev, Prod |

### Jenkins EC2 Template Parameters
| Parameter | Description | Default | Options |
|-----------|-------------|---------|---------|
| instanceType | EC2 instance size | t2.micro | t2.micro, t2.small, t2.medium |
| keyName | EC2 Key Pair for SSH access | - | Your existing EC2 key pairs |
| environment | Environment designation | Dev | Dev, Prod |
| amiId | Amazon Machine Image ID | ami-0dee22c13ea7a9a67 | Any Ubuntu AMI ID |

## 🤝 Contributing
Contributions to improve the templates are welcome! Please feel free to submit a pull request.

## 📜 License
[Specify your license here]
