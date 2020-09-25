import sys

p = int(sys.stdin.readline())

for i in range(p):
    ra, d, rb, e, rc = map(str, sys.stdin.readline().split())

    b = int(rb)
    c = int(rc)
    a = int(ra[:-1])

    if a == 0 and ((c-b) != 0):
        print("Equation",i+1)    
        print("No solution.")
    if a == 0 and ((c-b) == 0):
        print("Equation",i+1)
        print("More than one solution.")
    if a != 0:
        x = (c-b)/a
        print("Equation",i+1)
        print("x =", "%.6f"%x)