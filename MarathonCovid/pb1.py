import sys

p = int(sys.stdin.readline())

for i in range(p):
    ra, d, rb, e, rc = map(str, sys.stdin.readline().split())

    b = int(rb)
    c = int(rc)
    a = int(ra[:-1])

    x = (c-b)/a

    print("Equation",i+1)

    if a == 0 and b != 0:    
        print("No solution.")
    if a == 0 and b == 0:
        print("More than one solution.")
    if a != 0:
        print("x =", "%.6f"%x)