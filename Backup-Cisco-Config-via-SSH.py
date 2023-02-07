# Note: The python module Paramiko is required to run the following script.
# Use “pip install paramiko” to install the required module if it is not already present on your system.

import paramiko

# Set the list of IP addresses of the Cisco devices
hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# Set the username and password to use for the SSH connection
user = "user"
password = "password"

# Loop over the list of hosts
for host in hosts:
    # Set the filename to use for the configuration backup
    filename = f"config_backup_{host}.txt"

    # Create an SSH client
    ssh = paramiko.SSHClient()

    # Automatically add host keys for unknown hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the Cisco device
    ssh.connect(host, username=user, password=password)

    # Execute the "show run" command to retrieve the configuration
    stdin, stdout, stderr = ssh.exec_command("show run")

    # Wait for the command to complete
    output = stdout.read().decode()

    # Close the SSH connection
    ssh.close()

    # Write the configuration to the specified file
    with open(filename, "w") as f:
        f.write(output)

    print(f"Configuration successfully backed up for host {host} to {filename}")

stdin.close()
