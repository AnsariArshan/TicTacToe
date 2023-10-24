import random
run = True
for i in range(3):
	for j in range(3):
		print("|",3*i+j,"|",end="")
	print()
print("\n\n")

arr = [ [-1,-1,-1],
		[-1,-1,-1],
		[-1,-1,-1]
					]
choices = [0,1,2,3,4,5,6,7,8]
ch = random.randint(0,1)
while choices and run:
	if ch == 0:
		place = random.choice(choices)
		i = place//3
		j = place%3
		arr[i][j] = "X"
		choices.remove(place)

		for i in range(3):
			for j in range(3):
				if arr[i][j] != -1:
					print("|",arr[i][j],"|",end="")
				else:
					print("| "," |",end="")
			print()
		print("\n")
		ch = 1
	else:
		place = int(input("selct your choice: "))

		if place in choices:
			i = place//3
			j = place%3
			arr[i][j] = "O"
			choices.remove(place)
		else:
			print("Enter a valid choice: ")
			continue

		for i in range(3):
			for j in range(3):
				if arr[i][j] != -1:
					print("|",arr[i][j],"|",end="")
				else:
					print("| "," |",end="")
			print()
		print("\n")
		ch = 0



	for i in range(3):
		if(arr[i][0]==arr[i][1] and arr[i][0]==arr[i][2] and arr[i][0]!=-1):
			print(arr[i][0],"wins")
			choices =[]
			run = False

	for j in range(3):
		if(arr[0][j]==arr[1][j] and arr[0][j]==arr[2][j] and arr[0][j]!=-1):
			print(arr[0][j],"wins")
			choices =[]
			run = False

	if(arr[0][0]==arr[1][1] and arr[0][0]==arr[2][2] and arr[0][0]!=-1):
			print(arr[0][0],"wins")
			choices =[]
			run = False

	if(arr[0][2]==arr[1][1] and arr[0][2]==arr[2][0] and arr[0][2]!=-1):
			print(arr[0][2],"wins")
			choices =[]
			run = False


