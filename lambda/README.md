# 🚀 Lambda OpenSearch Log Management

## 📋 Overview

This project provides an automated solution for managing logs in AWS OpenSearch using Lambda functions. It enables efficient log rotation and cleanup based on configurable time parameters, helping maintain optimal OpenSearch performance while reducing storage costs.

## ✨ Features

- 🔄 Automated log rotation and cleanup
- ⏱️ Configurable retention periods (minutes, hours, or days)
- 🔍 Pattern-based index targeting
- ☁️ Seamless AWS integration (Lambda, OpenSearch, CloudFormation)
- 📅 Scheduled execution via EventBridge
- 🔒 Secure VPC deployment with proper IAM permissions

## 🌟 Benefits

- **Cost Optimization** - Automatically remove old logs to reduce storage costs
- **Performance Improvement** - Maintain optimal OpenSearch cluster performance
- **Operational Efficiency** - Eliminate manual log management tasks
- **Compliance Support** - Configure retention policies to meet compliance requirements

## 🎯 Use Cases

- **DevOps Teams** - Manage growing log volumes in development and production environments
- **Security Operations** - Maintain recent security logs while archiving older data
- **Application Monitoring** - Keep application logs organized and manageable
- **Cost-Conscious Deployments** - Optimize OpenSearch usage and costs

## 🔄 Comparison with Other Methods

| Feature | This Solution | Manual Cleanup | Third-Party Tools |
|---------|---------------|----------------|-------------------|
| Cost | Low (AWS Lambda costs only) | High (operational overhead) | Medium-High (licensing fees) |
| Setup Complexity | Medium (one-time) | N/A | Medium-High |
| Maintenance | Low | High | Medium |
| Customizability | High | High | Medium |
| AWS Integration | Native | Manual | Varies |

## 🛡️ Security Best Practices

- Uses dedicated IAM roles with least privilege
- Deploys within VPC for network isolation
- Configurable security groups for access control
- No storage of sensitive credentials in code

## 🚦 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://your-repository-url.git
   cd lambda-opensearch-log-management
   ```

2. **Configure your environment variables**
   - Edit the pipeline parameters in your Jenkins configuration
   - Required parameters: `environment`, `indexPattern`, `timeUnit`, `timeValue`

3. **Deploy using Jenkins pipeline**
   ```bash
   # Trigger Jenkins pipeline with appropriate parameters
   ```

## 📋 Requirements

- AWS Account with appropriate permissions
- OpenSearch domain
- VPC with at least 2 public subnets
- Jenkins with AWS plugin configured

## 🔧 Installation

### Using CloudFormation (via Jenkins)

The project includes a Jenkins pipeline for deployment:

1. Configure the pipeline parameters in Jenkins
2. Run the pipeline to deploy the CloudFormation stack
3. Verify the Lambda function deployment in AWS Console

### Manual Deployment

1. Package the Lambda function code
2. Deploy the CloudFormation template using AWS CLI or Console
3. Configure the environment variables

For detailed installation instructions, see [SETUP.md](SETUP.md).

## 🧩 Usage

The Lambda function will run automatically based on the configured schedule (default: 6:30 AM UTC daily).

You can also invoke the function manually from the AWS Console or CLI:

```bash
aws lambda invoke --function-name your-environment-lambda output.json
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
