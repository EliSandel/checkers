import tkinter as tk

class BoardGui:
    LIGHT_SQUARES_COLOR = "#b1e8b9" 
    DARK_SQUARES_COLOR = "#70a2a3"   
    
    def __init__(self, board_logic):#board_logic
        self.board_logic = board_logic
        self.window = tk.Tk()
        self.window.title("Checkers")
        self.window.config(padx=20, pady=20)
        self.buttons = []
        self.black_piece_image = tk.PhotoImage(file='images/black_piece.png')  # Keep a reference to the image
        self.red_piece_image = tk.PhotoImage(file='images/red_piece.png')
        self.black_king_image = tk.PhotoImage(file="images/black_king.png")
        self.red_king_image = tk.PhotoImage(file="images/red_king.png")
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
            
            #send move to backend
            result = self.board_logic.check_move(source_coor, dest_coor)
            if result == "move_piece":
                self.move_piece(source_coor, dest_coor)
            elif result == "illegal_move":
                self.illegal_move()
            elif result == "jump_piece":
                self.delete_piece(source_coor, dest_coor)
                self.move_piece(source_coor, dest_coor)
            elif result[:24] == "move_piece_and_make_king":
                print(f"got result in gui {result}")
                self.move_piece(source_coor, dest_coor)
                self.make_king(dest_coor, result)
            elif result[:24] == "jump_piece_and_make_king":
                self.delete_piece(source_coor, dest_coor)
                self.move_piece(source_coor, dest_coor)
                self.make_king(dest_coor, result)
            elif result.startswith("game_over"):
                self.delete_piece(source_coor, dest_coor)
                self.move_piece(source_coor, dest_coor)
                # if result.endswith("red"):
                #     winner = "red"
                # elif result.endswith("black"):
                #     winner  = "black"
                self.window.destroy()
                # return winner
                
    def move_piece(self, source_coor, dest_coor):
        source_x = source_coor[0]
        source_y = source_coor[1]
        dest_x = dest_coor[0]
        dest_y = dest_coor[1]
        
        image = self.buttons[source_x][source_y].cget('image')
        self.buttons[source_x][source_y].config(image=self.empty_image)
        self.buttons[dest_x][dest_y].config(image=image, width=74, height=65)
        
        
    def delete_piece(self, source_coor, dest_coor):
        print("delete piece")
        # Calculate the coordinates of the jumped-over piece
        jumped_x = (source_coor[0] + dest_coor[0]) // 2
        jumped_y = (source_coor[1] + dest_coor[1]) // 2
        
        # Set the image of the jumped-over piece to the empty image
        self.buttons[jumped_x][jumped_y].config(image=self.empty_image)
    
    
    def make_king(self, dest_coor, result):
        print("making king in gui")
        print(f"result: {result}")
        if result[-3:] == "red":
            color = "red"
        elif result[-5:] == "black":
            color = "black"
        # self.buttons[dest_coor[0]][dest_coor[1]].config(image=f"{self.{color}_king_image}")
        self.buttons[dest_coor[0]][dest_coor[1]].config(image=getattr(self, f"{color}_king_image"))
    
    
    def illegal_move(self):
        print("illegal move")
    
    
    def game_over(self):
        pass
        
        
        
if __name__ == "__main__":
    board_gui = BoardGui()
    board_gui.window.mainloop()