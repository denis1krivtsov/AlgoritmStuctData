check = False
def addN(arr, current, ind):
    current += arr[ind]
    ind += 1
    checkNum(arr, current, ind)

def multi(arr, current, ind):
    current *= arr[ind]
    ind += 1
    checkNum(arr, current, ind)

def sub(arr, current, ind):
    current -= arr[ind]
    ind += 1
    checkNum(arr, current, ind)

def checkNum(arr, current, ind):
    global check
    if ind < 5:
        for i in range(ind, 5):
            addN(arr, current, i)
    if ind < 5:
        for i in range(ind, 5):
            multi(arr, current, i)
    if ind < 5:
        for i in range(ind, 5):
            sub(arr, current, i)
    if current == 23 and ind == 5:
        check = True


def perm(a, k=0):
   global check
   if not check:
       if k == len(a):
           checkNum(a, a[0], 1)
       else:
          for i in range(k, len(a)):
             a[k], a[i] = a[i] ,a[k]
             perm(a, k+1)
             a[k], a[i] = a[i], a[k]


if __name__ == "__main__":
    checkArr = [0, 0, 0, 0, 0]
    arr = list(map(int, input().split()))

    while (arr != checkArr):
        try:

            check = False
            perm(arr)
            if check:
                print("Possible")
            else:
                print("Impossible")

            arr = list(map(int, arr[:]))

        except:
            print("Impossible")
