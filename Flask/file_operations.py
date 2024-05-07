class CustomFile:

    def read_file(self):
        with open('file2.txt') as fh:
            return fh.read()

    def wirite_file(self, line):
        with open('file2.txt', 'a') as fh:
            return fh.write(line)
    #
    # def post_file(self, word):
    #     with open('file2.txt', )


obj1 = CustomFile()
print(obj1.read_file())
obj1.wirite_file("Devenda")
