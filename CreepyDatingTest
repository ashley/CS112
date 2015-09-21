#Program Goal: program that provides guidance on whether a particular person on whether or not they should date a specific other person of a certain age

output = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
user = [18,18,30,30,18,18,30,30,18,18,30,30,22,46,23,47,18,30,18,30]
lover = [23,15,47,21,21,17,45,23,22,16,46,22,18,30,18,30,16,22,15,21]


for i in range(0,20):
    #Ask the user for their age and the significant other's age
    userAge = user[i]
    loverAge = lover[i]


    if (userAge < loverAge):
        #Calculates the age range the user is allowed to date
        youngest = userAge/2 + 7
        oldest = (userAge - youngest)  * 3 + youngest

        #Determine if the significant other fits into the user's age range
        if (youngest <= loverAge <= oldest):
            output[i] = "good"
        else:
            output[i] = "creepy"
    else :
        #Calculates the age range the user is allowed to date
        youngest = loverAge/2 + 7
        oldest = (loverAge - youngest)  * 3 + youngest

        #Determine if the significant other fits into the user's age range
        if (youngest <= userAge <= oldest):
            output[i] = "good"
        else:
            output[i] = "creepy"

print(output)

"""Test A: Input 18, 23. Output creepy
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
