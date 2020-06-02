def multi(arr):
    current = 1
    for el in arr:
        current *= int(el)
    return current

def permute(s, n, k=0):
    result = [[s]]
    if k == n:
        return result
    for i in range(1, len(s)):
        first = [s[:i]]
        rest = s[i:]
        for p in permute(rest, n, k+1):
            result.append(first + p)
    return result

while True:
    try:
        st = input()
        if len(st) == 0:
            break
        a, n = st.split()
        n = int(n)
        maxM = 0
        for arr in permute(a, n-1):
            if len(arr) == n:
                m = multi(arr)
                if maxM < m:
                    maxM = m

        print(maxM)

    except:
        break
