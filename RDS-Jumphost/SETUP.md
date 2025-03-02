# 🛠️ RDS-Jumphost Setup Guide

This document provides comprehensive setup instructions for the RDS-Jumphost project.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Detailed Setup Instructions](#detailed-setup-instructions)
  - [Environment Setup](#environment-setup)
  - [VPC Deployment](#vpc-deployment)
  - [Jump Host Deployment](#jump-host-deployment)
  - [RDS Deployment](#rds-deployment)
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
- Basic knowledge of AWS services and CloudFormation

## 🚀 Detailed Setup Instructions

### 🌐 Environment Setup

1. **Configure AWS credentials in Jenkins**
   ```bash
   # Add AWS credentials to Jenkins credentials store
   # ID should be 'AWS' as referenced in Jenkinsfiles
   ```

2. **Set up Jenkins folder properties**
   Create a Jenkins folder with the following properties:
   - `environment`: dev, staging, or prod
   - `keyName`: Name of your EC2 key pair
   - `engine`: mysql
   - `engineVersion`: 8.0.40
   - `dbUsername`: admin (default)

### 🏗️ VPC Deployment

The VPC must be deployed first as other resources depend on it:

1. **Review VPC configuration**
   Examine `iac/aws/cloudformation/vpc/vpc.yml` to ensure it meets your requirements.

2. **Deploy the VPC stack**
   ```bash
   # Run the VPC pipeline
   jenkins-cli run pipeline/vpc/Jenkinsfile
   ```

3. **Verify deployment**
   Confirm the following resources were created:
   - VPC with CIDR 10.0.0.0/16
   - Internet Gateway
   - 2 Public Subnets
   - 2 Private Subnets
   - Route Tables
   - Appropriate route associations

### 🖥️ Jump Host Deployment

The jump host provides secure access to your RDS instance:

1. **Review jump host configuration**
   Check `iac/aws/cloudformation/ec2/jumphost.yml` for:
   - Security group settings
   - Instance type mapping
   - User data script

2. **Deploy the jump host**
   ```bash
   # Run the Jumphost pipeline
   jenkins-cli run pipeline/jumphost/Jenkinsfile
   ```

3. **Verify deployment**
   - Confirm the jump host is running
   - Test SSH access using your key pair
   - Verify MySQL client is installed

### 🗄️ RDS Deployment

Deploy the RDS instance after the jump host:

1. **Review RDS configuration**
   Check `iac/aws/cloudformation/rds/rds.yml` for:
   - Database instance settings
   - Parameter group configuration
   - Security settings

2. **Deploy the RDS instance**
   ```bash
   # Included in the same pipeline as jump host
   # The RDS will be deployed after the jump host
   ```

3. **Verify deployment**
   - Check that the RDS instance is available
   - Retrieve the credentials from Secrets Manager
   - Test connection from the jump host:
     ```bash
     mysql -h <rds-endpoint> -u admin -p
     ```

## ⚙️ Configuration Details

### Security Group Configuration
- **Jump Host Security Group**: Allows SSH (port 22) from VPC CIDR and MySQL (port 3306) access to internal resources
- **RDS Security Group**: Allows MySQL (port 3306) access only from the jump host security group

### RDS Configuration
- **Instance Class**: Varies by environment (see mappings in CloudFormation)
- **Storage**: GP3 storage with size based on environment
- **Engine**: MySQL 8.0.40 (configurable)
- **Parameter Group**: Custom with optimized settings
- **Backups**: Disabled by default (enable for production)

### Database Access
Credentials are stored in AWS Secrets Manager with the name pattern:
```
<environment>-rds-secret
```

## 🚀 Production Deployment

For production environments, consider these additional steps:

1. **Enable RDS backups**
   Modify `rds.yml` to set:
   ```yaml
   BackupRetentionPeriod: 7  # Or your preferred retention period
   ```

2. **Add Multi-AZ support**
   Enable for production by adding to `rds.yml`:
   ```yaml
   MultiAZ: true
   ```

3. **Implement rotation for secrets**
   Configure AWS Secrets Manager to rotate credentials regularly.

4. **Enhance monitoring**
   Add CloudWatch enhanced monitoring and alarms.

5. **Network security**
   Restrict jump host access to specific corporate IP ranges.

## 🔧 Troubleshooting

### Common Issues

**Problem**: Cannot SSH to jump host
**Solution**:
- Verify security group allows SSH from your IP
- Check the key pair is correct
- Ensure the instance is running

**Problem**: Cannot connect to RDS from jump host
**Solution**:
- Check security group allows port 3306 from jump host
- Verify RDS instance is available
- Confirm you're using the correct endpoint and credentials

**Problem**: CloudFormation stack creation fails
**Solution**:
- Check CloudFormation logs for specific errors
- Verify IAM permissions
- Ensure resource names are not already in use

**Problem**: MySQL client not installed on jump host
**Solution**:
- SSH to jump host and run:
  ```bash
  sudo apt update && sudo apt install mysql-client -y
  ```

For additional help, please create an issue in the project repository or contact your system administrator.
