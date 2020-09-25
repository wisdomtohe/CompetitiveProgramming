import sys
import math

def estCarreParft(nbr):
    if str(math.sqrt(nbr)).endswith('.0'):
        return True
    
n = int(sys.stdin.readline())
tab = list(map(int, sys.stdin.readline().split()))
res = []
for i in range(n):
    if not estCarreParft(tab[i]):
        res.append(tab[i])
print(max(res))