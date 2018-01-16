with open ('scrabble_list.txt', 'r') as f:
    words = f.read().splitlines()
    print(words)

print(words[:10])

count = 0
for w in words:
    if 'e' not in w:
        count += 1

print(count)
