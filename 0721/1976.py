import sys

sys.stdin = open("1976_input.txt", "r")

T = int(input())
h = 0
m = 0

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    h = numbers[0] + numbers[2]
    m = numbers[1] + numbers[3] 
    if m > 59:
        m -= 60
        h += 1
    if h > 12:
        h -= 12
    print('#{} {} {}'.format(tc, h, m))
    # print(f'#{tc} {h} {m}')
