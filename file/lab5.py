import os


# def file_append():
#     fa = open('file001', 'a+')
#     fa.write(input(" enter name "))
#     fa.close()
#
#
# def file_read():
#     fr = open('file001', 'r')
#     print(fr.read())
#     fr.close()


def file_detail():
    print(os.getcwd())
    print(os.listdir()[-1])

# def file_remove(fname):
#     os.unlink(fname)


# file_append()
# file_read()
# file_remove('file001')
file_detail()
