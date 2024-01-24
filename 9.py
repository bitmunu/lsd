def Up(l, i, limit):

    while(True):
        left = i*2 + 1
        right = i*2 + 2

        if max(left, right) < limit:
            if l[i] >= max(l[left], l[right]):
                break
            elif l[left] > l[right]:
                l[i], l[left] = l[left], l[i]
                i = left
            else:
                l[i], l[right] = l[right], l[i]
                i = right
        elif left < limit:
            if l[left] > l[i]:
                l[i], l[left] = l[left], l[i]
                i = left
            else:
                break
        elif right < limit:
            if l[right] > l[i]:
                l[i], l[right] = l[right], l[i]
                i = right
            else:
                break
        else:
            break

def heapsort(l):

    for j in range((len(l)-2)//2, -1, -1):
        Up(l, j, len(l))

    #print((' '.join(map(str, a))))

    for i in range(len(l)-1, 0, -1):
        l[0], l[i] = l[i], l[0]
        Up(l, 0, i)

    return l


print("введите список")

a = list(map(int, input().split()))
print((' '.join(map(str, heapsort(a)))))
