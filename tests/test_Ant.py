from numpy import zeros, ones

from Application.Ant import Ant


def test_create_Ant():                                       ###### Testy niepoprawnych danych, ale bez obsługi w kodzie
    ant1 = Ant(100, 100)

    assert ant1._max_position_y == 99
    assert ant1._max_position_x == 99

    assert ant1._position_y == 50
    assert ant1._position_x == 50

    assert ant1._direction == 0

def test_create_Ant_negative_size():                                       ###### Testy niepoprawnych danych, ale bez obsługi w kodzie
    ant1 = Ant(-5, -5)


def test_create_Ant_with_odd_board_size():
    ant1 = Ant(25, 65)

    assert ant1._max_position_y == 24
    assert ant1._max_position_x == 64

    assert ant1._position_y == 12
    assert ant1._position_x == 32

    assert ant1._direction == 0


def test_creat_Ant_with_direction():
    ant1 = Ant(100, 100, 180)

    assert ant1._direction == 180


def test_get_position():
    ant1 = Ant(100, 100)

    assert ant1.get_position() == (50, 50)


def test_change_color_to_black():
    ant1 = Ant(100, 100)
    board = ones((100, 100)) * 255

    board = ant1.change_color(board)

    assert board[ant1.get_position()] == 0


def test_change_color_to_white():
    board = zeros((100, 100))
    ant1 = Ant(100, 100)

    board = ant1.change_color(board)

    assert board[ant1.get_position()] == 255


def test_move_forward():
    ant1 = Ant(100, 100)

    ant1.move()

    assert ant1.get_position() == (49, 50)


def test_move_backward():
    ant1 = Ant(100, 100, 180)

    ant1.move()

    assert ant1.get_position() == (51, 50)


def test_move_right():
    ant1 = Ant(100, 100, 90)

    ant1.move()

    assert ant1.get_position() == (50, 51)


def test_move_left():
    ant1 = Ant(100, 100, 270)

    ant1.move()

    assert ant1.get_position() == (50, 49)


def test_move_with_random_move_0(monkeypatch):
    def return_direction_0(directions):
        return 0

    monkeypatch.setattr('Application.Ant.choice', return_direction_0)

    ant1 = Ant(100, 100)
    ant1.rotate_right()
    ant1.rotate_right()

    while(ant1.get_position() != (99, 50)):
        ant1.move()

    ant1.move()

    assert ant1.get_position() == (98, 50)


def test_move_with_random_move_180(monkeypatch):
    def return_direction_180(directions):
        return 180

    monkeypatch.setattr('Application.Ant.choice', return_direction_180)

    ant1 = Ant(100, 100)

    while(ant1.get_position() != (0, 50)):
        ant1.move()

    ant1.move()

    assert ant1.get_position() == (1, 50)


def test_rotate_right():
    ant1 = Ant(100, 100, 270)

    ant1.rotate_right()

    assert ant1._direction == 0


def test_rotate_left():
    ant1 = Ant(100, 100, 0)

    ant1.rotate_left()

    assert ant1._direction == 270


def test_random_move():
    pass
