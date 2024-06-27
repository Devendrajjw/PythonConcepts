n = int(input())
array = list(map(int, input().split()))

def find_minimum_x(n, array):
    S = sum(array)
    x = (S + n) // n
    return x

result = find_minimum_x(n, array)

print(result)


'''
how to attempt or solve this given Python program in hacker rank console:

array A containing N integers. His task is to update all elements of array to some minimum value x, that is, A[i] = x; 1 N such that sum of this new array is strictly greater than the sum of the initial array. Note that x should be as minimum as possible such that sum of the new array is greater than the sum of the initial array. Input Format: First line of input consists of an integer N denoting the number of elements in the array A. Second line consists of N space separated integers denoting the array elements. Output Format: The only line of output consists of the value of x. Input Constraints: 1≤ N ≤ 105 1≤ A[i] ≤ 1000

Initial sum of array \(= 1+2+3+4+5=15\)
When we update all elements to 4, sum of array \(= 4+4+4+4+4 = 20\) which is greater than \(15\).
Note that if we had updated the array elements to 3, \ (sum= 15) which is not greater than \(15\). So, 4 is the minimum value to which array elements need to be updated.

and console only have this info
n = int(input())             # Reading input from STDIN
print('Hi, %s.' % n)         # Writing output to STDOUT

which it will run with its sample inputs
'''
