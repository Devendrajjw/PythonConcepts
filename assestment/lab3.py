# a.	Input :25,49,121,169,
# output for this series: 225
# b.	Input 30, 5, 26, 9, 22, 13, 18,
# Output for this series: 17

#  5 ** 2
# 5 + 2
# 7 ** 2
# 7 + 4
# 11 ** 2
#---
# 11 + 2
# 13 ** 2
# 13 + 2
# 15 ** 2

#4.	Write a program to decode the pattern from the given series and then apply to new set of input series
# and give the output and if the pattern is not matched then error message should be printed.

def series(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            diff = arr[j+1] - arr[j]


if __name__ == "__main__":
    inp = [25,49,121,169]
    series(inp)
