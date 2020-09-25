def findValleys(n, s):
    compteur = 0
    marqueur = 0
    if s[i] == "U":
        marqueur = 1
    else:
        marqueur = -1

    start = (s[i] == "U" and s[i+1] == "D")

    for i in s:        
        if start :
            compteur += 1
            if !start:
