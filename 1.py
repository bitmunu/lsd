

def reImagine(s):
    powerArr = []
    flag = False
    power = ""
    mistakes=0

    for i in range(0, len(s)):

        if flag == True:
            index = i
            if s[index] in "0123456789":
                power += s[index]
                if i == len(s)-1:
                    powerArr.append(power)
            else:
                flag = False
                if power == "":
                    power = "1"
                    print("неправильно")
                    mistakes+=1
                powerArr.append(power)
                #print(len(powerArr))
                power = ""

        elif s[i] == '^':
            flag = True

    for i in s:
        if i in "0123456789":
            s = s.replace(i, "")

    #print(powerArr)
    count = 0
    s = list(s)
    newline = ""

    for i in range(0, len(list(s))):
        if s[i] == '^':
            s[i] = powerArr[count]
            count += 1
            s[i - 1] = str(s[i - 1]) * int(s[i])
            s[i] = ""

    for j in s:
        newline += j

    print(newline)
    return (newline, mistakes)


def isValid(s):
    stack = []
    misks = 0
    for i in range(0, len(s)):
        current = s[i]
        if IsClosedBracket(current) == 1:
            if len(stack) !=0:
                if Skobochki(current) != stack.pop():
                    misks += 1
                    #return 0
            else:
                misks += 1
                #return 0
        else:
            stack.append(current)

    if misks == 0:
        if len(stack) == 0:
            return 1, misks
        else:
            misks += 1
            return 0, misks
    else:
        return 0, misks


def IsClosedBracket(ch):
    if ch == ')' or ch == '}' or ch == ']':
        return 1


def Skobochki(ch):
    if ch == ')':
        return '('
    elif ch == '}':
        return '{'
    elif ch == ']':
        return '['


print("введите скобочки")
s = input()
s, mistokes1 = reImagine(s)
isVal = 0
isVal, mistokes2 = isValid(s)
mistokes2 += mistokes1
if isVal == 0:
    print("неправильно")
    print(mistokes2)
else:
    print("правильно")