# snowflake

import turtle

def snowflake(lengthSide, levels):
  if levels == 0:
      t.forward(lengthSide)
      return
  lengthSide /= 3.0
  snowflake(lengthSide, levels-1)
  t.left(60)
  snowflake(lengthSide, levels-1)
  t.right(120)
  snowflake(lengthSide, levels-1)
  t.left(60)
  snowflake(lengthSide, levels-1)


def full_snowflake(lengthside, levels):
  for i in range(3):
    snowflake(lengthside, levels)
    t.right(120)


if __name__ == "__main__":
  t = turtle.Turtle()
  myWin = turtle.Screen()

  t.speed("Fastest")
  length = 300.0
  t.penup()
  t.backward(length / 2.0)
  t.pendown()
  t.color("green")
  full_snowflake(length, 4)
  # mainloop()

  myWin.exitonclick()
