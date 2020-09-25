import sys
while True:
    d,r,t = map(int, sys.stdin.readline().split())
    if r == 0 and d == 0 and t == 0:
        break
    if(r-d == t-r):
        print("AP",t+(t-r))
    else:
        print("GP",int((r/d)*t))
