

## Project Title: AWS ECS Deployment

## Description
This project provides an automated way to deploy and manage containerized applications using Amazon ECS (Elastic Container Service). It enables users to build, push, and deploy Docker containers in a scalable and secure manner within AWS infrastructure.

## Installation
### Prerequisites:
- AWS CLI installed and configured (`aws configure`)
- Docker installed
- Amazon ECR repository created

### Steps to Set Up:
1. Clone the repository:
   ```bash
   git clone https://github.com/vanshPadia/project.git
   cd project/ecs
   ```
2. Build and push the Docker image:
   ```bash
   aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <ecr-repo>
   docker build -t my-app .
   docker tag my-app:latest <ecr-repo>:latest
   docker push <ecr-repo>:latest
   ```
3. Create an ECS cluster:
   ```bash
   aws ecs create-cluster --cluster-name my-cluster
   ```
4. Register a task definition:
   ```bash
   aws ecs register-task-definition --cli-input-json file://task-definition.json
   ```
5. Deploy the service:
   ```bash
   aws ecs create-service --cluster my-cluster --service-name my-service --task-definition my-task:1 --desired-count 1 --launch-type FARGATE
   ```

## Usage
- To check running tasks:
  ```bash
  aws ecs list-tasks --cluster my-cluster
  ```
- To get service status:
  ```bash
  aws ecs describe-services --cluster my-cluster --services my-service
  ```
- To view logs, use Amazon CloudWatch.

## Important Tips
- Ensure correct IAM roles and permissions are assigned.
- Use a private ECR repository to secure Docker images.
- Monitor CloudWatch logs for debugging issues.
- Auto-scaling can be configured based on CPU/memory usage.

## Contact Information
For any queries, reach out via GitHub issues or email at vansh@example.com.

