import board_gui
import board_logic
import game_over



if __name__ == "__main__":
    board_logic = board_logic.BoardLogic()
    board_gui = board_gui.BoardGui(board_logic)
    board_gui.window.mainloop()
    winner = board_logic.winner
    print(f"main winner:  {winner}")
    game_over.GameOver(winner)
