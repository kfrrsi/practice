word = input()
for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        print(chr(ord(word[i])+32), end='')
    else :
        print(chr(ord(word[i])-32), end='')