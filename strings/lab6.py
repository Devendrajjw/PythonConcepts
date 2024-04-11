def first_last(first, last):
    if len(first) <= 10 and len(last) <= 10:
        return f'Hello {first} {last}! You just delved into python.'

if __name__ == '__main__':
    print(first_last('Rudraveer', 'D'))
