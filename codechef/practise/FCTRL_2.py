__author__ = 'CustomFurnish'
'''
The most important part of a GSM network is so called Base Transceiver Station (BTS). These transceivers form the areas called cells (this term gave the name to the cellular phone) and every phone connects to the BTS with the strongest signal (in a little simplified view). Of course, BTSes need some attention and technicians need to check their function periodically.
The technicians faced a very interesting problem recently. Given a set of BTSes to visit, they needed to find the shortest path to visit all of the given points and return back to the central company building. Programmers have spent several months studying this problem but with no results. They were unable to find the solution fast enough. After a long time, one of the programmers found this problem in a conference article. Unfortunately, he found that the problem is so called "Traveling Salesman Problem" and it is very hard to solve. If we have N BTSes to be visited, we can visit them in any order, giving us N! possibilities to examine. The function expressing that number is called factorial and can be computed as a product
1.2.3.4....N. The number is very high even for a relatively small N.
The programmers understood they had no chance to solve the problem. But because they have already received the research grant from the government, they needed to continue with their studies and produce at least some results. So they started to study behavior of the factorial function.
For example, they defined the function Z. For any positive integer N, Z(N) is the number of zeros at the end of the decimal form of number N!. They noticed that this function never decreases. If we have two numbers N1<N2, then Z(N1) <= Z(N2). It is because we can never "lose" any trailing zero by multiplying by any positive number. We can only get new and new zeros. The function Z is very interesting, so we need a computer program that can determine its value efficiently.
Input

There is a single positive integer T on the first line of input (equal to about 100000). It stands for the number of numbers to follow. Then there are T lines, each containing exactly one positive integer number N, 1 <= N <= 1000000000.
Output

For every number N, output a single line containing the single non-negative integer Z(N).
Example

Sample Input:
6
3
60
100
1024
23456
8735373
Sample Output:
0
14
24
253
5861
2183837

#that's the goal
print string.find_all('test') # [0,5,10,15]

>>> import re
>>> text = 'Allowed Hello Hollow'
>>> for m in re.finditer('ll', text):
         print('ll found', m.start(), m.end())

ll found 1 3
ll found 10 12
ll found 16 18
'''

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# from math import factorial
# import re
# number = factorial(1024)
# print(number)
# string = str(number)
# for m in re.finditer('0', string):
#     print('0 found ', m.start())

t = int(input());
p = [];
for i in range(t):
	n = int(input());
	k = 5;
	a = 0;
	while (True):
		a = int(a + n / k);
		k = k*5;
		if (n/k < 1):
			break;
	print(a);