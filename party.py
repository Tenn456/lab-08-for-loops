userinput = input("Let's party! How long until the party?: ")
userint = int(userinput, 10);

if userint < 1:
	print("PARTY NOW!")
else:
	for i in range(userint, 0, -1):
		print(i)
		if i == 1:
			print("PARTY TIME!")