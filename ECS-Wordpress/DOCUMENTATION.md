### Project Overview
This project sets up and deploys a containerized application using Amazon Elastic Container Service (ECS). It automates deployment, scaling, and management of containerized applications within AWS infrastructure.

## Features
- Containerized application deployment with ECS
- Automatic scaling of services
- Secure networking and IAM role management
- Integration with Amazon Elastic Container Registry (ECR) for image storage
- Logging and monitoring with Amazon CloudWatch

## Technologies Used
- **AWS Services**: ECS, ECR, CloudWatch, IAM
- **Programming & Tools**: Docker, AWS CLI, Bash
- **Infrastructure as Code**: JSON (Task Definitions), Shell Scripting

## Architecture
The project follows a microservices architecture using AWS ECS with the following components:
- **ECS Cluster**: Manages containers and services
- **Task Definition**: Defines container configurations
- **ECR Repository**: Stores Docker images
- **Load Balancer (optional)**: Distributes traffic
- **CloudWatch**: Logs and monitors container performance

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/vanshPadia/project.git
cd project/ecs
```

### 2. Configure AWS CLI
```bash
aws configure
```

### 3. Build and Push Docker Image
```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <ecr-repo>
docker build -t my-app .
docker tag my-app:latest <ecr-repo>:latest
docker push <ecr-repo>:latest
```

### 4. Create ECS Cluster
```bash
aws ecs create-cluster --cluster-name my-cluster
```

### 5. Register Task Definition
```bash
aws ecs register-task-definition --cli-input-json file://task-definition.json
```

### 6. Deploy Service
```bash
aws ecs create-service --cluster my-cluster --service-name my-service --task-definition my-task:1 --desired-count 1 --launch-type FARGATE
```

## Usage
- Monitor running tasks:
  ```bash
  aws ecs list-tasks --cluster my-cluster
  ```
- View service status:
  ```bash
  aws ecs describe-services --cluster my-cluster --services my-service
  ```
- Access logs via CloudWatch.

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License
This project is licensed under the MIT License.

