import sys
sys.stdin = open("1545_input.txt", "r")

n = int(input())
for i in range(n, -1, -1):
    print(i, end=' ')
