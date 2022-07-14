from multiprocessing.pool import ApplyResult


word = 'apple'
newword = ''
for char in word:
    newword = char + newword
print(newword)