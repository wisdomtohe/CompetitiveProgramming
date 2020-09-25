import sys

n = int(sys.stdin.readline())

for i in range(n):
    q,d,m,p = 0,0,0,0
    c = int(sys.stdin.readline())

    q = c//25
    r = c%25
    d = r//10
    r = r%10
    m = r//5
    r = r%5
    p = r//1

    print(i+1, q, "QUARTER(S),",d, "DIME(S),",m, "NICKEL(S),",p, "PENNY(S)")
