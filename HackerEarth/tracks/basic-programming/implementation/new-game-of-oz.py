__author__ = 'narendra'

'''
Today Oz is playing a new game. He has an array arr[] of N distinct integers . In each turn he is will follow two actions -
1) He select a random number from arr[]. Say value of this element is X.
2) He will remove X from arr[]. if X-1 is present in arr[] then he will remove it. if X+1 is present in arr[] then he will remove it.
Oz will make turns until arr[] becomes empty. Oz loves this game so he wants to make maximum number of possible turns.

Help Oz to make maximum number of possible turns.

Input :
The first line contains the number of test cases - T . Each test case consist of two lines. First line will contain

a integer N - number of elements in arr[]. Second line will contain N space separated integers.

Output :
For each test case output maximum number of possible turns that Oz can make.

SAMPLE INPUT
1
6
291 292 295 297 298 299
SAMPLE OUTPUT
4
'''

from random import randint

def remove_elements(array):
    max_count = 0
    array_length = len(array)
    while array_length > 0:
        random_number = randint(0, array_length)
        print random_number
        array_length -= 1
        if array[random_number]:
            del array[random_number]
        elif array[random_number]:
            pass


if __name__ == '__main__':
    test_cases = int(raw_input())
    for _ in range(test_cases):
        array_size = int(raw_input())
        array = map(int, raw_input().split())
        remove_elements(array)