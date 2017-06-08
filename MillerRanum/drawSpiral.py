# 4.7 Visualizing Recursion using Turtle
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
# myTurtle.setpos(-100, -200)


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        myTurtle.left(45)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()

# # print myTurtle.position()
# myTurtle.forward(65)
# print myTurtle.position()
# myWin.exitonclick()


# t = turtle.Turtle()

# t.left(90)
# # t.up()
# t.backward(100)
# t.down()
# t.width(10)
# # t.color("green")
# drawSpiral(t,100)
# myWin.exitonclick()










