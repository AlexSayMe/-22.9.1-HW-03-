array = input("Введите последовательность чисел через пробел:").split()
array_list = list(map(int, array))

print(type(array_list))

for i in range(len(array_list)):
    for j in range(len(array_list) - i - 1):
        if array_list[j] > array_list[j + 1]:
            array_list[j], array_list[j + 1] = array_list[j + 1], array_list[j]

print(array_list)

N = len(array_list)
print(N)


def binary_search(array_list, number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array_list[middle] == number:
        return middle
    elif number < array_list[middle]:
        return binary_search(array_list, number, left, middle - 1)
    else:
        return binary_search(array_list, number, middle + 1, right)


number = int(input("Введите число:"))

print(type(number))

array_list = [i for i in range(array_list[-1])]

print(binary_search(array_list, number, array_list[0], array_list[-1]))
