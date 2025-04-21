from graphics import Window, Point, Line

def main():
    win = Window(800, 600)

    cords = 200
    size = 100

    ### Square ###
    p1 = Point(cords, cords) #upper left
    p2 = Point(cords+size, cords) #upper right
    p3 = Point(cords, cords+size) #lower left
    p4 = Point(cords+size, cords+size) #lower right

    line1 = Line(p1, p2) #top edge
    line2 = Line(p1, p3) #left edge
    line3 = Line(p3, p4) #bottom edge
    line4 = Line(p2, p4) #right Edge

    win.draw_line(line1, "red")
    win.draw_line(line2, "red")
    win.draw_line(line3, "red")
    win.draw_line(line4, "red")

    win.wait_for_close()


if __name__ == "__main__":
    main()