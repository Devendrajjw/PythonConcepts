import json

states = ['jharkhand', 'bihar', 'delhi', 'andhra pradesh', 'tamil naidu', 'kolkata', 'punjab']
en_states = dict(enumerate(states, 1))
print(en_states)
fh = open('file001', 'w+')
json.dump(en_states, fh)
fh.close()

fh = open('file001', 'r+')
print(fh.read())
fh.close()
