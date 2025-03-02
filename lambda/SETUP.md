# 🛠️ Detailed Setup Guide

## 📑 Table of Contents
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [CloudFormation Deployment](#cloudformation-deployment)
- [Lambda Function Configuration](#lambda-function-configuration)
- [OpenSearch Integration](#opensearch-integration)
- [Production Deployment Considerations](#production-deployment-considerations)
- [Troubleshooting](#troubleshooting)

## 📋 Prerequisites

Before getting started, ensure you have:

- ☁️ AWS Account with administrative access
- 🔑 AWS CLI configured with appropriate credentials
- 🌐 VPC with at least two public subnets
- 🔍 Existing OpenSearch domain
- 🔄 Jenkins server with AWS plugin installed

## 🌍 Environment Setup

### AWS Resources Requirements

1. **VPC Configuration**
   - The Lambda function requires a VPC with public subnets
   - Make sure the VPC has proper internet access via an Internet Gateway
   - The CloudFormation template expects the following exports:
     - `vpc` - The VPC ID
     - `PublicSubnet1` and `PublicSubnet2` - Subnet IDs
     - `DomainEndpoint` - OpenSearch domain endpoint

### Development Environment

1. **Setup Python Environment**
   ```bash
   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install required packages
   pip install requests boto3
   ```

2. **AWS Credentials Configuration**
   ```bash
   aws configure
   ```

## ☁️ CloudFormation Deployment

### Parameters

The CloudFormation template (`lambda.yml`) accepts the following parameters:

| Parameter | Description | Default | Required |
|-----------|-------------|---------|----------|
| environment | Deployment environment (dev/prod/staging) | - | Yes |
| indexPattern | OpenSearch index pattern to target | filebeat02-* | No |
| timeUnit | Time unit for retention (days/hours/minutes) | minutes | No |
| timeValue | Time value for retention | 2 | No |

### Deployment Via Jenkins

1. **Configure Jenkins Pipeline**
   - Create a new pipeline job
   - Configure the following parameters:
     - `environment`
     - `indexPattern`
     - `timeUnit`
     - `timeValue`

2. **Run Pipeline**
   - The pipeline will use the AWS CloudFormation plugin to deploy the stack

### Manual Deployment

```bash
aws cloudformation deploy \
  --template-file iac/aws/cloudformation/lambda.yml \
  --stack-name your-environment-lambda \
  --parameter-overrides \
    environment=dev \
    indexPattern=filebeat02-* \
    timeUnit=days \
    timeValue=7 \
  --capabilities CAPABILITY_IAM
```

## ⚙️ Lambda Function Configuration

### Environment Variables

The Lambda function requires the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| OPENSEARCH_ENDPOINT | OpenSearch domain endpoint | (Required) |
| INDEX_PATTERN | Pattern to match indices | filebeat01-* |
| TIME_UNIT | Unit for time calculation (days, hours, minutes) | minutes |
| TIME_VALUE | Amount of time to retain logs | 2 |

### Lambda Code Structure

- `lambda_function.py` - Main entry point with the `lambda_handler` function
  - Uses delete-by-query to remove documents older than the specified time
- `lambda.py` - Alternative implementation that deletes entire indices based on date

## 🔗 OpenSearch Integration

### Connection Setup

The Lambda function connects to OpenSearch using the endpoint URL provided in the environment variable. 

### Index Management

There are two strategies implemented:

1. **Delete documents older than a specific time** (`lambda_function.py`)
   - Uses OpenSearch delete-by-query API
   - Keeps the indices but removes old documents
   - More granular but potentially slower for large indices

2. **Delete entire indices older than today** (`lambda.py`)
   - Deletes complete indices based on date pattern in the index name
   - Faster but less granular
   - Requires indices to follow a date-based naming convention

## 🚀 Production Deployment Considerations

### Scaling

- The Lambda function is configured with 128MB memory by default
- For larger OpenSearch clusters or more complex queries, consider increasing:
  - Memory allocation (affects CPU allocation)
  - Timeout (default: 300 seconds)

### Monitoring

1. **Set up CloudWatch Alarms**
   ```bash
   aws cloudwatch put-metric-alarm \
     --alarm-name LambdaErrors \
     --metric-name Errors \
     --namespace AWS/Lambda \
     --statistic Sum \
     --period 300 \
     --threshold 1 \
     --comparison-operator GreaterThanOrEqualToThreshold \
     --dimensions Name=FunctionName,Value=your-environment-lambda \
     --evaluation-periods 1 \
     --alarm-actions <your-sns-topic-arn>
   ```

2. **Log Analysis**
   - Review CloudWatch logs for the Lambda function
   - Look for patterns in deleted document counts or errors

### Security Hardening

1. **IAM Permissions**
   - Review and tighten Lambda IAM role permissions
   - Restrict access to specific OpenSearch domain ARNs

2. **Network Security**
   - Restrict security group rules to necessary ports and IP ranges
   - Consider using private subnets with NAT Gateway instead of public subnets

## 🔍 Troubleshooting

### Common Issues

#### Lambda Function Timeout
- **Symptom**: Function execution exceeds the configured timeout
- **Solution**: Increase the Lambda timeout in the CloudFormation template
  ```yaml
  Timeout: 600  # Increase from default 300
  ```

#### OpenSearch Connection Issues
- **Symptom**: Lambda cannot connect to OpenSearch
- **Solutions**:
  - Verify the OPENSEARCH_ENDPOINT environment variable is correct
  - Check security group rules allow Lambda to access OpenSearch
  - Ensure the VPC configuration is correct

#### Permission Denied
- **Symptom**: Lambda function fails with permission errors
- **Solution**: 
  - Review the Lambda execution role
  - Ensure it has appropriate permissions for OpenSearch operations

#### No Documents/Indices Deleted
- **Symptom**: Lambda runs successfully but doesn't delete anything
- **Solutions**:
  - Verify the index pattern matches existing indices
  - Check if time parameters are correct
  - Ensure there are documents older than the specified time threshold

### Debugging

Enable detailed debugging by adding the following to the Lambda function:

```python
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
```

### Support Resources

- AWS Lambda Documentation: https://docs.aws.amazon.com/lambda/
- OpenSearch Documentation: https://opensearch.org/docs/
- AWS CloudFormation Documentation: https://docs.aws.amazon.com/cloudformation/
