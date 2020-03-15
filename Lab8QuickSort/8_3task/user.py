
"""
Реалізуйте підпрограми сортування масиву.
"""

N = 10000    # Кількість елементів масиву.
              # Використовується у головній програмі для генерування
              # масиву з випадкових чисел


def bubble_sort(array):
    """ Сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    """
    n = len(array)
    k = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                k += 1
                array[j], array[j+1] = array[j+1], array[j]

    pass  # TODO: реалізуйте відповідний алгоритм тут

def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"

    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    k = 0
    for i in range(n - 1, 0, -1):
        sortCheck = 0
        for j in range(i):
            if array[j] > array[j + 1]:
                k += 1
                array[j], array[j + 1] = array[j + 1], array[j]
            else:
                sortCheck += 1
        if sortCheck == i:
            break
    pass # TODO: реалізуйте відповідний алгоритм тут


def selection_sort(array):
    """ Сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(n-1, 0, -1):
        currentMax = 0
        for j in range(1, i+1):
            if array[currentMax] < array[j]:
                currentMax = j
        array[i], array[currentMax] = array[currentMax], array[i]
    pass


def insertion_sort(array):
    """ Сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    # TODO: реалізуйте відповідний алгоритм тут
    for i in range(1, n):
        currentValue = array[i]
        position = i
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue
    pass  # TODO: реалізуйте відповідний алгоритм тут


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
    pass  # TODO: реалізуйте відповідний алгоритм тут


def qsort(array, a, b):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    if a >= b:
        return
    pivot = array[a + (b - a)//2]
    left = a
    right = b

    while True:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left >= right:
            break
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    qsort(array, a, right)
    qsort(array, right + 1, b)
    pass# TODO: реалізуйте відповідний алгоритм тут

def quick_sort(array):
    """ Швидке сортування

        :param array: Масив (список однотипових елементів)
        :return: None
        """
    qsort(array, 0, len(array) - 1)
    pass  # TODO: реалізуйте відповідний алгоритм тут

