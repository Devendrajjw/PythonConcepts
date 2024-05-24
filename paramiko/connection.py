import paramiko

def ssh_connect(hostname, port, username, password, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode('utf-8')
        print(output)
        error = stderr.read().decode('utf-8')
        if error:
            print(error)
    except Exception as e:
        print(f'an error occurred: {e}')
    finally:
        ssh.close()


if __name__ == '__main__':
    hostname = "your.server.com"  # Replace with your server's hostname or IP address
    port = 22  # Default SSH port is 22
    username = "your_username"  # Replace with your SSH username
    password = "your_password"  # Replace with your SSH password
    command = "ls -l"  # Replace with the command you want to execute

    ssh_connect(hostname, port, username, password, command)



