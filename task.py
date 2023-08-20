def InputData():
	with open("db.dat", "a") as f:
		arr = []
		arr.append(input("Input surname: "))
		arr.append(input("Input name: "))
		arr.append(input("Input patronymic: "))
		arr.append(input("Input name of the company: "))
		arr.append(input("Input work phone: "))
		arr.append(input("Input personal phone: "))

		for i in range(len(arr)):
			if i != 3:
				arr[i] = arr[i].replace(" ", "")

		for i in arr:
			f.write(i)
			f.write(" ")
		f.write("\n")

def OutputData():
	print()
	with open("db.dat", "r", encoding="utf-8") as f:
		while True:
			line = f.readline()
			if not line:
				break
			for i in line:
				print(i, end="")
	print()

def EditData():
	print()
	print("If you want to leave the field as it was input $")

	with open("db.dat", "r") as f:
		lines = f.readlines()

	while True:
		try:
			n = int(input("Input number of line to edit: "))
			if n < 1 or n > len(lines):
				print("Invalid line number! Please try again.")
			else:
				break
		except:
			print("Input number!")

	arr = []
	arr.append(input("Input surname: "))
	arr.append(input("Input name: "))
	arr.append(input("Input patronymic: "))
	arr.append(input("Input name of the company: "))
	arr.append(input("Input work phone: "))
	arr.append(input("Input personal phone: "))

	for i in range(len(arr)):
		if i != 3:
			arr[i] = arr[i].replace(" ", "")
	
	for i in range(len(arr)):
		if arr[i] == "$":
			arr[i] = lines[n - 1].split(" ")[i]

	lines[n - 1] = " ".join(arr) + "\n"

	with open("db.dat", "w") as f:
		f.writelines(lines)

def FindDataByName():
    name = input("Input name to search: ").lower()
    with open("db.dat", "r") as f:
        lines = f.readlines()
    found = False
    for line in lines:
        if name in [x.lower() for x in line.split(" ")]:
            print(line, end="")
            found = True
    if not found:
        print("No entries found with the given name.")
    print()

while True:
	print("1. Input new entry\n2. Show whole entries\n3. Edit data\n4. Find entry by Name\n")
	n = input("Input option: ")
	match n:
		case '1':
			InputData()
		case '2':
			OutputData()
		case '3':
			EditData()
		case '4':
			FindDataByName()
		case _:
			print("Choose from 1 to 4!")


