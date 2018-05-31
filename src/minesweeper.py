import os, sys
d = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(d)
from src.board import Board
from src.view import View
from src import user_input, constants


def play_game():
    board = Board(10, 40)
    retry_reason = None
    while True:
        view = View(board)
        view.print()
        if board.won() or board.lost():
            sys.exit()
            
        u_input = user_input.determine_operation(retry_reason)
        if constants.retry_user_input in u_input:
            retry_reason = user_input[constants.retry_user_input]
        else:
            retry_reason = None
            getattr(board, u_input['operation'])(
                x=u_input['x'], y=u_input['y'])


if __name__ == "__main__":
    play_game()
