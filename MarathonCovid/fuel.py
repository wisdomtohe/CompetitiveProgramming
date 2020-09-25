import sys

p = int(sys.stdin.readline())

for i in range(p):
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    if (n-k) > 60:
        print(((n-k)-60)*3000 + (k+60)*1500)
    else:
        print((k+(n-k))*1500)