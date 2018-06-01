import sys

def enumeratePrime(n):
    if n < 2:
        return []

    if n == 2:
        return [2]

    arr = {}
    for i in range(2, n+1):
        arr[i] = True

    i = 2
    while (i**2 <= n):
        if arr[i] == True:
            j = i * 2
            while j < n:
                arr[j] = False
                j += i
        i += 1

    res = []
    for i in range(2,len(arr)):
        if arr[i] == True:
            res.append(i)

    print res

n = 25
enumeratePrime(n)
