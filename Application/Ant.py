from random import choice

from Application.Const import IMAGE_MAX_VALUE as IMAXVAL
from Application.Const import IMAGE_MIN_VALUE as IMINVAL


class Ant():
    def __init__(self, board_size_y, board_size_x, direction=0):
        self._max_position_y = board_size_y - 1
        self._max_position_x = board_size_x - 1
        self._position_y = int(board_size_y / 2)
        self._position_x = int(board_size_x / 2)
        self._direction = direction

    def get_position(self):
        y = self._position_y
        x = self._position_x

        return (y, x)

    def change_color(self, board):
        position = self.get_position()

        board[position] = IMAXVAL if(board[position] == IMINVAL) else IMINVAL

        return board

    def rotate_right(self):
        self._direction += 90

        if(self._direction > 270):
            self._direction = 0

    def rotate_left(self):
        self._direction -= 90

        if(self._direction < 0):
            self._direction = 270

    def move(self):
        old_y = self._position_y
        old_x = self._position_x

        self.move_v2()

        self._random_move(old_y, old_x)

    def move_v2(self):
        if(self._direction == 0):
            self._position_y -= 1
        elif(self._direction == 90):
            self._position_x += 1
        elif(self._direction == 180):
            self._position_y += 1
        elif(self._direction == 270):
            self._position_x -= 1

    def _random_move(self, old_y, old_x):
        max_y = self._max_position_y
        max_x = self._max_position_x
        directions = [0, 90, 180, 270]

        while(self._position_y < 0 or self._position_x < 0
              or self._position_y > max_y or self._position_x > max_x):
            self._position_y = old_y
            self._position_x = old_x

            self._direction = choice(directions)
            directions.remove(self._direction)
            self.move_v2()
