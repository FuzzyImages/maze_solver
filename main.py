from graphics import Window, Point, Line, Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(50,100,50,100,win)
    cell2 = Cell(100,150,50,100,win)
    cell2.has_top_wall = False
    cell3 = Cell(150,200,50,100,win)
    cell4 = Cell(50,100,100,150,win)
    cell5 = Cell(100,150,100,150,win)
    cell5.has_bottom_wall = False
    cell6 = Cell(150,200,100,150,win)

    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell5.draw()
    cell6.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()