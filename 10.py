def merge(a1, a2):
    final = []
    i = 0
    j = 0

    while (i < len(a1)) and (j < len(a2)):
        if a1[i] <= a2[j]:
            final.append(a1[i])
            i += 1
        else:
            final.append(a2[j])
            j += 1

    final += a1[i:] + a2[j:]
    return final


def split(lizt):
    size = len(lizt) // 2
    l1 = lizt[:size]
    l2 = lizt[size:]

    if len(l1) > 1:
        l1 = split(l1)
    if len(l2) > 1:
        l2 = split(l2)

    return merge(l1, l2)

print("введите массив")

a = list(map(int, input().split()))
a = split(a)
print(a)
