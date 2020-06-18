from graphics import *
win = GraphWin("Line drawer")
message = Text(Point(100,100), "Click on first point")
message.draw(win)
p1 = win.getMouse()
message.setText("Click on second point")
p2 = win.getMouse()
line = Line(p1, p2)
line.draw(win)
message.setText("")