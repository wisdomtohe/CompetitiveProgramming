def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)

def solve():
    s = 0
    i = 0
    # for i in range(10):
    while i<=9:
        s += 1/fact(i)
        print(i, s)
        i += 1

print("n e")
print("- -----------")
print(solve())