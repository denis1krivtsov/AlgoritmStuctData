
def sort(array, n):
    b = False
    for i in range(1, n):
        currentValue = array[i]
        position = i
        while position > 0:
            if array[position-1] > currentValue:
                array[position] = array[position-1]
                b = True
            else:
                break
            position -= 1
        array[position] = currentValue
        if b:
            b = False
            print(" ".join(map(str, array)))
    return array

n = int(input())
arr = list(map(int, input().split(" ")))
sort(arr, n)