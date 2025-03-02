# 🔍 AWS OpenSearch Project

## 📋 Overview
This project provides infrastructure as code (IaC) for deploying an AWS OpenSearch cluster with a Tomcat EC2 instance for log generation and visualization. The solution uses AWS CloudFormation templates and Jenkins for automated deployment.

## ✨ Features
- 🔍 Fully managed OpenSearch domain deployment
- 🖥️ Tomcat EC2 instance with automated setup
- 📊 Filebeat integration for log shipping
- 🔒 Security group configuration
- 🌐 Multi-environment support (dev, staging, prod)
- 🚦 VPC integration with private subnets

## 🏆 Benefits
- **Centralized Logging** - All application logs in one searchable place
- **Real-time Monitoring** - Instant visibility into application behavior
- **Automated Deployment** - Entire stack provisioned with minimal effort
- **Scalable Architecture** - Easily scales as log volume increases
- **Operational Insights** - Advanced search and analytics capabilities

## 🎯 Use Cases
- **Application Monitoring** - Track application performance and errors
- **Security Analysis** - Identify suspicious patterns in logs
- **Compliance Auditing** - Maintain records for regulatory requirements
- **DevOps Observability** - Complete visibility into infrastructure behavior
- **Troubleshooting** - Quickly identify and resolve issues

## 🔍 Comparison with Other Methods
| Method | Search Capability | Setup Complexity | Management Overhead | Cost | Scalability |
|--------|-------------------|------------------|---------------------|------|-------------|
| **AWS OpenSearch (This Project)** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| ELK Self-Managed | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| CloudWatch Logs | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Third-party Solutions | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |

## 🚀 Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/aws-opensearch.git
   cd aws-opensearch
   ```

2. **Set up Jenkins pipeline with required parameters:**
   - `environment`: dev, staging, or prod
   - `domainName`: name for your OpenSearch domain
   - `keyName`: EC2 key pair name for SSH access

3. **Deploy the infrastructure:**
   ```bash
   # Make sure VPC is already deployed first
   # Then run the OpenSearch pipeline
   jenkins-cli run pipeline/Jenkinsfile
   ```

4. **Access OpenSearch Dashboard:**
   ```bash
   # SSH to the EC2 instance first
   ssh -i your-key.pem ubuntu@ec2-instance-ip
   
   # Then access the dashboard via browser at:
   # https://opensearch-domain-endpoint/_dashboards/
   ```

## 🔒 Security Best Practices
- ✅ **Deploy in private subnets** to prevent public access
- ✅ **Implement fine-grained access control** for OpenSearch
- ✅ **Use HTTPS** for all communications
- ✅ **Enable node-to-node encryption** for data in transit
- ✅ **Encrypt data at rest** using AWS KMS
- ✅ **Restrict security group access** to necessary sources only
- ⚠️ **Regularly rotate credentials** for EC2 and OpenSearch access

## 📋 Requirements
- AWS Account with appropriate permissions
- Jenkins with AWS plugin
- AWS CLI
- SSH key pair for EC2 access
- Existing VPC infrastructure (see the vpc.yml template)

## 🛠️ Installation
See [SETUP.md](SETUP.md) for detailed installation instructions.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
