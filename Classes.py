class Friend:
    def __init__(self, n, p, a):
        self.name = n
        self.phone = p
        self.age = a
        
    def __str__(self):
        return(" Name:" + self.name + " Phone: " + self.phone + " Age: " + str(self.age))

def main():
    name = input("Name: ")
    phone = input("Phone: ")
    age = int(input("Age: "))

    friend1 = Friend(name,phone,age)

    print(friend1)
    
main()
