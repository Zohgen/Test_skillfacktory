def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


test_member = list(map(int, input("введите последовательность чисел:\n").split()))
min_number = min(list(map(int, test_member)))
max_number = max(list(map(int, test_member)))
y = int(input(f"введите число в диапазоне от {min_number} и до {max_number} : \n"))
while (y >= max_number or y <= min_number): #проверка ввода числа в диапазоне списка
    y = int(input(f"введите число в диапазоне от {min_number} и до {max_number}  : \n"))
    if (min_number < y < max_number):
        break

result = test_member.count(y) #проверка введенного числа на наличие в списке
if result > 0:
    print(f"число {y} уже есть в последовательности \n")
else:
    test_member.append(y)
    print(f"число {y} добавлено в список: {test_member} \n")

test_member = sorted(test_member) #сортируем последовательность
print(f"сортируем числовую последовательность: {test_member} \n")
print(f"вывод индекса меньшего (левого ) числа от введеного пользователем:{((binary_search(test_member, y, 0, len(test_member) - 1))-1)}")
#вывод индекса меньшего (левого ) числа от введеного пользователем