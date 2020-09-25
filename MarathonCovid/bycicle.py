import sys
i = 1
while True:
    d,r,t = sys.stdin.readline().split()
    d,r,t = float(d), int(r), float(t)
    if r == 0:
        break
    distance = float((d/63360) * r*3.1415927)
    vitesse = distance/(t/3600)

    print("Trip #{}:".format(i) ,"%.2f"%distance, "%.2f"%vitesse)
    i+=1