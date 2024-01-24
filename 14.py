def put(hasheer, value, hash_table):
    table[hasheer].append(value)

with open("twentytwo.txt") as file:
    song = file.read()

words = song.split()
table = []
for i in range(len(words)*2):
    table.append([])

for word in words:
    sum = 0

    for j in word:
        if j in "!.,?';":
            hasher = ord(j) % len(table)
            put(hasher, j, table)
            word = word[:len(word)-1]
        sum += ord(j)
    hasher = sum % len(table)
    put(hasher, word, table)

with open("table2.txt","w") as file:
    for i in range(len(table)):
        temp_string = f"{i} : {table[i]}\n"
        file.write(temp_string)