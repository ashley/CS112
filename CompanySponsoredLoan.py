#Introduce users to the program
print("This program will determine whether or not you are eligible for a company sponsored loan.")
employeeName = input("Enter your name: ")
employeeYears = int(input("Enter the amount of years you have been working at this company (please enter a number): "))
employeeSalary = float(input("Enter your salary: $"))

#If Employee is eligible for a loan..
if (employeeYears < 2):
    print("I'm sorry, ", employeeName, "You are not eligible for a company sponsored loan.")
elif (employeeSalary < 24000):
    print("I'm sorry, ", employeeName, "You are not eligible for a company sponsored loan.")
else:
    print("Congratulations ", employeeName, "! You are eligible for a company sponsored loan.")
