import sys

p = int(sys.stdin.readline())

for i in range(p):
    n,d,a = sys.stdin.readline().split()
    n = int(n)
    somme1 = 0
    somme2 = 0
    for i in range(n):
        ld,la,di = sys.stdin.readline().split()
        di = int(di)
        if ld == d or ld == a:
            ld = d
            somme1+=di
        if la == d or la == a:
            la = a
            somme2+=di
    print(d,a,min(somme1, somme2))