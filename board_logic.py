import soldier
class BoardLogic:
    def __init__(self) -> None:
        self.board = []
        self.initialize_board()
    
    def initialize_board(self):
        for i in range(8):
            row = []
            for j in range(8):
                piece = None
                if i % 2 ==0:
                    if j % 2 ==0:
                        pass
                    else:
                        if i == 0 or i == 2:
                            piece = soldier.Soldier("black")
                        if i == 6:
                            piece = soldier.Soldier("red")
                else:
                    if j % 2 == 0:
                        if i == 1:
                            piece = soldier.Soldier("black")
                        elif i == 5 or i == 7:
                            piece = soldier.Soldier("red")
                    else:
                        pass
                row.append(piece)
            self.board.append(row)
    
    def check_move(self, source_coor, dest_coor):
        print("checking move")

        source_x = source_coor[0]
        source_y = source_coor[1]
        dest_x = dest_coor[0]
        dest_y = dest_coor[1]
        
        #check if the destination square is taken or if source squar is empty so its illegal move
        if self.board[dest_x][dest_y] != None or self.board[source_x][source_y] == None:
            return "illegal_move"
        if self.board[source_x][source_y].is_legal_move(source_coor, dest_coor):
            self.board[dest_x][dest_y] = self.board[source_x][source_y]
            self.board[source_x][source_y] = None
            # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
            return "move_piece"
        else:
            return "illegal_move"
        
        #check if its a one square move forward with empty space
        # return "move_piece"
            
            
if __name__ == "__main__":
    b = BoardLogic()
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in b.board]))
                