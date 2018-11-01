import math
import turtle


# draw the circle using turtle
def drawCircleTurtle(x, y, r):

    turtle.shape('turtle')
    # move to the start of circle
    turtle.up() # 告诉python提笔，让笔离开虚拟的纸,这样移动海龟也不会画图。
    turtle.setpos(x, y)
    turtle.down()

    # draw the circle
    for i in range(0, 365, 5):
        # print(i)
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))


drawCircleTurtle(0, 0, 50)
turtle.mainloop()