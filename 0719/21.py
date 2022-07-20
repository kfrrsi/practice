n = 123

#print(int(str(n)[::-1]))
result = 0
while n:
    result *= 10
    result += n%10
    n //= 10

print(result)