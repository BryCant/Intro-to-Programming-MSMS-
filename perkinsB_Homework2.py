# Bryant Perkins
# Introduction to Computer Programming
# Programming Assignment 2
# Due Date: 1 Nov 2020

import random   # Module imported to generate random integers (https://docs.python.org/3/library/random.html)
import string   # Module imported to check user input

print("Welcome, Mighty Warrior (MW)! \n")
print("Opponent List: \n [0] Zeta, [1] Ewing, [2] Chrackehn")
monsterId = input("Type a number to choose your opponent: ")
monsterAC, monsterHP, monsterName = 0, 0, 0
invalidMonster = True


# function used to make code 'cleaner'
def choose_monster():
    global monsterAC, monsterHP, monsterName, monsterId, invalidMonster     # affect variables outside of function
    is_number = monsterId not in (string.ascii_letters + string.punctuation)    # make sure user input is a number
    if (len(monsterId) < 2) and is_number and (0 <= int(monsterId) <= 2):   # if a single digit number and in range
        if monsterId == '0':
            monsterName = "Zeta"
            monsterAC, monsterHP = 12, 20
        elif monsterId == '1':
            monsterName = "Ewing"
            monsterAC, monsterHP = 19, 50
        elif monsterId == '2':
            monsterName = "Chrackehn"
            monsterAC, monsterHP = 1, 1000
        invalidMonster = False
    else:
        monsterId = input("Please type a number within the range:")


while invalidMonster:
    choose_monster()

roundNum = 1    # counter variable used to keep up with round, to be displayed
while monsterHP > 0:    # will continue to loop until the monster's defeated
    print(f"Round {roundNum}")      # indicates current round
    attackRoll = random.randint(1, 20)  # generates attack value
    damageRoll = random.randint(1, 8)   # generates attack value

    if attackRoll >= monsterAC:     # determines if attack is high enough to apply damage
        monsterHP -= damageRoll     # damage applied
        print(f"{monsterName} hit! -{damageRoll} health")     # Indicates hit
    else:
        print(f"{monsterName} dodged!")        # Indicates attack was too low

    print(f"{monsterName} Health: {monsterHP}, Attack: {attackRoll}, Damage: {damageRoll}")   # Statistics from round
    print("-------------------------------------------")    # Line to separate rounds
    roundNum += 1   # Counter to update round-indicator

print(f"Victory, REEE! {monsterName} defeated in {roundNum} rounds")    # Necessary victory screech showing final stats
