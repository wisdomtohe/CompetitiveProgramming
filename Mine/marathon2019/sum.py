def position():
	for i in range(n):
		for entry in tab:
			if sum(int(entry[:i]+entry[i:]))


def main():
	tab = []
	while True:
		n = input()
		a,b,c = input().split("\n")
		if n == "0":
			break
		tab.append(a, b, c)


if __name__ == '__main__':
	main()
