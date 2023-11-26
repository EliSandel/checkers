import tkinter as tk

class BoardGui:
    LIGHT_SQUARES_COLOR = "#b1e8b9"  # Hexadecimal color code for (177, 228, 185)
    DARK_SQUARES_COLOR = "#70a2a3"   # Hexadecimal color code for (112, 162, 163)
    
    def __init__(self):#board_logic
        # self.board_logic = board_logic
        self.window = tk.Tk()
        self.window.title("Checkers")
        self.window.config(padx=20, pady=20)
        self.buttons = []
        self.gui_setup()
        
        
    def gui_setup(self):
        board_frame = tk.Frame(master=self.window, height=600, width=600)
        
        #setting up the buttons
        for i in range(8):
            row = []
            for j in range(8):
                button = tk.Button(
                    master=board_frame, 
                    text=f"{i}: {j}", 
                    command= lambda i=i, j=j: self.move_piece((i,j)) 
                )
                if i % 2 ==0:
                    if j % 2 ==0:
                        button.config(bg=self.LIGHT_SQUARES_COLOR)
                    else:
                        button.config(bg=self.DARK_SQUARES_COLOR)
                else:
                    if j % 2 == 0:
                        button.config(bg=self.DARK_SQUARES_COLOR)
                    else:
                        button.config(bg=self.LIGHT_SQUARES_COLOR)
                row.append(button)
                button.grid(row=i, column=j)
            
            self.buttons.append(row)
        
        board_frame.grid(row=0, column=0)
        
    def move_piece(self, coor):
        print(coor)
    
    def make_king(self):
        pass
    
    def remove_piece(self):
        pass
        
        
        
if __name__ == "__main__":
    board_gui = BoardGui()
    board_gui.window.mainloop()