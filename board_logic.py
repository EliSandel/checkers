import soldier
import king


class BoardLogic:
    def __init__(self) -> None:
        self.board = []
        self.turn = "red"
        self.is_there_another_move = False
        self.current_possible_moves = []
        self.red_players_eaten = 0
        self.black_players_eaten = 0
        self.initialize_board()
    
    #setting up the list of buttons
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
    
    #called from gui when the player clicks buttons
    def check_move(self, source_coor, dest_coor):
        print("checking move in board_logic")

        source_x = source_coor[0]
        source_y = source_coor[1]
        dest_x = dest_coor[0]
        dest_y = dest_coor[1]
        
        #check if in case of a double move that the move is a chain jump
        if self.is_there_another_move:
            flag = False
            for move in self.current_possible_moves:
                if move[0] == dest_x and move[1] == dest_y:
                    flag = True
            if not flag:
                print("illegal chain move")
                return "illegal_move"
            else:
                self.is_there_another_move = False
                self.current_possible_moves = []
                self.change_turn()
                return self.jump_piece(source_coor, dest_coor)
        
        #check if the first button pressed is the current players
        if self.board[source_x][source_y].color != self.turn:
            print("in board_logic wrong players move")
            return "illegal_move"
        
        #check if the destination square is taken or if source squar is empty so its illegal move
        if self.board[dest_x][dest_y] != None or self.board[source_x][source_y] == None:
            return "illegal_move"
        if self.board[source_x][source_y].is_legal_move(source_coor, dest_coor):
            print("legal move in if")
            if abs(source_x - dest_x) == 1:
            #basic moveing the piece
                self.change_turn()
                return self.move_piece(source_coor, dest_coor)
            #jump move
            if abs(source_x - dest_x) == 2:
                self.change_turn()
                return self.jump_piece(source_coor, dest_coor)
        print("no other options")
        return "illegal_move"
    
    def move_piece(self, source_coor, dest_coor):
        print(f"moving {type(self.board[source_coor[0]][source_coor[1]])} piece from {source_coor} to {dest_coor}")
        self.board[dest_coor[0]][dest_coor[1]] = self.board[source_coor[0]][source_coor[1]]
        self.board[source_coor[0]][source_coor[1]] = None
        #check to see if piece reached the edge and is a soldier and then make king
        if dest_coor[0] == 0 or dest_coor[0] == 7:
            if isinstance(self.board[dest_coor[0]][dest_coor[1]], soldier.Soldier):
                color = self.make_king(dest_coor)
                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
                return f"move_piece_and_make_king_{color}"
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
        return "move_piece"
    
    
    def jump_piece(self, source_coor, dest_coor):
        if self.board[(source_coor[0] + dest_coor[0])//2][(source_coor[1] + dest_coor[1])//2] != None:#checks that there is something in the middle piece
            if self.board[(source_coor[0] + dest_coor[0])//2][(source_coor[1] + dest_coor[1])//2].color != self.board[source_coor[0]][source_coor[1]].color:
                #increment eaten pieces color
                current_color = self.board[source_coor[0]][source_coor[1]].color
                eaten_color = self.board[(source_coor[0] + dest_coor[0])//2][(source_coor[1] + dest_coor[1])//2].color
                current_value = getattr(self, f"{eaten_color}_players_eaten")
                setattr(self, f"{eaten_color}_players_eaten", current_value + 1)
                
                self.board[dest_coor[0]][dest_coor[1]] = self.board[source_coor[0]][source_coor[1]]
                self.board[(source_coor[0]+dest_coor[0])//2][(source_coor[1]+dest_coor[1])//2] = None
                self.board[source_coor[0]][source_coor[1]] = None#removes the piece
                
                #check for game over
                if current_value + 1 == 12:
                    print(f"game over {current_color} wins:     {eaten_color} loses")
                    return f"game_over_{current_color}"
                
                #check to see if piece reached the edge and is a soldier and then make king
                if dest_coor[0] == 0 or dest_coor[0] == 7:
                    if isinstance(self.board[dest_coor[0]][dest_coor[1]], soldier.Soldier):
                        color = self.make_king(dest_coor)
                        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
                        return f"jump_piece_and_make_king_{color}"
                print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
                answer, answer_text, possible_moves = self.check_for_second_move(dest_coor)
                if answer:
                    self.change_turn()
                    self.current_possible_moves = possible_moves
                    self.is_there_another_move = True
                return "jump_piece"
    
    
    def make_king(self, coor):
        print("make king")
        color = self.board[coor[0]][coor[1]].color
        self.board[coor[0]][coor[1]] = king.King(f"{color}")
        return color
        
    
    def change_turn(self):
        if self.turn == "red":
            self.turn = "black"
        elif self.turn == "black":
            self.turn = "red"
    
    
    def check_for_second_move(self, coor) -> (bool, str):
        button = self.board[coor[0]][coor[1]]
        possible_moves = []
        reply = False
        #up right
        try:
            if self.board[coor[0] - 2][coor[1] + 2] == None:#check if two squares ahead is empty
                if self.board[coor[0] -1][coor[1] + 1].color != button.color:#check if the next square is the other players
                    reply = True
                    possible_moves.append((coor[0] - 2, coor[1] + 2))
                    # return (True, "hello", (coor[0] -1, coor[1] + 1))
        except:
            pass
        
        #up left
        try:
            if self.board[coor[0] - 2][coor[1] - 2] == None:#check if two squares ahead is empty
                if self.board[coor[0] -1][coor[1] - 1].color != button.color:#check if the next square is the other players
                    # return (True, "hello", (coor[0] -1, coor[1] - 1))
                    reply = True
                    possible_moves.append((coor[0] - 2, coor[1] - 2))
        except:
            pass
        
        #down right
        try:
            if self.board[coor[0] + 2][coor[1] + 2] == None:#check if two squares ahead is empty
                if self.board[coor[0] + 1][coor[1] + 1].color != button.color:#check if the next square is the other players
                    # return (True, "hello", (coor[0] + 1, coor[1] + 1))
                    reply = True
                    possible_moves.append((coor[0] + 2, coor[1] + 2))
        except:
            pass
        
        #down left
        try:
            if self.board[coor[0] + 2][coor[1] - 2] == None:#check if two squares ahead is empty
                if self.board[coor[0] + 1][coor[1] - 1].color != button.color:#check if the next square is the other players
                    # return (True, "hello", (coor[0] +1, coor[1] -1))
                    reply = True
                    possible_moves.append((coor[0] + 2, coor[1] - 2))
        except:
            pass
        
        return reply, "hello", possible_moves
        
        
            
            
if __name__ == "__main__":
    b = BoardLogic()
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in b.board]))
                