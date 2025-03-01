---
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

