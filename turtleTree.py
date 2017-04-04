import turtle
import random

# original
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()




"""

def tree(branchLen,t):
    if branchLen > 5:
        # if branchLen < 20:
        #     t.color(.4, .9, .3)
        t.forward(branchLen)
        # r = random.randint(10,60)
        t.right(20)
        t.width(7)
        # s = random.randint(5,15)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        # t.width(1)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()   # put the pen up
    t.backward(100)
    t.down()  # put the pen down
    t.color(.1, .45, .1)
    t.width(10)
    tree(90,t)
    myWin.exitonclick()

main()
"""