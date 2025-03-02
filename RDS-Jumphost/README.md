# 🚀 RDS-Jumphost Project

## 📋 Overview
This project provides infrastructure as code (IaC) for deploying a secure RDS database with a jump host in AWS. It creates a fully configured VPC with public and private subnets, a jump host for secure access, and an RDS MySQL instance, all using AWS CloudFormation templates and Jenkins pipelines.

## ✨ Features
- 🔒 Secure VPC setup with public and private subnets
- 🖥️ Configured jump host for secure database access
- 🗄️ Automated MySQL RDS deployment
- 🚦 Security groups for controlled access
- 🔄 CI/CD pipeline integration with Jenkins
- 🌐 Multi-environment support (dev, staging, prod)

## 🏆 Benefits
- **Enhanced Security** - Isolated database access through a jump host
- **Infrastructure as Code** - Complete AWS setup defined in version-controlled templates
- **Operational Efficiency** - Significant reduction in manual configuration tasks
- **Consistent Environments** - Identical configurations across dev, staging, and production
- **Disaster Recovery Ready** - Easily redeploy entire infrastructure after failures

## 🎯 Use Cases
- **Secure Database Development** - Perfect for teams that need secure access to databases
- **Compliance Requirements** - Ideal for applications that must meet regulatory requirements for data access
- **Multi-Team Projects** - Great for projects where database access needs to be controlled and audited
- **DevOps Implementation** - Example of well-structured cloud infrastructure automation

## 🔍 Comparison with Other Methods
| Method | Security | Automation | Complexity | Cost |
|--------|----------|------------|------------|------|
| **RDS-Jumphost (This Project)** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Direct RDS Access | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| VPN Solution | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Third-party Tools | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |

## 🚀 Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/RDS-Jumphost.git
   cd RDS-Jumphost
   ```

2. **Set up Jenkins pipeline with required parameters:**
   - `environment`: dev, staging, or prod
   - `keyName`: EC2 key pair name for SSH access
   - `engine`: mysql
   - `engineVersion`: 8.0.40 (or your preferred version)

3. **Deploy the infrastructure:**
   ```bash
   # First deploy the VPC
   jenkins-cli run pipeline/vpc/Jenkinsfile
   
   # Then deploy the jumphost and RDS
   jenkins-cli run pipeline/jumphost/Jenkinsfile
   ```

4. **Access your database:**
   ```bash
   # SSH to the jump host
   ssh -i your-key.pem ec2-user@jump-host-ip
   
   # Connect to the database from the jump host
   mysql -h rds-endpoint -u admin -p
   ```

## 🔒 Security Best Practices
- ✅ **Never expose RDS directly** to the internet
- ✅ **Rotate credentials** regularly using AWS Secrets Manager
- ✅ **Restrict jump host access** to specific IP addresses
- ✅ **Use key-based authentication** for SSH access
- ✅ **Enable enhanced monitoring** for RDS instances
- ✅ **Regularly patch** both jump host and RDS instances
- ⚠️ **Avoid hardcoding credentials** in templates or scripts

## 📋 Requirements
- AWS Account with appropriate permissions
- Jenkins with AWS plugin
- AWS CLI
- SSH key pair for EC2 access

## 🛠️ Installation
See [SETUP.md](SETUP.md) for detailed installation instructions.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
