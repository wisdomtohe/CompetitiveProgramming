def brent_cycle_detect(f, x0):
  # main phase: search successive powers of two
  power = lam = 1
  tortoise = x0
  hare = f(x0)  # f(x0) is the element/node next to x0.
  while tortoise != hare:
    if power == lam:  # time to start a new power of two?
      tortoise = hare
      power *= 2
      lam = 0
    hare = f(hare)
    lam += 1

  # Find the position of the first repetition of length λ
  mu = 0
  tortoise = hare = x0
  for i in range(lam):
    # range(lam) produces a list with the values 0, 1, ... , lam-1
    hare = f(hare)
    # The distance between the hare and tortoise is now λ.

  # Next, the hare and tortoise move at same speed until they agree
  while tortoise != hare:
    tortoise = f(tortoise)
    hare = f(hare)
    mu += 1

  return lam, mu


case_no = 1
while True:
  z, i, m, l = list(map(int, input().split()))

  if z == i == m == l == 0:
    break

  f = lambda l: (z*l+i) % m
  print("Case {}: {}".format(case_no, brent_cycle_detect(f, l)[0]))
  case_no += 1
