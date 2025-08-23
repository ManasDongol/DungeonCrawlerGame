import tkinter as tk

class display:
    ROWS = -1
    COLS = -1
    CELL_SIZE = -1
    def __init__(self,ROWS,COLS,CELL_SIZE):
        self.ROWS = ROWS
        self.COLS = COLS
        self.CELL_SIZE = CELL_SIZE

    def createworld(self):
        root = tk.Tk()
        root.title("Dungeon Crawler Grid")
        # Create Canvas
        canvas = tk.Canvas(root, width=self.COLS * self.CELL_SIZE, height=self.ROWS * self.CELL_SIZE, bg="black")
        canvas.pack()
        player = canvas.create_rectangle(
            0, 0, self.CELL_SIZE, self.CELL_SIZE, fill="blue"
        )

        for row in range(self.ROWS):
            for col in range(self.COLS):
                x1 = col * self.CELL_SIZE
                y1 = row * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE
                canvas.create_rectangle(x1, y1, x2, y2, outline="gray")
        root.mainloop()




