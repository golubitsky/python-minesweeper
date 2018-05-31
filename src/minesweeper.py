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

        user_input = user_input.determine_operation(retry_reason)
        if constants.retry_user_input in user_input:
            retry_reason = user_input[constants.retry_user_input]
        else:
            retry_reason = None
            getattr(board, user_input['operation'])(
                x=user_input['x'], y=user_input['y'])


if __name__ == "__main__":
    play_game()
