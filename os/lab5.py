import os

def check_os():
    return os.name

def get_ip():
    pass

if __name__ == '__main__':
    if os.name.lower() == 'nt':
        print(f'os name is {os.name.lower()}')

