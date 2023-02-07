from turtle import *
side = 10
for i in range(side):
    pencolor("red")
    fd(100)
    lt(360/side)
    pencolor("blue")
    dot(30)
mainloop()
