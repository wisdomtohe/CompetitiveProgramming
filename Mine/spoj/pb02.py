from math import sqrt, floor
t = int(input())
def isPrime(nombre):
	i = 2
	while i < nombre and nombre % i != 0 :
	    i = i + 1
	if i == nombre :
	    return True
	else :
	    return False

def isPrime2(n):
    for i in range(2, int(sqrt(n) + 1)):

        if n % i == 0:
            return False
            break
    else:
        return True

def isPrime3(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = floor(sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % 2 == 0:
            return False
    return True
    
	    
for i in range(t):
    a,b = map(int, input().split())
    for i in range(a,b):
        if isPrime3(i) : print(i)
    print('')