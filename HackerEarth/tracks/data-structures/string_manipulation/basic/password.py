__author__ = 'Hinshitsu-IT'
'''
4
abc
def
feg
cba

3 b
'''
s = []
for _ in range(int(raw_input())):
    s.append(raw_input())

for i in s:
    if i[::-1] in s:
        print(str(len(i))+' '+ str( i[int(len(i)/2)] ))
        break