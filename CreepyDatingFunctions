def main():
	print("This program determines whether you can date someone based on their age")
	age = int(input("Enter their age in a whole number: "))
	userAge = int(input("Enter your age in a whole number: "))
	youngAge = youngestCalc(userAge)
	oldAge = oldestCalc(userAge)
	determine(oldAge,youngAge,age,userAge)
	
	print("Thanks for using this program!")
	
def youngestCalc(age):
	youngest = age/2 + 7
	return youngest
	
def oldestCalc(age):
	oldest = 2*age - 14
	return oldest

def determine(old, young, age, personage):
	print(old,young,age,personage)
	if young < personage < old:
		print("You can successfully date this person!")
	else:
		print("No, You're creepy")

main()
