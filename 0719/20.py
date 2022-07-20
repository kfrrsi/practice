number = 123

result = 0
while number:
    result += number%10
    number //= 10
    
print(result)