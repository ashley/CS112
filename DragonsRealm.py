#import initial values 
import random
import time

#set initial treasure
treasure = 50
caveNumber = 0

def describeChoose():
    print("You are surrounded by dragons. There is a friendly dragon in one cave and a dangerous one in another. One cave does not have air and the other does not have water. There are four caves total.")
    print("You approach the cave,")
    time.sleep(2)
    print("enter,")
    time.sleep(2)
    print("and...")
    caveNumber= random.randint(1,4)
    return caveNumber

def chooseCave(life,gold):
    while life == True:
      caveNum = describeChoose()
      print("You have " + str(gold) + " gold now.") #depend on different caves
      if (caveNum == 1):
        life,treasure = dangerousCave(gold)
      elif caveNum == 2:
        treasure = friendlyCave(gold)
      elif caveNum == 3:
        life, treasure = waterlessCave(gold)
      else:
        treasure,life = airlessCave(gold)

def dangerousCave (treasure): # need to know how much money they have
    print(" You have entered a dangerous cave.")
    time.sleep(2)
    if treasure<20:
        time.sleep(2)
        print(" The dragon gobbles you down.")
        life=False
    else: #treasure>20
        print("The dragon tells you he will let you go if you give him 20 gold coins")
        time.sleep(2)
        answer=input("Would you like to give the dragon 20 gold coins to save your life?[y/n]")
        if answer=="y":
            treasure-=20
            life=True
        else:
            print("The dragon kills you.")
            life=False

    return (life,treasure)

def friendlyCave(treasure):
    import time
    
    time.sleep(2)
    print("The dragon gives you some treasure! ")
    treasure += 5
    print("You now have " + str(treasure) + " gld coins")
    return(treasure)

def waterlessCave(coins):
    days = random.randrange(1,11)
    cansOfWater = random.randrange(1,11)
    alive = True
    print("You are trapped in a cave!")
    print("There is no way out!")
    print("You will have to wait to be rescued.")
    print("There is a vending machine in the cave.")
    print("It sells cans of water for two gold coins apiece.")
    print("Each can of water is enough to keep you alive for one day.")
    print("You have " + str(coins) + " gold coins.")
    while days > 0 and cansOfWater > 0 and coins >= 2 and alive == True:
        buyWater = input("Do you want to purchase a can of water? Enter 'y' or 'n'. ")
        while buyWater != 'y' and buyWater != 'n':
            print("ERROR: You must enter either 'y' or 'n'.")
            print("       Do not enter the quotation marks, just the lowercase letter.")
            buyWater = input("Do you want to purchase a can of water? Enter 'y' or 'n'. ")
        if buyWater == 'y':
            coins = coins - 2
            cansOfWater = cansOfWater - 1
            print("You bought a can of water.")
            print("You survived another day.")
        if buyWater == 'n':
            print("You can't survive without water.")
            print("You died.")
            alive = False
    if days == 0:
        print("Congratulations! You just got rescued.")
        alive = True
    elif cansOfWater == 0:
        print("There are no more cans of water.")
        print("You can't survive without water.")
        print("You died.")
        alive = False
    elif coins < 2:
        print("You don't have enough money to purchase water.")
        print("You can't survive without water.")
        print("You died.")
        alive = False
    return (alive, coins)

def airlessCave(treasure):
    time1 = random.randrange (30,120)
    elapsed = 0
    print("This cave has no air! You're gonna die!!")
    time.sleep(2)
    while (elapsed < time1):
        if (treasure > 20):
            print("You can buy cans of air for 20 gold!")
            air = input("Will you buy the air? y/n ")
            if (air == "y"):
                treasure = (treasure - 20)
                print("You bought an air can. It will last for 30 minutes.")
                print("You have " + str(treasure) + " gold remaining.")
                time.sleep(2)
                elapsed = elapsed + 30
                if ((time1 - elapsed) > 0):
                    print("You are stuck in this cave for " + str(time1 - elapsed) + "more minutes.")
                    life = False
            else:
                life = False
                elapsed = 200
        else:
            print("Rest in peace.")
            life = False
            elapsed = 200
    if (life == True):
        print("You made it out okay.")
    
    return(treasure,life)
    
def main (gold):
    life = True
    chooseCave(life,gold)
    print("You've died.Thank you for playing!")

main(treasure)
