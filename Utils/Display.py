import tkinter as tk

# Grid size
ROWS = 12
COLS = 12
CELL_SIZE = 40

# Create main window
root = tk.Tk()
root.title("Dungeon Crawler Grid")

# Create Canvas
canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="black")
canvas.pack()
player = canvas.create_rectangle(
    0, 0, CELL_SIZE, CELL_SIZE, fill="blue"
)


# Draw the grid
for row in range(ROWS):
    for col in range(COLS):
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

root.mainloop()
