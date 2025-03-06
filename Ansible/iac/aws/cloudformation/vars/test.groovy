def call() {
    sh '''
        ansible-playbook -i inventory.ini fetch-ec2.yml --vault-password-file vault.pass
        cat inventory.ini  # Debugging: Ensure inventory is updated
        ansible-playbook -i inventory.ini playbook.yml --vault-password-file vault.pass
    '''
}
