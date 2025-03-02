# 🛠️ AWS OpenSearch Project Setup Guide

This document provides comprehensive setup instructions for deploying the AWS OpenSearch project with Tomcat EC2 instance for log analysis.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Detailed Setup Instructions](#detailed-setup-instructions)
  - [Environment Setup](#environment-setup)
  - [VPC Prerequisites](#vpc-prerequisites)
  - [OpenSearch Deployment](#opensearch-deployment)
  - [EC2 Tomcat Deployment](#ec2-tomcat-deployment)
  - [Filebeat Configuration](#filebeat-configuration)
- [Configuration Details](#configuration-details)
- [Production Deployment](#production-deployment)
- [Troubleshooting](#troubleshooting)

## 📋 Prerequisites
Before starting the deployment, make sure you have:

- AWS account with proper permissions
- AWS CLI installed and configured
- Jenkins server with the following plugins:
  - AWS CloudFormation
  - Credentials Binding
  - Pipeline
- SSH key pair created in AWS EC2
- Existing VPC infrastructure
- Basic knowledge of AWS services and CloudFormation

## 🚀 Detailed Setup Instructions

### 🌐 Environment Setup

1. **Configure AWS credentials in Jenkins**
   ```bash
   # Add AWS credentials to Jenkins credentials store
   # ID should be 'AWS' as referenced in Jenkinsfile
   ```

2. **Set up Jenkins folder properties**
   Create a Jenkins folder with the following properties:
   - `environment`: dev, staging, or prod
   - `domainName`: name for your OpenSearch domain
   - `keyName`: name of your EC2 key pair

### 🏗️ VPC Prerequisites

This project requires an existing VPC with the following exported outputs:
- `vpc`: VPC ID
- `PrivateSubnet1`: ID of a private subnet
- `PublicSubnet1`: ID of a public subnet

If you don't have these resources, deploy the VPC stack from the RDS-Jumphost project first.

### 🔍 OpenSearch Deployment

1. **Review OpenSearch configuration**
   Examine `iac/aws/cloudformation/opensearch.yml` to ensure it meets your requirements.

2. **Deploy the OpenSearch domain**
   ```bash
   # Run the Jenkins pipeline
   jenkins-cli run pipeline/Jenkinsfile
   ```

3. **Verify deployment**
   - Check that the OpenSearch domain is active in the AWS console
   - Note the domain endpoint for later configuration

### 🖥️ EC2 Tomcat Deployment

The EC2 instance hosts Tomcat and Filebeat for log generation and shipping:

1. **Review EC2 configuration**
   Check `iac/aws/cloudformation/ec2.yml` for:
   - Security group settings
   - Instance type mapping
   - User data script that installs and configures Tomcat and Filebeat

2. **Deploy the EC2 instance**
   ```bash
   # Included in the same pipeline as OpenSearch
   # The EC2 will be deployed after OpenSearch
   ```

3. **Verify deployment**
   - Confirm the EC2 instance is running
   - Test SSH access using your key pair
   - Verify Tomcat is running:
     ```bash
     curl http://localhost:8080
     ```

### 📊 Filebeat Configuration

Filebeat is configured automatically through the EC2 user data script, but you may need to update the OpenSearch endpoint:

1. **SSH to the EC2 instance**
   ```bash
   ssh -i your-key.pem ubuntu@ec2-instance-ip
   ```

2. **Update Filebeat configuration if needed**
   ```bash
   sudo nano /etc/filebeat/filebeat.yml
   ```

3. **Replace OpenSearch endpoint**
   Update the `hosts` field with your actual OpenSearch domain endpoint:
   ```yaml
   output.elasticsearch:
     hosts: ["your-opensearch-domain-endpoint:443"]
   ```

4. **Restart Filebeat**
   ```bash
   sudo systemctl restart filebeat
   ```

## ⚙️ Configuration Details

### OpenSearch Configuration
- **Instance Type**: Varies by environment (see mappings in CloudFormation)
- **Engine Version**: Elasticsearch 7.10
- **Storage**: 10GB GP3 EBS volume
- **Network**: Deployed in a private subnet with security group
- **Access Policy**: Allows access from within the VPC

### EC2 Tomcat Configuration
- **Instance Type**: t2.micro (configurable per environment)
- **AMI**: Ubuntu LTS (ami-00bb6a80f01f03502)
- **Software**: Java 11, Tomcat 10.1.35, Filebeat 7.10.2
- **Network**: Deployed in a public subnet
- **Security Group**: Allows SSH, HTTP, HTTPS, and Tomcat ports

### Filebeat Configuration
- **Input**: Monitors Tomcat log files in `/opt/tomcat/logs/*.out`
- **Output**: Ships logs to OpenSearch domain
- **Index Pattern**: filebeat01-%{+yyyy.MM.dd}
- **Pipeline**: Includes host metadata, cloud metadata

## 🚀 Production Deployment

For production environments, consider these additional steps:

1. **Increase OpenSearch capacity**
   Modify `opensearch.yml` to use:
   ```yaml
   InstanceCount: 3  # For better reliability
   InstanceType: r5.large.search  # Or another appropriate instance type
   ```

2. **Enable domain encryption**
   Add to the OpenSearch configuration:
   ```yaml
   EncryptionAtRestOptions:
     Enabled: true
   NodeToNodeEncryptionOptions:
     Enabled: true
   ```

3. **Implement tighter security**
   - Use a more restrictive access policy
   - Configure fine-grained access control
   - Implement Cognito authentication for the dashboard

4. **Configure a larger EBS volume**
   Increase the volume size based on your log volume:
   ```yaml
   EBSOptions:
     VolumeSize: 100  # Or appropriate size for your needs
   ```

5. **Set up alerts and monitoring**
   - Configure CloudWatch alarms for OpenSearch metrics
   - Set up log-based alerts in OpenSearch

## 🔧 Troubleshooting

### Common Issues

**Problem**: OpenSearch domain creation fails
**Solution**:
- Check that your service-linked role exists for OpenSearch
- Verify subnet and security group configurations
- Ensure you're not exceeding service limits

**Problem**: Tomcat not starting on EC2
**Solution**:
- Check the system logs:
  ```bash
  sudo journalctl -u tomcat
  ```
- Verify Java is installed correctly:
  ```bash
  java -version
  ```
- Check file permissions on Tomcat directories

**Problem**: Filebeat not shipping logs
**Solution**:
- Check Filebeat status:
  ```bash
  sudo systemctl status filebeat
  ```
- Verify configuration file is valid:
  ```bash
  sudo filebeat test config -c /etc/filebeat/filebeat.yml
  ```
- Check connectivity to OpenSearch:
  ```bash
  curl -k https://your-opensearch-endpoint:443
  ```

**Problem**: Can't access OpenSearch dashboard
**Solution**:
- Verify security group allows connections from your EC2 instance
- Check that your network route allows access to the OpenSearch domain
- Verify HTTPS is working properly

For additional help, please create an issue in the project repository or contact your system administrator.
