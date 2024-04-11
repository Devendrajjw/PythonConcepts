import os
import glob
import re


class FileOperations:
    def __init__(self):
        # print(os.getcwd())
        self.file_lists = glob.glob(os.getcwd() + r'\*')
        self.oldest_file = min(self.file_lists, key=os.path.getctime)
        print("oldest path -->>", self.oldest_file)
        print("oldest name -->>", os.path.basename(self.oldest_file))
        print(self.latest_file_fun())
        self.rem_file_fun()

    def file_append_fun(self):
        user_file = input(" enter file name ")
        with open(user_file, 'a+') as fh:
            fh.write(input(" enter name ") + "\n")

    def latest_file_fun(self):
        self.latest_file = max(self.file_lists, key=os.path.getctime)
        print("latest file -->>", self.latest_file)
        print("latest file -->>", os.path.basename(self.latest_file))
        self.latest_file_name = os.path.basename(self.latest_file)
        return self.latest_file_name

    def rem_file_fun(self):
        # os.unlink(self.latest_file_name)
        l_f_n = self.latest_file_fun()
        pattern = r'^file\w*'
        match_res = re.match(pattern, l_f_n)
        # print(match_res.group())
        try:
            if l_f_n == match_res.group():
                print('hello file is  deleted ', l_f_n)
                os.unlink(self.latest_file_name)
        except FileNotFoundError as f:
            print(f)

    def read_file_fun(self):
        with open(self.latest_file_fun(), 'r') as fr:
            print(fr.read())


fo = FileOperations()


