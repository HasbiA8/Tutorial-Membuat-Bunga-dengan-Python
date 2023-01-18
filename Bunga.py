import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('#696969')
t.pencolor('#FF0000')
t.speed(100)
col = ('#4169E1', '#ffd23f', '#3bceac', '#FFC0CB')

for n in range(5):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()