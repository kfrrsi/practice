number = 123
# 1. 문자열로 형변환 print(len(str(number)))
# 1x100 2X10 3X1 
# while문 접근이 중요
# 종료조건은 몫이 0!!!!!
result = 0
while number:
    number //= 10
    result += 1
print(result)
