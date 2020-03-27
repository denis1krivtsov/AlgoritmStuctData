def lowLst(arr, i, j):
    n = len(arr)
    n_arr = []
    for k in range(n):
        if k != i and k != j:
            n_arr.append(arr[k])
    return n_arr

count = 0
def cookie(arr, sumN, sumB):
    n = len(arr)
    global count
    if n == 0:
        count += 1
        return sumN

    for i in range(n):
        for j in range(n):
            if sumN > sumB:
                sumN += arr[j]
                sumB += arr[i]
            else:
                sumN += arr[i]
                sumB += arr[j]
            cookie(lowLst(arr, i, j), sumN, sumB)


maxCookie = 0
n = int(input())
arr = list(map(int, input().split()))
n = n*2
for i in range(n):
    for j in range(n):
        c = cookie(lowLst(arr, i, j), arr[i], arr[j])
        if maxCookie < c:
            maxCookie = c

print(maxCookie)