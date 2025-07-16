with open('file.txt', 'r') as file:
    res = file.read().replace('\n', '')
res = res.split(' ')
text = 'aeiou'
for word in res:
    i = 0
    j = 0
    while True:
        if i == len(text) and j <= len(word):
            print(word)
            break
        elif i < len(text) and j >= len(word):
            break
        elif text[i] == word[j]:
            i += 1
            j += 1
        else:
            j += 1