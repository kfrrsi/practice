word = input()
cnt = 0
for char in word:
    if char in ['a']:
        break 
    cnt += 1
    
    if char == len(word):
        cnt = -1
        
print(cnt)

