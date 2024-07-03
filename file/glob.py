import os
import glob

cwd = os.getcwd()
# print(glob.glob(cwd + r'\*'))
files_lists = glob.glob(cwd + r'\*') # returns list of all available files
# print(files_lists)
latest_file = max(files_lists, key=os.path.getctime)
print(latest_file)
oldest_file = min(files_lists, key=os.path.getctime)
print(oldest_file)
