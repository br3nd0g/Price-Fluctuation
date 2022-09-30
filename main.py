# price fluctuation
import random
import time

def nextStep(price, method):
    #gets a two decimal point float to add or subtract
    newAmount = round(random.uniform(0, 2.1), 2)

    #adds or subtracts amount dependent on method
    if method == "add":
        price += newAmount
    elif method == "subtract":
        price -= newAmount

    return price


def fluctuate(price, dir):

    #uses decided direction to decide method
    dir = decideDirection(dir)
    if dir == True: method = "add"
    else: method = "subtract"

    #adds or subtracts a random value
    price = nextStep(price, method)

    return price, dir


def decideDirection(dir):
    #uses a RNG to create a 1/4 chance of the direction switching
    randNum = random.randint(0,4)

    if randNum == 3:
        if dir == True: dir = False
        else: dir = True

    return dir


#initial values
value = 50
progression = 0
directionUp = True

#while value and print statement to keep the 'simulation' going
while True:
    value, directionUp = fluctuate(value, directionUp)
    print(value)
    time.sleep(1)