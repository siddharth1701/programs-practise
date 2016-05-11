__author__ = 'Narendra Avula'
'''
All submissions for this problem are available.

A positive integer is called a palindrome if its representation in the decimal system is the same when read from left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.
Input

The first line contains integer t, the number of test cases. Followed by t lines containing integers K.
Output

For each K, output the smallest palindrome larger than K.
Example

Input:
2
808
2133
Output:
818
2222
Warning: large Input/Output data, be careful with certain languages
'''

def reverse(num):
  temp = num
  rev = 0
  while(num > 0):
    rev = (10*rev)+num%10
    num //= 10
  return temp == rev

for _ in range(int(input())):
    number = int(input())
    sum = 0
    for i in range(number+1,100000000):
        if reverse(i):
            print(i)
            break
