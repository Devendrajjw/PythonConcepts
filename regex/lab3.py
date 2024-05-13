import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# ipv4_regex = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'
# email_regex = r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$'
#
# email_regex = r'^[\w\-\.]+@([\w-]+\.)+][\w-]{2,}$'
