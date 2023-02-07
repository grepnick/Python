# Note: The python module Paramiko is required to run the following script.
# Use “pip install paramiko” to install the required module if it is not already present on your system.

import paramiko

# Set the IP address of the Cisco device
HOST = "192.168.1.1"

# Set the username and password to use for the SSH connection
user = "user"
password = "password"

# Set the filename to use for the configuration backup
filename = "config_backup.txt"

# Create an SSH client
ssh = paramiko.SSHClient()

# Automatically add host keys for unknown hosts
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the Cisco device
ssh.connect(HOST, username=user, password=password)

# Execute the "show run" command to retrieve the configuration
stdin, stdout, stderr = ssh.exec_command("show run")

# Wait for the command to complete
output = stdout.read().decode()

# Close the SSH connection
ssh.close()

# Write the configuration to the specified file
with open(filename, "w") as f:
	f.write(output)

print(f"Configuration successfully backed up to {filename}")
stdin.close()
