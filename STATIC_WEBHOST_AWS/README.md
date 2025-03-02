# 🌐 Static Webhost AWS Project

## 📋 Overview
This project provides infrastructure as code (IaC) for deploying a static website using AWS S3, CloudFront, and Route 53. It automates the entire setup process from DNS configuration to content delivery network deployment using AWS CloudFormation templates and Jenkins.

## ✨ Features
- 🌍 Custom domain with SSL/TLS via AWS Certificate Manager
- 🚀 CloudFront CDN for global content delivery
- 🗄️ S3 bucket for secure content storage
- 🔒 Origin Access Control for enhanced security
- 🔄 CI/CD pipeline for automated deployments
- 🌐 Multi-environment support (dev/prod)

## 🏆 Benefits
- **Global Performance** - Content delivered at high speed worldwide
- **Cost Efficiency** - Pay only for what you use with S3 and CloudFront
- **Scalability** - Handles traffic spikes without provisioning servers
- **High Availability** - Built on AWS global infrastructure
- **Security** - SSL/TLS encryption and limited access to origin

## 🎯 Use Cases
- **Company Websites** - Perfect for business websites with global audience
- **Landing Pages** - Ideal for marketing campaigns and product launches
- **Documentation Sites** - Great for technical documentation and user guides
- **Portfolio Websites** - Showcase your work with high performance
- **Event Websites** - Temporary sites that can handle traffic surges

## 🔍 Comparison with Other Methods
| Method | Global Performance | Setup Simplicity | Operational Cost | Scalability | Security |
|--------|-------------------|------------------|------------------|-------------|----------|
| **S3+CloudFront (This Project)** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Traditional Web Hosting | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Self-managed VPS | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Managed WordPress | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

## 🚀 Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/STATIC_WEBHOST_AWS.git
   cd STATIC_WEBHOST_AWS
   ```

2. **Set up Jenkins pipeline with required parameters:**
   - `environment`: dev or prod
   - `product`: your product name
   - `service`: your service name (e.g., static-webapp)
   - `domainName`: your registered domain name
   - `subdomain`: subdomain for your site (e.g., www)

3. **Deploy the infrastructure:**
   ```bash
   # Run the Jenkins pipeline
   jenkins-cli run Pipelines/static_webapp/Jenkinsfile
   ```

4. **Update website content:**
   ```bash
   # Modify index.html in the root directory
   # Then redeploy the content stage in Jenkins
   ```

5. **Visit your website:**
   ```
   https://subdomain.yourdomain.com
   ```

## 🔒 Security Best Practices
- ✅ **Block public access** to S3 buckets
- ✅ **Use Origin Access Control** instead of Origin Access Identity
- ✅ **Enable S3 versioning** to protect against accidental deletions
- ✅ **Implement SSL/TLS** with AWS Certificate Manager
- ✅ **Configure secure CloudFront settings** with HTTPS policies
- ✅ **Set up proper IAM roles** for deployment processes
- ⚠️ **Regularly audit CloudFront distributions** for security configurations

## 📋 Requirements
- AWS Account with appropriate permissions
- Registered domain name
- Jenkins with AWS plugin
- AWS CLI configured with appropriate credentials

## 🛠️ Installation
See [SETUP.md](SETUP.md) for detailed installation instructions.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
