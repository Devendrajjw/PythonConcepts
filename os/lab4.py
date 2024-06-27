import os
import subprocess

print(type(os.name))
print(os.getpid())
print(os.getcwd())

cmd = 'VOL'

response = os.system(cmd)
print("responseeeee", response)
print(type(response))


# response1 = subprocess.run(cmd)
# print("response11111", response1)
# print(type(response1))

response2 = subprocess.Popen(cmd, shell=True)
print("response22222", response2)
print(type(response2))

response3 = subprocess.call(cmd, shell=True)
print('response33333', response3)

response4 = subprocess.check_output(cmd)
print("response44444", response4.decode('utf-8'))





