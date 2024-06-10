import subprocess
import re

cmd = subprocess.Popen('ipconfig', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = cmd.communicate()
print("="*10)
print(stdout)
pattern = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'
match_ip = re.finditer(pattern, stdout)
print("="*10)
for mp in match_ip:
    print(mp.group())
# re.finditer()
# re.sub()
# re.split()
# re.findall()
# re.match()
# re.search()

