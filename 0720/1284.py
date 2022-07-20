import sys
sys.stdin = open("1284_input.txt", "r")

t = int(input())

for i in range(1, t+1):
    P, Q, R, S, W = map(int,input().split())
    a = W*P
    if R > W:
        b = Q
    else:
        b = Q + S*(W-R)
    print(f'#{i} {min(a, b)}')
    

# 오류났던 코드
# t = int(input())

# for i in range(1, t+1):
#     P, Q, R, S, W = map(int,input().split())
#     a_case, b_case = 0, 0
#     a_case += W*P
#     b_case += Q
#     if W > R:
#         b_case += (W-R)*S
# print('#{} {}'.format(i, min(a_case, b_case)))


