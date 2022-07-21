import sys

sys.stdin = open("1989_input.txt", "r")

word = int(input())

for i in range(word):
    a = input()
    if a == a[::-1]:
        result = 1
    else:
        result = 0
    
    print('#{} {}'.format(i+1, result))
    

    