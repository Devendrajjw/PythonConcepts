def reverseStr(data):
    new_str = data[::-1]
    if new_str == data:
        print('its palindrome')
    else:
        print('not a palindrome')


if __name__ == '__main__':
    reverseStr('hello')
