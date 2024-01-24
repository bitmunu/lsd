from math import log
#  дается ичсло x, вывести все числа от 1 до x, удовлетворяющие условию
#  3^k * 5^l * 7^m = x[i]
def simple_multipiers(x):
    res = []
    for m in range(int(log(x, 7)) + 1):
        for l in range(int(log(x, 5)) + 1):
            for k in range(int(log(x, 3)) + 1):
                xi = 3**k * 5**l * 7**m
                if xi <= x:
                    res.append(xi)
                else:
                    break
    return res


x = int(input("Введите число х: "))
print("Числа, удовлетворяющие заданному условию:", end=' ')
print(simple_multipiers(x), sep=", ")

