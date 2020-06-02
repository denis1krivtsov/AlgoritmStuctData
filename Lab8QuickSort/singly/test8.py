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

arr = [[9, 9], [6, -100], [11, 5], [1, 5], [5, 6], [7, 5]]
print(merge_sort(arr))