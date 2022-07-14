from multiprocessing.pool import ApplyResult


word = input()
cnt = 0
for char in word:
    if char == 'a':
        cnt += 1
print(cnt)