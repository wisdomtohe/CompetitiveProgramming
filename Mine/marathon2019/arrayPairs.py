array = [5, 0, 10, 2, 4, 1, 6]


def handle_array(array):
	nombre = 0
	for i in range(len(array)-1):
		j=i+1
		for j in range(len(array)-1):
			if (array[i]*i) > (array[j]*j):
				nombre += 1

	return nombre

print(handle_array(array))