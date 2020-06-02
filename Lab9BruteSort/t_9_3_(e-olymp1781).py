def lowLst(arr, i, j):
    n_arr = []
    n = len(arr)
    for el in range(n):
        sub = []
        for el2 in range(n):
            if el != i and el2 != j:
                sub.append(arr[el][el2])
        if len(sub) > 0:
            n_arr.append(sub)
    return n_arr


def func(arr, minSum):
    global minF
    n = len(arr)
    if n == 0:
        if minF > minSum:
            minF = minSum
    for i in range(n):
        for j in range(n):
            minSum += arr[i][j]
            func(lowLst(arr, i, j), minSum)

n = int(input())
arr = []
minF = 10**6
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n//2 + 1):
    for j in range(n):
        func(lowLst(arr, i, j), arr[i][j])
print(minF)