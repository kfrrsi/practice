#students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
cnt = 0
for vote in students:
    if '이영희' == vote:
        cnt += 1
print(cnt)