import re

email_list = ['abc@mail.com', 'bbc_1@gmail.co.in', 'rcb.1@hotmail.com', 'karnataka@buses@com', 'babaji.com@kaka']
# email_list = 'abc@mail.com'
# nl = [email_list]
# print(nl)
# pattern = r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$'

pattern = re.compile(r'^[\w\-/.]+@([\w-]+\.)+[\w-]{2,}$', re.I)
for email in email_list:
    results = re.finditer(pattern, email)
    for results_obj in results:
        print(results_obj.group())
    # for results_obj in results:
    #     print(results_obj.group())

'''
For example, [\w-] is the same as [A-Za-z0-9_-]. They both match any of the characters in "no_reply@example-server.com" except for the "@" and the "."

{2,} Which basically would read: match n-times, 2 or more times
'''
