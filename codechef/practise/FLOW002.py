__author__ = 'CustomFurnish'
'''
All submissions for this problem are available.

Write a program to find the remainder when two given numbers are divided.
Input

The first line contains an integer T, total number of test cases. Then follow T lines, each line contains two Integers A and B.
Output

Find remainder when A is divided by B.
Constraints

1 ? T ? 1000
1 ? A,B ? 10000
Example

Input
3
1 2
100 200
10 40

Output
1
100
10
'''

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a%b)