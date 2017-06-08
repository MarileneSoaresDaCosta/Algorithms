import turtle


def drawTriangle(points,color,myTurtle):
  myTurtle.speed(1)
  myTurtle.fillcolor(color)
  myTurtle.up()
  myTurtle.goto(points[0][0],points[0][1])
  myTurtle.down()
  myTurtle.begin_fill()
  myTurtle.goto(points[1][0],points[1][1])
  myTurtle.goto(points[2][0],points[2][1])
  myTurtle.goto(points[0][0],points[0][1])
  myTurtle.end_fill()

def drawCircle(points, color, myTurtle):
  myTurtle.speed(1)
  myTurtle.fillcolor(color)
  myTurtle.up()
  myTurtle.goto(points[1][0],points[1][1])
  myTurtle.down()
  myTurtle.begin_fill()
  myTurtle.circle(50)
  myTurtle.end_fill()


def drawSquare(points, color, myTurtle):
  myTurtle.speed(1)
  myTurtle.fillcolor(color)
  myTurtle.up()
  myTurtle.goto(points[0][0],points[0][1])
  myTurtle.down()
  myTurtle.begin_fill()
  myTurtle.goto(points[1][0],points[1][1])
  myTurtle.goto(points[2][0],points[2][1])
  myTurtle.goto(points[3][0],points[3][1])
  myTurtle.goto(points[0][0],points[0][1])
  myTurtle.end_fill()


myTurtle = turtle.Turtle()
myWin = turtle.Screen()
myPoints = [[-100,-50],[0,100],[100,-50]]
sqPoints = [[-50,-50],[-50,50],[50,50],[50,-50]]
drawTriangle(myPoints,'green',myTurtle)
drawCircle(myPoints, 'red', myTurtle)
drawSquare(sqPoints, 'yellow', myTurtle)
myWin.exitonclick()