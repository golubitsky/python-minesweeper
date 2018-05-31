from src import board, view, constants
import re


def test_new_board_printed_all_empty(capsys):
    # arrange
    board_input = board.Board(2)
    sut = view.View(board_input)

    # act
    sut.print()
    out, err = capsys.readouterr()

    # assert
    actual = re.findall('_', out)
    assert len(actual) == 4


def test_board_with_all_mines_prints_all_mines(capsys):
    # arrange
    board_input = board.Board(2, 4)

    for y in range(2):
        for x in range(2):
            board_input.reveal(y, x)

    sut = view.View(board_input)

    # act
    sut.print()
    out, err = capsys.readouterr()

    # assert
    actual = re.findall('x', out)
    assert len(actual) == 4


def test_board_with_no_mines_prints_all_zeroes(capsys):
    # arrange
    board_input = board.Board(2, 0)

    for y in range(2):
        for x in range(2):
            board_input.reveal(y, x)

    sut = view.View(board_input)

    # act
    sut.print()
    out, err = capsys.readouterr()

    # assert
    two_zeroes_in_labels = 2
    actual = re.findall('0', out)
    assert len(actual) - two_zeroes_in_labels == 4


def test_board_with_half_mines_prints(capsys):
    # arrange
    board_input = board.Board(2, 2)

    for y in range(2):
        for x in range(2):
            board_input.reveal(y, x)

    sut = view.View(board_input)

    # act
    sut.print()
    out, err = capsys.readouterr()

    # assert
    expected_chars = []
    for cell in board_input.board:
        if cell.mine:
            expected_chars.append(constants.display_char_mine)
        else:
            expected_chars.append(cell.n_surrounding_mines)

    a, b, c, d = expected_chars

    actual = re.findall(f'{a}|{b}|{c}|{d}', out)
    # this test is slightly imprecise
    assert len(actual) >= 4


def test_board_with_flag_prints_flag(capsys):
    # arrange
    board_input = board.Board(2, 0)
    board_input.toggle_flag(0, 0)
    sut = view.View(board_input)

    # act
    sut.print()
    out, err = capsys.readouterr()

    # assert
    actual = re.findall('f', out)
    assert len(actual) == 1