import tkinter as tk

class BoardGui:
    LIGHT_SQUARES_COLOR = "#b1e8b9"  # Hexadecimal color code for (177, 228, 185)
    DARK_SQUARES_COLOR = "#70a2a3"   # Hexadecimal color code for (112, 162, 163)
    
    def __init__(self, board_logic):#board_logic
        self.board_logic = board_logic
        self.window = tk.Tk()
        self.window.title("Checkers")
        self.window.config(padx=20, pady=20)
        self.buttons = []
        self.black_piece_image = tk.PhotoImage(file='images/black_piece.png')  # Keep a reference to the image
        self.red_piece_image = tk.PhotoImage(file='images/red_piece.png')
        self.empty_image = tk.PhotoImage()
        self.source_coor = None
        self.dest_coor = None
        self.gui_setup()
        
        
    def gui_setup(self):
        board_frame = tk.Frame(master=self.window, height=600, width=600)
        
        #setting up the buttons
        for i in range(8):
            row = []
            for j in range(8):
                button = tk.Button(
                    master=board_frame, 
                    command= lambda i=i, j=j: self.click((i,j)),
                    width=74,
                    height=65,
                    image=self.empty_image
                )
                if i % 2 ==0:
                    if j % 2 ==0:
                        button.config(bg=self.LIGHT_SQUARES_COLOR, state="disabled")
                    else:
                        button.config(bg=self.DARK_SQUARES_COLOR)
                        if i == 0 or i == 2:
                            button.config(image=self.black_piece_image, width=74, height=65)
                        if i == 6:
                            button.config(image=self.red_piece_image, width=74, height=65)
                else:
                    if j % 2 == 0:
                        button.config(bg=self.DARK_SQUARES_COLOR)
                        if i == 1:
                            button.config(image=self.black_piece_image, width=74, height=65)
                        elif i == 5 or i == 7:
                            button.config(image=self.red_piece_image, width=74, height=65)

                    else:
                        button.config(bg=self.LIGHT_SQUARES_COLOR, state="disabled")
                row.append(button)
                button.grid(row=i, column=j)
            
            self.buttons.append(row)
        
        board_frame.grid(row=0, column=0)
        
    def click(self, coor):
        if self.source_coor == None:
            if self.buttons[coor[0]][coor[1]].cget('image') == str(self.empty_image):
                return
            else:
                self.source_coor = coor
        else:
            self.dest_coor = coor
            source_coor = self.source_coor
            dest_coor = self.dest_coor
            self.source_coor = None
            self.dest_coor = None
            result = self.board_logic.check_move(source_coor, dest_coor)
            if result == "move_piece":
                self.move_piece(source_coor, dest_coor)
            elif result == "illegal_move":
                self.illegal_move()
            
    
    def move_piece(self, source_coor, dest_coor):
        source_x = source_coor[0]
        source_y = source_coor[1]
        dest_x = dest_coor[0]
        dest_y = dest_coor[1]
        
        image = self.buttons[source_x][source_y].cget('image')
        self.buttons[source_x][source_y].config(image=self.empty_image)
        self.buttons[dest_x][dest_y].config(image=image, width=74, height=65)
        
        
    
    def make_king(self):
        pass
    
    def remove_piece(self):
        pass
    
    def illegal_move(self):
        print("illegal move")
    
    def game_over(self):
        pass
        
        
        
if __name__ == "__main__":
    board_gui = BoardGui()
    board_gui.window.mainloop()