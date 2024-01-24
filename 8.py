def xdd(orig, place):
    countList = [0] * 10
    size = len(orig)

    for i in range(size):
        placeElement = (orig[i] // place) % 10
        countList[placeElement] += 1

    for i in range(1, 10):
        countList[i] += countList[i - 1]

    output = [0] * size
    i = size - 1

    while i >= 0:
        currentEl = orig[i]
        placeElement = (orig[i] // place) % 10
        countList[placeElement] -= 1
        newPosition = countList[placeElement]
        output[newPosition] = currentEl
        i -= 1

    return output


def radixxxd(inputArray):
    maxEl = max(inputArray)

    D = 1
    while maxEl > 0:
        maxEl /= 10
        D += 1

    place = 1
    outputArray = inputArray

    while D > 0:
        outputArray = xdd(outputArray, place)
        place *= 10
        D -= 1

    return outputArray

def splitter(l):
    new1 = []
    new2 = []

    for i in range(0, len(l)):
        if l[i] < 0:
            new1.append(l[i])
        else:
            new2.append(l[i])

    return new1, new2

def joiner(l1, l2):
    for i in range(0, len(l2)):
        l1.append(l2[i])
    return l1

print("введите список")

a = list(map(int, input().split()))
b, c = splitter(a)
a = joiner(radixxxd(b), radixxxd(c))
print((' '.join(map(str, a))))
