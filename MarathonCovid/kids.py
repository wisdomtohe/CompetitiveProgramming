import sys

p = int(sys.stdin.readline())

for i in range(p):
    l = []
    r = 0
    n,m = map(int, sys.stdin.readline().split())
    l = input().split()
    for j in range(n):
        r+= int(l[j])//m
    print(r)