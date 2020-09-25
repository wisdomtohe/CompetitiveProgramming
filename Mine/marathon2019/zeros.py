array = ["1", "1" ,"1" ,"1" ,"1" ,"1" ,"1" ,"1" ,"1" ,"0" ,"0" ,"0"]


def handle_array_zero_count(array):
	compte = 0
	for item in array:
		if item == "0":
			compte = compte+1
	return compte

print(handle_array_zero_count(array))

def main():
	item = input()