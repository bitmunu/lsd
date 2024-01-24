print("введите массив")

a = list(map(int, input().split()))

for i in range(len(a)):
    mi = a[i]
    x = i

    for j in range(i+1, len(a)):
        if mi > a[j]:
            mi = a[j]
            x = j

    if x != i:
        temp = a[i]
        a[i] = a[x]
        a[x] = temp

print(a)
