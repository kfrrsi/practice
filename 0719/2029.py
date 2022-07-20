import sys
sys.stdin = open("2029_input.txt", "r")

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(int,sys.stdin.readlline().split())
    print("#%d %d %d"%(i+1, a//b, a%b))
