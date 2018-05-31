from src import board
import pytest

@pytest.mark.parametrize("expected_size", [3,7,10])
def test_board_is_square_with_correct_dimensions(expected_size):
    # arrange
    sut = board.Board(expected_size)

    # act
    actual = sut.board

    # assert
    assert len(actual) == expected_size ** 2

@pytest.mark.parametrize("expected_mines", [3,7,10])
def test_corrent_number_of_mines_on_creation(expected_mines):
    # arrange
    sut = board.Board(10, expected_mines)

    # act
    actual_mines = sum(map(lambda x: x.mine, sut.board))

    # assert
    assert expected_mines == actual_mines

def test_reveals_square():
    # arrange
    sut = board.Board(3)

    # act
    sut.reveal(1,2) # y, x
    actual = sut.board

    # assert
    assert actual[5].revealed == True
    
def test_flags_square():
    # arrange
    sut = board.Board(3)

    # act
    sut.toggle_flag(1,2) # y, x
    actual = sut.board

    # assert
    assert actual[5].flagged == True

def test_flag_of_square_is_toggled_back():
    # arrange
    sut = board.Board(3)

    # act
    sut.toggle_flag(1, 2)
    sut.board[5].flagged = True
    sut.toggle_flag(1,2)

    # assert
    assert sut.board[5].flagged == False

def test_lost_if_revealed_mine():
    # arrange
    sut = board.Board(3)

    # act
    # reveal all 
    for y in range(3):
        for x in range(3):
            sut.reveal(y, x)

    # assert
    assert sut.lost()

def test_not_won_on_initialize():
    # arrange
    sut = board.Board(3)

    # assert
    assert sut.won() == False