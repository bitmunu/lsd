print("введите массив")

a = list(map(int, input().split()))

print(a)

for i in range(1, len(a)):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j-1], a[j] = a[j], a[j-1]
        else:
            break

print(a)
