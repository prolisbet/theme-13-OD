# O(n) - линейная сложность алгоритма

def line_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1


arr = [10, 20, 30, 40, 50]
print(line_search(arr, 30))
print(line_search(arr, 60))
