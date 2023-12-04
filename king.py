class King:
    def __init__(self, color) -> None:
        self.color = color
    
    def is_legal_move(self, source_coor, dest_coor) -> bool:
        print("checking legal move in king")
        #one square move
        if abs(source_coor[1] - dest_coor[1]) == 1:
            if abs(source_coor[0] - dest_coor[0]) == 1:
                return True
        #two square jump move
        elif abs(source_coor[1] - dest_coor[1]) == 2:
            if abs(source_coor[0] - dest_coor[0]) == 2:
                return True
        return False