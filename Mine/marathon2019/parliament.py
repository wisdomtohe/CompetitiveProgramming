def process(n,m,k):
	win_if = int((n/2))+1
	r = n -(m+k)
	if m >= win_if:
		return 0
	if((m+r) >= (win_if)):
		# return (win_if-(m+r))
		return r
	else:
		return -1


def main():
	f = open("parliament.in", 'r')
	while True:
		n, m, k = f.readline().split(" ")
		if (n == m == k == '0'):
			break
		print(process(int(n),int(m),int(k)))


if __name__ == '__main__':
	main()