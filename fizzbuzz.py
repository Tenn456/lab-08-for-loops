for i in range(1, 101, 1):
	multipleOfThree = i % 3
	multipleOfFive = i % 5

	if multipleOfThree == 0 and multipleOfFive == 0:
		print("FizzBuzz")
	elif multipleOfThree == 0:
		print("Fizz")
	elif multipleOfFive == 0:
		print("Buzz")
	else:
		print(i)