"e-olimp merge_sort"

def merge_sort(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    if len(array) > 1:
        mid = len(array) // 2
        leftArr = array[:mid]
        rightArr = array[mid:]
        merge_sort(leftArr)
        merge_sort(rightArr)

        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i][0] < rightArr[j][0]:
                array[k] = leftArr[i]
                i += 1
            else:
                array[k] = rightArr[j]
                j += 1
            k += 1

        while i < len(leftArr):
            array[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            array[k] = rightArr[j]
            j += 1
            k += 1
    return array  # TODO: реалізуйте відповідний алгоритм тут

n = int(input())
array = []
for i in range(n):
    arr = list(map(int, input().split(" ")))
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    array.append(arr)

array = merge_sort(array)

for i in array:
    print(i[0], i[1])
