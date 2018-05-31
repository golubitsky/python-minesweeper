import os, sys
d = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(d)
from src.board import Board
from src.view import View
from src import user_input

def play_game():
    board = Board(10)
    view = View(board)
    retry_reason = None
    while True:
        view.print()
        result = user_input.determine_operation(retry_reason)
        if 'retry_user_input' in result:
            retry_reason = result['retry_user_input']
        else:
            retry_reason = None

if __name__ == "__main__":
    play_game()

