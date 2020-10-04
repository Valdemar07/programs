import math
import time
import random
import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")

global M
M = 0
global money
money = 0

# Draw the money
money_pen = turtle.Turtle()
money_pen.speed(0)
money_pen.color("white")
money_pen.penup()
money_pen.setposition(-290, 270)
moneystring = "Money: %s" %money
money_pen.write(moneystring, False, align="left", font=("Arial", 14, "normal"))
money_pen.hideturtle()

global L
L = 1
global level
level = 1

# Draw the level
level_pen = turtle.Turtle()
level_pen.speed(0)
level_pen.color("white")
level_pen.penup()
level_pen.setposition(0, 270)
levelstring = "Level: %s" %level
level_pen.write(levelstring, False, align="left", font=("Arial", 14, "normal"))
level_pen.hideturtle()

global MoneyByLevel
MoneyByLevel = 0
global upgradeCost
upgradeCost = 10
global uCost
uCost = 10

# Draw the upgrade cost
upgrade_pen = turtle.Turtle()
upgrade_pen.speed(0)
upgrade_pen.color("white")
upgrade_pen.penup()
upgrade_pen.setposition(0, 250)
upgradestring = "Upgrade costs: %s" %upgradeCost
upgrade_pen.write(upgradestring, False, align="left", font=("Arial", 14, "normal"))
upgrade_pen.hideturtle()

# Draw how to upgrade
ub_pen = turtle.Turtle()
ub_pen.speed(0)
ub_pen.color("white")
ub_pen.penup()
ub_pen.setposition(0, 230)
ubstring = "Click U to upgrade"
ub_pen.write(ubstring, False, align="left", font=("Arial", 14, "normal"))
ub_pen.hideturtle()

# Draw the status
status_pen = turtle.Turtle()
status_pen.speed(0)
status_pen.color("white")
status_pen.penup()
status_pen.setposition(0, 0)
status_pen.hideturtle()


def runUpgrade():
    global upgradeCost
    global level
    global money
    print("Reading")
    if money > upgradeCost:
        money -= upgradeCost
        level += 1
        upgradeCost *= 2
        upgrade_pen.clear()
        upgradestring = "Upgrade costs: %s" % upgradeCost
        upgrade_pen.write(upgradestring, False, align="left", font=("Arial", 14, "normal"))
        level_pen.clear()
        levelstring = "Level: %s" % level
        level_pen.write(levelstring, False, align="left", font=("Arial", 14, "normal"))
        money_pen.clear()
        moneystring = "Money: %s" % money
        money_pen.write(moneystring, False, align="left", font=("Arial", 14, "normal"))
    else:
        print("You need more money")

# Create keybind controls
turtle.listen()
turtle.onkey(runUpgrade, "u")

# The loop that gives you money
while True:
    MoneyByLevel = level * 2
    money += MoneyByLevel
    money_pen.clear()
    moneystring = "Money: %s" % money
    money_pen.write(moneystring, False, align="left", font=("Arial", 14, "normal"))
    time.sleep(1)
    M = money
    money = M
    uCost = upgradeCost
    upgradeCost = uCost
    L = level
    level = L

delay = turtle.done()