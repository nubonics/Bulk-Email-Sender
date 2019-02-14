from random import randint


def code_generator():
	alpha_numeric = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
	raw_identifier = list()
	identifier = ''
	for char in range(10):
		random_number = str(alpha_numeric[randint(0,len(alpha_numeric)-1)])
		raw_identifier.append(random_number)
		identifier += random_number
		
	return identifier


if __name__ == "__main__":
	code_generator()