
def put(hesheer, value, hash_table):
    if table[hesheer] == 0:
        table[hesheer] = value

with open("twentytwo.txt") as file:
    song = file.read()

words = song.split()
table = [0]*(len(words)*2)

for i in words:
    sum_of_ords = 0
    k_counter = 1
    counter2 = 0
    for j in i:
        if j in ';:,%".!?' or j == '\'':
            i = i[:k_counter-1] + i[k_counter:]
        k_counter+=1
        sum_of_ords += ord(j)
    hasher = (sum_of_ords+counter2) % len(table) + counter2*(1 + sum_of_ords%(len(table)-1))
    put(hasher, i, table)
    counter2+=1


with open("hashtable.txt","w") as file:
    for i in range(len(table)):
        temp_string = f"{i} : {table[i]}\n"
        file.write(temp_string)
file.close()
