def boble(array):
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


print("введите список")

arrayTest = list(map(int, input().split()))

print((' '.join(map(str, boble(arrayTest)))))