
def xd(l):
    gap = int(len(l) / 2)

    while gap > 0:

        for i in range(gap, len(l)):

            current = l[i]
            position = i

            while position >= gap and l[position - gap] > current:
                l[position] = l[position - gap]
                position -= gap
                l[position] = current

        gap = int(gap/2)
        print(l)

    return l


print("введите список")

a = list(map(int, input().split()))

print((' '.join(map(str, xd(a)))))
