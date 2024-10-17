# O(log n) = логарифмическая сложность алгоритма

def binary_search(array, element):
    low, high = 0, len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        if array[middle] == element:
            return middle
        elif array[middle] < element:
            low = middle + 1
        else:
            high = middle - 1
    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binary_search(arr, 70))
print(binary_search(arr, 25))
