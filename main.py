def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def binary_search(array, element, left, right):
    if left > right:
        return left

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

sequence = str(input("Введите последовательность чисел через пробел ")).split()
sequence = list(map(int, sequence))

number = int(input("Введите число "))

qsort(sequence, 0, sequence.__len__() - 1)

print(sequence)
next_element_index = binary_search(sequence, number, 0, sequence.__len__() - 1)
previous_element_index = next_element_index - 1

if previous_element_index >=0:
    print("Индекс элемента меньшего числа —", previous_element_index)
else:
    print("Число является наименьшим элементом")

if next_element_index > sequence.__len__() - 1:
    print("Число является наибольшим элементом")
else:
    print("Индекс элемента больше или равного числа —", next_element_index)
