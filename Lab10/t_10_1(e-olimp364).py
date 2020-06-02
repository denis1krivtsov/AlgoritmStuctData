def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

def d(alph, word, N, k, p):
    if p == 0:
        word += alph[0]
        return word

    num = int(k-1)//N
    word += alph[num]
    del alph[num]
    k -= num*N

    return d(alph, word, N//(p), k, p-1) # уменьшаю факториал N и вызываю функцию

lst = list("abcdefghijkl")
N, k = map(int, input().split())
print(d(lst[:N], "", fact(N-1), k, N-1))
