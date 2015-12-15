class Friend:
    def __init__(self, n, a, b):
        self.name = n
        self.age = a
        self.birthdate = b

    def __str__(self):
        return("name: " + self.name + ", age: " + str(self.age) + ", birthdate: " + self.birthdate)

def main():
    file = open("Friends.txt", "r")
    friendsList = []
    for lines in file:
        line = lines.strip()
        if line != '':
            friendsList.append(line)
    #print(friendsList)
    num = int(len(friendsList)/3)

    print("This program determines whether you can date someone based on their age")
    userAge = int(input("Enter your age in a whole number: "))
    year = int(input("How many years from now?: "))
    youngAge = int(youngestCalc(userAge+year))
    oldAge = int(oldestCalc(userAge+year))
    future(year,friendsList,num,youngAge,oldAge)

def future(year,friendsList,num,youngAge,oldAge):   
    listt = []
    for i in range(num):
       f = makeAFriend(friendsList, i, num)
       if youngAge < int(f.age)+year < oldAge:
           listt.append(str(f.name))
    if not listt:
        print("you can't date anyone from the list.")
    else:
        print("You can date: ", ', '.join(listt))


def youngestCalc(age):
	youngest = age/2 + 7
	return youngest
	
def oldestCalc(age):
	oldest = 2*age - 14
	return oldest

def makeAFriend(array, i, count):
    name = array[i*3]
    age = array[i*3+1]
    birthdate = array[i*3+2]
    f = Friend(name, age, birthdate)
    return f

main()
