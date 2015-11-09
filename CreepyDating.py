#Code written by Ashley Chen
"""Program Goal: program that provides guidance on whether a particular
person on whether or not they should date a specific other person of a certain age"""

#Ask the user for their age and the significant other's age
userAge = int(input("Enter your age: "))
loverAge = int(input("Enter your significant other's age: "))

#Determine whether the user is older or younger
if (userAge < loverAge):
    #Calculates the age range the user is allowed to date
    youngest = userAge/2 + 7
    oldest = (userAge - youngest)  * 3 + youngest

    #Determine if the significant other fits into the user's age range
    if (youngest <= loverAge <= oldest):
        print("\n","Go for it! It's socially acceptable!", "\n")
    else:
        print("\n", "Don't even try. It's creepy.", "\n")
elif (userAge > loverAge):
    #Calculates the age range the user is allowed to date
    youngest = loverAge/2 + 7
    oldest = (loverAge - youngest)  * 3 + youngest

    #Determine if the significant other fits into the user's age range
    if (youngest <= userAge <= oldest):
        print("\n", "You're creepy. But...you can still date each other!", "\n")
    else:
        print("\n", "Your lover is creepy.", "\n")

#Ask the user for the significant other's name
loverName = input("Enter your significant other's name: ")

#Decides whether to diss the significant other
if (loverName == "David"):
    print("\n", "Ewwwwwww. WHY")
else:
    print("\n", "You go girl!")

"""
Test A: Input 18, 23. Output creepy
Test B: Input 18, 15. Output creepy
Test C: Input 30, 47. Output creepy
Test D: Input 30, 21. Output creepy
Test E: Input 18, 21. Output good
Test F: Input 18, 17. Output good
Test G: Input 30, 45. Output good
Test H: Input 30, 23. Output good
Test I: Input 18, 22. Output good
Test J: Input 18, 16. Output good
Test K: Input 30, 46. Output good
Test L: Input 30, 22. Output good
Test M: Input 22, 18. Output good
Test N: Input 46, 30. Output good
Test O: Input 23, 18. Output creepy
Test P: Input 47, 30. Output creepy
Test Q: Input 18, 16. Output good
Test R: Input 30, 22. Output good
Test S: Input 18, 15. Output creepy
Test T: Input 30, 21. Output creepy
"""
