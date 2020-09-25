import sys

p = int(sys.stdin.readline())

for i in range(p):
    # a, b, c = map(int, _in.split())
    n, m = map(int, sys.stdin.readline().split())
    cand = []
    suffrage = []

    for i in range(n):
        cand.append(sys.stdin.readline())
    for i in range(m):
        suffrage.append(sys.stdin.readline())
    
    x = suffrage[0]
    r = int(suffrage[1])
    c = suffrage[2]

    winner = ""

    for i in range(n):
        for j in range(m):
            
            

    if x == "":
        print("VOTE {}: THE WINNER IS").__format__(i)
