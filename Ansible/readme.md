# README.md

## Ansible Project Overview

This project is an Ansible-based infrastructure automation setup designed for deploying and managing Jenkins and cloud infrastructure. The repository includes Ansible playbooks, inventory configurations, and Jenkins pipeline automation.

## Project Structure

```
Ansible
├── iac
│   └── aws
│       └── cloudformation
├── jenkins-ansible
│   ├── ansible.cfg
│   ├── group_vars
│   │   └── all.yml
│   ├── inventory.ini
│   ├── playbook.yml
│   └── roles
│       ├── jenkins-master
│       └── jenkins-slave
└── pipeline
    └── Jenkinsfile
```

### Key Components

- **iac/aws/cloudformation**: Infrastructure-as-Code (IaC) setup for AWS using CloudFormation.
- **jenkins-ansible**: Contains Ansible configurations for deploying Jenkins.
  - `ansible.cfg`: Ansible configuration file.
  - `group_vars/all.yml`: Global variables for Ansible playbooks.
  - `inventory.ini`: Inventory file defining target hosts.
  - `playbook.yml`: Ansible playbook for provisioning Jenkins.
  - `roles/jenkins-master` & `roles/jenkins-slave`: Role definitions for master and slave nodes.
- **pipeline/Jenkinsfile**: CI/CD pipeline script for automating deployments.

## Usage Instructions

### 1. Set Up Ansible
Ensure you have Ansible installed:
```bash
sudo apt update
sudo apt install ansible -y
```

### 2. Configure Inventory
Modify `inventory.ini` with your target servers.

### 3. Run Playbook
Execute the Ansible playbook:
```bash
ansible-playbook -i inventory.ini playbook.yml
```

---

# DOCUMENTATION.md

## Jenkins Deployment using Ansible

### Purpose
This project automates the deployment of Jenkins using Ansible. It provisions both Jenkins Master and Slave nodes, ensuring a scalable and automated setup.

### Prerequisites
- Ansible installed on your control machine.
- SSH access to target servers.
- AWS infrastructure configured (if using CloudFormation).

### Deployment Steps

#### 1. Configure Inventory
Update `inventory.ini` with your target server details:
```ini
[jenkins-master]
master.example.com

[jenkins-slave]
slave1.example.com
slave2.example.com
```

#### 2. Define Variables
Modify `group_vars/all.yml` with necessary configurations:
```yaml
jenkins_version: "2.289.1"
jenkins_user: "admin"
```

#### 3. Run the Playbook
Execute the deployment playbook:
```bash
ansible-playbook -i inventory.ini playbook.yml
```

#### 4. Verify Installation
Access Jenkins UI via `http://<master-server>:8080` and complete the setup.

### CI/CD Pipeline
The `Jenkinsfile` in `pipeline/` automates the build and deployment process using Jenkins pipelines.

### Conclusion
This Ansible project simplifies Jenkins deployment, automating both infrastructure provisioning and software configuration.

