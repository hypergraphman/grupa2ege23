from turtle import *


def move(a, b):
    global x, y
    x += a
    y += b
    goto(x, y)


cell = 20
speed(0.0001)
y = x = 0

for i in range(15):
    move(10 * cell, 10 * cell)
    move(3 * cell, -6 * cell)
    move(-9 * cell, 3 * cell)

penup()
for x in range(15):
    for y in range(11):
        goto(x * cell, y * cell)
        dot(3, 'red')

done()