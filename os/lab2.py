import subprocess

# Use 'dir' command with shell=True to ensure it's recognized
process = subprocess.Popen('ipconfig', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Capture the output and error
stdout, stderr = process.communicate()

# Print the output
print(stdout)

# Check if there were any errors
if process.returncode != 0:
    print(f"Error: {stderr}")
