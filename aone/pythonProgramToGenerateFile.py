import os

dir_files = './logs'
os.makedirs(dir_files, exist_ok=True)
file_content = '''
Test Results:
PASS
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
FAIL
PASS
'''

def create_file(file_path, content):
    with open(file_path, 'w') as fh:
        fh.write(content)

for i in range(1, 101):
    file_name = f'file{i}.log'
    file_path = os.path.join(dir_files, file_name)
    create_file(file_path, file_content)
    print(f'{file_name} created')
print("100 files are created")
