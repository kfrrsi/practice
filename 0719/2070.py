import sys

sys.stdin = open("2070_input.txt", "r")
T = int(input())
for i in range(1, T+1):
    numbers = map(int, input().split())
    if numbers[0] > numbers[1]:
        result = '>'
    if numbers[0] == numbers[1]:
        result = '='
    if numbers[0] < numbers[1]:
        result = '<'
    print('#{} {}'.format(i, result))