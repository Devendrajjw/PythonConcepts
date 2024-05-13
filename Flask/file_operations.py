import re
class CustomFile:

    def read_content(self):
        with open('file2.txt') as fh:
            return fh.read()

    def post_content(self, line):
        with open('file2.txt', 'a') as fh:
            return fh.write(line)

    def put_content(self):
        with open('file2.txt', 'r+') as fh:
            search_input = input('enter word to replace ')
            fh.seek(0)
            data = fh.read()
            if search_input in data:
                new_input = input('enter new updated string ')
                data = data.replace(search_input, new_input)
                fh.seek(0)
                fh.write(data)
            else:
                print('given string not found')
    def delete_content(self):
        with open('file2.txt', 'r+') as fh:
            search_input = input('enter word to delete ')
            fh.seek(0)
            data = fh.readlines()
            print(data)
            # # data = fh.read()
            # if search_input in data:
            #     print(f'deleting the {search_input} ')
            #     data = data.remove()
            #     fh.seek(0)
            #     fh.write(data)
            # else:
            #     print('given string not found')


obj1 = CustomFile()
# print(obj1.read_content())
obj1.delete_content()
# print(obj1.read_content())
