print("Learn whether or not your dog can be learn new tricks.") ##Intro Prompt
dogName = input("Enter the dog's name: ") ##Ask for the dog's name
calendarAge = int(input("Enter the dog's calendar age: ")) ##Ask for dog's calendar age

if (calendarAge > 16): ##prompts situation if dog is too old for tricks
    print(dogName, " is too old to remember tricks.")
elif (calendarAge > 8) : ##prompts situation if dog is old enough to do tricks
    print(dogName, " cannot be taught tricks.") 
else: ##prompts situation if dog is too young to earn tricks
    print(dogName, " is ready to learn new tricks!")
            
dogAge = calendarAge * 7 ##Calculates the dog's real age

yourAge = int(input("Enter your age: ")) ##Asks for user's age

print(dogName, "is ", dogAge, " years old.") ##Shows the dog's real age

if (yourAge > dogAge): ##Prompts sitation if user is older than dog
    print("You are effectively older than ", dogName, ".")
elif (yourAge == dogAge): ##Prompts situation if user is the same age as the dog
    print("You are the same age as ", dogName, ".")
else: ##Prompts sitation if user is younger than the dog
    print("You are younger than " , dogName, ".")
