from src import board, view, constants
import pytest

def test_new_board_printed_all_empty(capsys):
    # arrange
    board_input = board.Board(2)
    sut = view.View(board_input)
    
    # act
    actual = sut.print()
    
    # assert
    out, err = capsys.readouterr()
    assert out == '  0 1\n0 _ _\n1 _ _\n'

def test_board_with_all_mines_prints_all_mines(capsys):
    # arrange
    board_input = board.Board(2, 4)

    for y in range(2):
        for x in range(2):
            board_input.reveal(y, x)
    
    # act
    sut = view.View(board_input)
    
    actual = sut.print()
    
    # assert
    out, err = capsys.readouterr()
    assert out == '  0 1\n0 x x\n1 x x\n'

def test_board_with_no_mines_prints_all_zeroes(capsys):
    # arrange
    board_input = board.Board(2, 0)

    for y in range(2):
        for x in range(2):
            board_input.reveal(y, x)
    
    # act
    sut = view.View(board_input)
    
    actual = sut.print()
    
    # assert
    out, err = capsys.readouterr()
    assert out == '  0 1\n0 0 0\n1 0 0\n'

def test_board_with_half_mines_prints(capsys):
    # arrange
    board_input = board.Board(2, 2)

    for y in range(2):
        for x in range(2):
            board_input.reveal(y, x)
    
    # act
    sut = view.View(board_input)
    
    expected_chars = []
    for cell in board_input.board:
        if cell.mine:
            expected_chars.append(constants.display_char_mine)
        else:
            expected_chars.append(cell.n_surrounding_mines)
    
    actual = sut.print()
    
    # assert
    out, err = capsys.readouterr()
    a, b, c, d = expected_chars
    assert out == f"  0 1\n0 {a} {b}\n1 {c} {d}\n"

def test_board_with_flag_prints_flag(capsys):
    # arrange
    board_input = board.Board(2, 0)

    board_input.toggle_flag(0, 0)
    
    # act
    sut = view.View(board_input)
    actual = sut.print()
    
    # assert
    out, err = capsys.readouterr()
    assert out == "  0 1\n0 f _\n1 _ _\n"