import turtle
from turtle import left, right, forward



def hilbert(size, angle, t):
  right(angle)

  right(-angle)
  forward(size)
  left(-angle)
  forward(size)
  left(-angle)
  forward(size)
  right(-angle)

  forward(size)
  left(angle)

  forward(size)
  # right(angle)
  forward(size)
  left(angle)
  forward(size)
  left(angle)
  forward(size)
  right(angle)
  if size > 10:
    hilbert(size - 10, angle, t)


def main():
  t = turtle.Turtle()
  myWin = turtle.Screen()
  size = 50
  angle = 90
  # t.down()
  t.color("Blue")
  t.speed("Slowest")
  hilbert(size, angle, t)
  myWin.exitonclick()

main()


"""
right(angle)

# 1st hilbert call
right(-angle)
forward(size)
left(-angle)
forward(size)
left(-angle)
forward(size)
right(-angle)

# Continue from first call of hilbert
forward(size)
left(angle)

# 2nd hilbert call
right(angle)
forward(size)
left(angle)
forward(size)
left(angle)
forward(size)
right(angle)

# Continue from second call of hilbert
forward(size)

# 3rd hilbert call
right(angle)
forward(size)
left(angle)
forward(size)
left(angle)
forward(size)
right(angle)

# Continue from third call of hilbert
left(angle)
forward(size)

# 4th call of hilbert
right(-angle)
forward(size)
left(-angle)
forward(size)
left(-angle)
forward(size)
right(-angle)

# Continue from fourth call of hilbert
right(angle)"""