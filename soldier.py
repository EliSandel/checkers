class Soldier:
    def __init__(self, color) -> None:
        self.color = color
    
    def is_legal_move(source_coor, dest_coor, color) -> bool:
        if color == "red":
            if source_coor[0] == 7:
                return False
        elif color == "black":
            if source_coor[0] == 0:
                return False