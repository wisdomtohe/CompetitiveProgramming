def process(X,Y,Z):
	a, b, c = 0, 0, 0
	x = 0
	total = [x in range(1000)]
	premier = ((a - b) == X) or ((a - b) == -X)
	deuxieme = ((b - c) == Y) or ((b - c) == -Y)
	troisieme = ((c - a) == Z) or ((c - a) == -Z)
	for i in range(1000):
		a = i
		for j in range(1000):
			b = j
			if premier:
				for k in range(1000):
					c = k
					if deuxieme:
						if troisieme:
							return "yes"
							break
		return "no"

	while x<1000:
		pass

def main():
	# T = input()
	X,Y,Z = input().split(" ")

	print(process(int(X), int(Y), int(Z)))

if __name__ == '__main__':
	main()