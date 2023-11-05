





























### Important Question

K = 2
M = 4
n = K
while True:
    x = sorted(range(1,n+1), key=str)
    i = 1
    if x.index(K)+1 == M:
        print(n)
        break
    if x.index(K)>M:
        print("not possible")
        break
    n = n+1