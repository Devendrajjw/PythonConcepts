def reverseStr(data):
    # return data[::-1]
    new_str = data[::-1]
    if new_str == data:
        print('its palindrome')
    else:
        print('not a palindrome')


if __name__ == '__main__':
    reverseStr('hello')
