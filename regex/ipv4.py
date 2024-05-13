import subprocess
# import os
import re

cmd = 'ipconfig'
# res = os.system(cmd)
res = subprocess.check_output(cmd)
res = res.decode("utf-8")
# print(type(res))
# print(res)
pattern = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'
# results = re.finditer(r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}', res)
results = re.finditer(r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}', res)
for results_obj in results:
    # print(results_obj)
    print(results_obj.group())

