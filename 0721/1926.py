import sys

sys.stdin = open("1926_input.txt", "r")

t = int(input())
a = '3', '6', '9'
result = ''

for i in range(1, t+1):
    b = str(i)
    clap = 0

    for j in range(len(b)):
        if b[j] in a:
            clap += 1
    if clap == 0:
        result += b
    else:
        result += '-'*clap
    result += ' '
print(result)