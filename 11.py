def quick_sort(a):
    if len(a) <= 1:
        return a

    base = a[len(a)-1]
    left = list(filter(lambda x: x < base, a))
    center = [i for i in a if i == base]
    right = list(filter(lambda x: x > base, a))

    return quick_sort(left) + center + quick_sort(right)


print("введите список")

a = list(map(int, input().split()))
print((' '.join(map(str, quick_sort(a)))))
