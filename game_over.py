import tkinter as tk

class GameOver():
    def __init__(self, color) -> None:
        self.root = tk.Tk()
        
        label = tk.Label(text=f"{color} wins")
        label.pack()
        
        self.root.mainloop()