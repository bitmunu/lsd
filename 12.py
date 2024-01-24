def quick_sort(a):
    if len(a) <= 1:
        return a

    base = a[len(a)-1]
    left = list(filter(lambda x: x < base, a))
    center = [i for i in a if i == base]
    right = list(filter(lambda x: x > base, a))

    return quick_sort(left) + center + quick_sort(right)


def finalwrite (i, array): # записать в ответ с номером i список чисел
    with open(f"ans{i}.txt", "w") as f:
        temp_s = ' '.join(map(str, array))
        f.write(temp_s)


i = 0
while True:
    try:
        with open(f'example{i}.txt') as file: # открыть первый подфайл для чтения
            array = list(map(int, file.read().split())) # прочитать оттуда числа и отсортировать
            array = quick_sort(array) #
            print(array)
        with open(f"temp{i}.txt", "w") as file: #
            temp_str = ' '.join(map(str, array)) #
            file.write(temp_str) # записать прочитанный и отсортированный список в новый буферный файл с номером i
    except FileNotFoundError: # нет файла
        break
    i += 1
# сколько example'ов, столько и temp'ов

min_file_ind = 0 # номер файла с минимумом
ans_file_cnt = 0
temp_ans_array = [] # временный список для рзультата
while True: #
    temp_file_array = [] #
    flag = False #
    minim = 99999999999 #
    for j in range(i): # читаем сортированные списки из временных файлов
        with open(f"temp{j}.txt") as file: #
            array = list(map(int, file.read().split())) #
            if len(array) != 0: #
                flag = True #
                if array[0] < minim: # находим среди временных файлов тот, который содержит наименьший первый элемент
                    # (меньший из меньших, тк сортированы)
                    minim = array[0] #
                    min_file_ind = j # нашли файл с минимальным элементом
                    temp_file_array = array # вытащили из этого файла список
                    del(temp_file_array[0]) # удалили минимальный элемент из этого списка

    if not flag:
        finalwrite(ans_file_cnt, temp_ans_array) #не нашли ни одного существующего списка
        break

    with open(f"temp{min_file_ind}.txt", "w") as file:
        temp_str = ' '.join(map(str, temp_file_array)) # записать в файл, где нашли минимум, последовательность без этого минимума в начале
        file.write(temp_str)

    if len(temp_ans_array) < 10:
        temp_ans_array.append(minim) # если массив еще неполной длины, то добавить элемент
    else:
        finalwrite(ans_file_cnt, temp_ans_array) #
        ans_file_cnt += 1 #
        temp_ans_array.clear()
        temp_ans_array.append(minim)