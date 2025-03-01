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

