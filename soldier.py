class Soldier:
    def __init__(self, color) -> None:
        self.color = color
    
    def is_legal_move(self, source_coor, dest_coor) -> bool:#checks if theoretticaly the move is legal. all board based checks are in board_logic
        print("checking is legal move in soldier")
        if self.color == "red":
            if source_coor[0] > dest_coor[0]:#going up
                if source_coor[0] - dest_coor[0] == 1:#if its a regular move
                    if abs(source_coor[1] - dest_coor[1]) == 1:
                        return True
                elif source_coor[0] - dest_coor[0] == 2:#if its a jump
                    if abs(source_coor[1] - dest_coor[1]) == 2:
                        return True
        elif self.color == "black":
            if source_coor[0] < dest_coor[0]:#going down
                if source_coor[0] - dest_coor[0] == -1:#if its a regular move
                    if abs(source_coor[1] - dest_coor[1]) == 1:
                        return True
                elif source_coor[0] - dest_coor[0] == -2:#if its a jump
                    if abs(source_coor[1] - dest_coor[1]) == 2:
                        return True
        return False
    