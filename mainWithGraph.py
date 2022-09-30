# price fluctuation
import random
import time
import matplotlib.pyplot as plt


def nextStep(price, method):
    # gets a two decimal point float to add or subtract
    newAmount = round(random.uniform(0, 2.1), 2)

    # adds or subtracts amount dependent on method
    if method == "add":
        price += newAmount
    elif method == "subtract":
        price -= newAmount

    return price


def fluctuate(price, dir):
    # uses decided direction to decide method
    dir = decideDirection(dir)
    if dir == True:
        method = "add"
    else:
        method = "subtract"

    # adds or subtracts a random value
    price = nextStep(price, method)

    return price, dir


def decideDirection(dir):
    # uses a RNG to create a 1/4 chance of the direction switching
    randNum = random.randint(0, 4)

    if randNum == 3:
        if dir == True:
            dir = False
        else:
            dir = True

    return dir


# initial values
value = 50
progression = 0
directionUp = True

# setting matplotlib up

x = [progression]
y = [value]

plt.ion()

figure, axis = plt.subplots(figsize=(10, 8))
line1, = axis.plot(x, y)

# setting labels

plt.title("Price Fluctuation", fontsize=20)
plt.xlabel("Time Progression")
plt.ylabel("Price")

# while value and print statement to keep the 'simulation' going
while True:
    value, directionUp = fluctuate(value, directionUp)
    progression += 0.2
    x.append(progression)
    y.append(value)

    # refreshing graph
    line1.set_xdata(x)
    line1.set_ydata(y)

    plt.xlim([0, progression + 5])
    plt.ylim([0, max(y) + 5])

    figure.canvas.draw()
    figure.canvas.flush_events()

    time.sleep(0.1)