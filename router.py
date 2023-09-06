import paramiko

router_ip = "192.168.1.1"
router_username = "admin"
router_password = "password"

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(router_ip, username=router_username, password=router_password)

# Execute command to print system information
stdin, stdout, stderr = ssh.exec_command("system info")
print(stdout.read().decode())

# Close the SSH connection
ssh.close()

