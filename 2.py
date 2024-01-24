line = input()
nums, operations, priorities = [], [], []
int_buffer, cur_priority, max_priority = '', 0, 0

opposites = {")": "(", "}": "{", "]": "["}
result, storage, count = True, [], -1
for char in line:  # рассматриваем каждый символ в строке

    if char in opposites.values():  # если нам встретилась открывающая скобка
        storage.append(char)  # добавим ее в конец массива
        count += 1  # и запишем, что нам встретилась открывающая скобка
    elif char in opposites.keys():
        if count == -1:  # если нам встретилась закрывающая скобка,
            result = False  # но массив с открывающими скобками оказался пуст
            break  # выйдем из программы
        count -= 1
        if storage.pop() != opposites[char]:  # если открывающая скобка с конца массива
            result = False  # не соответствует виду закрывающей скобки
            break  # выйдем из программы

if result or count == -1:
    for char in line:
        if char in '0123456789': # встретилась цифра
            int_buffer += char # запихиваем в буфер
        if char in '+-*/': # встретилась операция
            if len(int_buffer) > 0: # если есть цифра перед операцией
                nums.append(int(int_buffer)) # добавляем ёё в нормальный список
                int_buffer = '' #
            operations.append(char) # добавляем в список операций текущую операцию
            if char in '+-': #
                priorities.append(cur_priority) # приоритет низкий
            if char in '*/': #
                priorities.append(cur_priority + 1) # приоритет жесткий
                if cur_priority + 1 > max_priority: #
                    max_priority = cur_priority + 1 # делаем приоритет самым жестким если он больше чуть менее жесткого
        if char in '({[': #
            cur_priority += 2 #
        if char in ')}]': #
            cur_priority -= 2 #
        if cur_priority > max_priority: #
            max_priority = cur_priority #
    nums.append(int(int_buffer)) #

    while max_priority >= 0: # выполняем операции
        i = 0 #
        while i < len(operations):
            if priorities[i] == max_priority:
                if operations[i] == '+':
                    nums[i] = nums[i] + nums[i + 1]
                elif operations[i] == '-':
                    nums[i] = nums[i] - nums[i + 1]
                elif operations[i] == '*':
                    nums[i] = nums[i] * nums[i + 1]
                elif operations[i] == '/':
                    if nums[i + 1] == 0:
                        max_priority = -10
                        break
                    nums[i] = nums[i] / nums[i + 1]
                nums.pop(i + 1)
                operations.pop(i)
                priorities.pop(i)
                i -= 1 #чтобы не превысить радиус индексации списка
            i += 1
        max_priority -= 1
    if max_priority > -10:
        print(nums.pop())
    else:
        print("деление на ноль") #
else:
    print("скобки расставлены неправильно")

#(2 * (10 * (28 + 14/2)))