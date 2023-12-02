import soldier
class BoardLogic:
    def __init__(self) -> None:
        self.board = []
        self.turn = "red"
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
        
        #check if the first button pressed is the current players
        if self.board[source_x][source_y].color != self.turn:
            return "illegal_move"
        
        #check if the destination square is taken or if source squar is empty so its illegal move
        if self.board[dest_x][dest_y] != None or self.board[source_x][source_y] == None:
            return "illegal_move"
        if self.board[source_x][source_y].is_legal_move(source_coor, dest_coor):
            if abs(source_x - dest_x) == 1:
            #basic moveing the piece
                self.change_turn()
                return self.move_piece(source_coor, dest_coor)
            #jump move
            if abs(source_x - dest_x) == 2:
                self.change_turn()
                return self.jump_piece(source_coor, dest_coor)
        return "illegal_move"
    
    def move_piece(self, source_coor, dest_coor):
        print("moving piece")
        self.board[dest_coor[0]][dest_coor[1]] = self.board[source_coor[0]][source_coor[1]]
        self.board[source_coor[0]][source_coor[1]] = None
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
        return "move_piece"
    
    
    def jump_piece(self, source_coor, dest_coor):
        if self.board[(source_coor[0] + dest_coor[0])//2][(source_coor[1] + dest_coor[1])//2] != None:#checks that there is something in the middle piece
            if self.board[(source_coor[0] + dest_coor[0])//2][(source_coor[1] + dest_coor[1])//2].color != self.board[source_coor[0]][source_coor[1]].color:
                self.board[dest_coor[0]][dest_coor[1]] = self.board[source_coor[0]][source_coor[1]]
                self.board[(source_coor[0]+dest_coor[0])//2][(source_coor[1]+dest_coor[1])//2] = None
                self.board[source_coor[0]][source_coor[1]] = None#removes the piece
                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
                return "jump_piece"
    
    def make_king(self, coor):
        pass
    
    def change_turn(self):
        if self.turn == "red":
            self.turn = "black"
        elif self.turn == "black":
            self.turn = "red"
    
    def check_for_second_move():
        pass
            
            
if __name__ == "__main__":
    b = BoardLogic()
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in b.board]))
                