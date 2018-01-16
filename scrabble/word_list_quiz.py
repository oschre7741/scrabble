with open ("words_alpha.txt", "r") as f:
    words = f.read().splitlines()
#total number of words
print(len(words))

#number of 5 letter words
count = 0
for w in words:
    if len(w) == 5:
        count += 1

print(count)

#number of words longer than 7 letters
count = 0
for w in words:
    if len(w) > 7:
        count += 1

print(count)

#total number of characters
count = 0
for w in words:
    count += len(w)

print(count)

#number of words w/o letter e
count = 0
for w in words:
    if "e" not in w:
        count += 1

print(count)

#number of words that start and end w/ same letter
count = 0
for w in words:
    if w[0] == w[-1]:
        count += 1

print(count)

#number of words w 3 'a's
count = 0
uniq = []
for w in words:
    if w.count("a") == 3:
        count += 1

print(count)

#words that have a q not followed by u
count = 0
for w in words:
    if "q" in w and "u" not in w:
        count += 1

print(count)




