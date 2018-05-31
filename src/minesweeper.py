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
        result = user_input.determine_operation(retry_reason)
        if constants.retry_user_input in result:
            retry_reason = result[constants.retry_user_input]
        else:
            retry_reason = None
            getattr(board, result['operation'])(x=result['x'],y=result['y'])


if __name__ == "__main__":
    play_game()
