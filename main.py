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

    def wait_for_close(self):
        self.__is_running = True

        while self.__is_running:
            self.redraw()
        
        print("Loop ended, program will exit.")

    def close(self):
        self.__is_running = False


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()