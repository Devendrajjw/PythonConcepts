import re
import os

dir_name = './logs'

def collect_data(file_path):
    pass_c = 0
    fail_c = 0
    with open(file_path, 'r') as fh:
        for line in fh:
            if re.search(r'\bPASS\b', line):
                pass_c += 1
            if re.search(r'\bFAIL\b', line):
                fail_c += 1
    return pass_c, fail_c

for i in range(1, 100):
    file_name = f'file{i}.log'
    file_path = os.path.join(dir_name, file_name)
    if os.path.exists(file_path):
        pass_c, fail_c = collect_data(file_path)
        print(f'{file_name} : PASS - {pass_c}; FAIL - {fail_c}')
    else:
        print(f'{file_name} does not exist')

