# 🛠️ Static Webhost AWS Setup Guide

This document provides comprehensive setup instructions for deploying a static website using AWS S3, CloudFront, and Route 53.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Detailed Setup Instructions](#detailed-setup-instructions)
  - [Environment Setup](#environment-setup)
  - [Domain Configuration](#domain-configuration)
  - [S3 and CloudFront Deployment](#s3-and-cloudfront-deployment)
  - [Content Deployment](#content-deployment)
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
- Registered domain name (you can purchase one through Route 53 or another registrar)
- Basic knowledge of AWS services and CloudFormation

## 🚀 Detailed Setup Instructions

### 🌐 Environment Setup

1. **Configure AWS credentials in Jenkins**
   ```bash
   # Add AWS credentials to Jenkins credentials store
   # ID should be 'aws' as referenced in Jenkinsfile
   ```

2. **Set up Jenkins folder properties**
   Create a Jenkins folder with the following properties:
   - `environment`: dev or prod
   - `product`: your product name (e.g., impressico)
   - `service`: your service name (e.g., static-webapp)
   - `domainName`: your registered domain name
   - `subdomain`: subdomain for your site (e.g., www)

### 🌐 Domain Configuration

1. **Review DNS configuration**
   Examine `iac/aws/cloudformation/route_53/Route53-acm.yaml` to ensure it meets your requirements.

2. **Deploy the DNS and ACM stack**
   ```bash
   # Run the first stage of the Jenkins pipeline
   jenkins-cli run Pipelines/static_webapp/Jenkinsfile -s DeployDNSStack
   ```

3. **Verify ACM certificate**
   - Check that the certificate validation is complete
   - This may take some time as DNS validation occurs

### 🗄️ S3 and CloudFront Deployment

1. **Review CDN configuration**
   Check `iac/aws/cloudformation/s3/s3-cdn.yaml` for:
   - S3 bucket settings
   - CloudFront distribution configuration
   - Route 53 record settings

2. **Deploy the CDN stack**
   ```bash
   # Run the second stage of the Jenkins pipeline
   jenkins-cli run Pipelines/static_webapp/Jenkinsfile -s DeployCDNStack
   ```

3. **Verify deployment**
   - Confirm S3 bucket is created with proper policies
   - Check that CloudFront distribution is deployed (this may take 15-30 minutes)
   - Verify Route 53 records point to the CloudFront distribution

### 📄 Content Deployment

1. **Customize the website content**
   Edit the `index.html` file in the project root to match your requirements.

2. **Deploy the content**
   ```bash
   # Run the content deployment stage
   jenkins-cli run Pipelines/static_webapp/Jenkinsfile -s DeployContent
   ```

3. **Verify website accessibility**
   - Open your browser and navigate to:
     ```
     https://subdomain.yourdomain.com
     ```
   - Also check the apex domain:
     ```
     https://yourdomain.com
     ```

## ⚙️ Configuration Details

### DNS Configuration
- **Hosted Zone**: Created for your domain name
- **Certificate**: ACM certificate with wildcard support (*.yourdomain.com)
- **Validation**: DNS-based validation

### S3 Configuration
- **Bucket Policy**: Allows access only from CloudFront
- **Public Access**: Blocked at bucket level
- **Versioning**: Enabled for content versioning

### CloudFront Configuration
- **Origin**: S3 bucket using Origin Access Control
- **Behaviors**: Configured for static content delivery
- **SSL/TLS**: Custom certificate from ACM
- **Default Root**: index.html

### Route 53 Configuration
- **Subdomain Record**: CNAME pointing to CloudFront distribution
- **Apex Domain**: A record with alias to CloudFront distribution
