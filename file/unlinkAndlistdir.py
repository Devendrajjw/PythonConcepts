import os

def check_details():
    print(os.listdir())
    print(len(os.listdir()))


def remove_file(filename):
    try:
        os.unlink(filename)
    except FileNotFoundError as e:
        print(e)
        print(" RERUN TO RETRY")
    else:
        print("file removed successfully")
    finally:
        print("Successfully in finally ")


check_details()
remove_file('file003')
check_details()
