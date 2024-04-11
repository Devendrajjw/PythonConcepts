# palindrome, racecar, mam, racingcar
data = input('enter word ')
flag = True
for i in range(len(data)//2):
    if data[i] != data[len(data) - i - 1]:
        flag = False
        print('not palindrome')
        break

if flag:
    print('palindrome')
