"e-olimp Сортировка по росту"

def merge_sort(array):
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
            if leftArr[i] < rightArr[j]:
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
    return array

def countElemArray(array, a, b):
    array = merge_sort(array)
    print(array)
    left = 0
    right = 0
    limitA = len(array)

    while left < limitA:
        if array[left] > a:
            break
        left += 1
    right = left
    while right < limitA:
        if array[right] <= b:
            break
        right += 1
    return right - left

c = int(input())
array = list(map(int, input().split(" ")))
rangeA = input().split(" ")
print(countElemArray(array, int(rangeA[0]), int(rangeA[1])))