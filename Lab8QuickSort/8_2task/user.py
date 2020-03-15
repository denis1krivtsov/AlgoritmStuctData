
"""
Реалізуйте підпрограму сортування масиву.
"""

N = 1000000  # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000



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

def sort(array):
    qsort(array, 0, len(array) - 1)
    pass
# arr = [1, 3, -10, 55, 1000, 10, 10, 2]
# print(qsort(arr, 0, len(arr)-1))

