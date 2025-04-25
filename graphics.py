from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create the main window (root widget)
        self.__root = Tk()

        # Set properties on the main window
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width}x{height}")

        # Create canvas widget (This is where things are drawn)
        self.__canvas = Canvas(self.__root, bg="white")

        # Pack canvas (Make it fill the window)
        self.__canvas.pack(fill=BOTH, expand=True)

        # Track if window is running
        self.__is_running = False

        # I guess .protocol is the X button on the window....
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__is_running = True

        while self.__is_running:
            self.redraw()
        
        print("Loop ended, program will exit.")

    def close(self):
        self.__is_running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_1.x, 
            self.point_1.y, 
            self.point_2.x, 
            self.point_2.y, 
            fill=fill_color, 
            width=2
        )

class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1 
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win #the Canvas I'm guessing

    def draw(self):
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall, "black")
        
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall, "black")

        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall, "black")

        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall, "black")

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"

        move_line = Line(
            Point((self._x1 + self._x2)//2, (self._y1 + self._y2)//2),
            Point((to_cell._x1 + to_cell._x2)//2, (to_cell._y1 + to_cell._y2)//2)
        )
        self._win.draw_line(move_line, fill_color)


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

    def _create_cells(self):
        pass

    def _draw_cells(self, i, j):
        pass

    def _animate(self):
        pass
