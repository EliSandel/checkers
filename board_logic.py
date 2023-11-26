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
        print(source_coor)
        print(dest_coor)
        pass
            
            
if __name__ == "__main__":
    b = BoardLogic()
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in b.board]))
                