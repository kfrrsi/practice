import sys

sys.stdin = open("1288_input.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = [0] * 10
    i = 1
    while 0 in numbers:
        num = str(N * i)
        for j in range(len(num)):
            numbers[int(num[j])] += 1
        i += 1
    print('#{} {}'.format(tc, num))
