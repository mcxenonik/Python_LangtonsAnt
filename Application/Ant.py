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

    def move(self):
        max_y = self._max_position_y
        max_x = self._max_position_x
        old_y = self._position_y
        old_x = self._position_x

        if(self._direction == 0):
            self._position_y -= 1
        elif(self._direction == 90):
            self._position_x += 1
        elif(self._direction == 180):
            self._position_y += 1
        elif(self._direction == 270):
            self._position_x -= 1

        # if(self._position_y < 0 or self._position_x < 0
        #    or self._position_y > max_y or self._position_x > max_x):
        #     self._position_y = old_y
        #     self._position_x = old_x

        #     self._random_move()
        while(self._position_y < 0 or self._position_x < 0
              or self._position_y > max_y or self._position_x > max_x):
            self._position_y = old_y
            self._position_x = old_x

            self._random_move()

    def move_v2(self):
        if(self._direction == 0):
            self._position_y -= 1
        elif(self._direction == 90):
            self._position_x += 1
        elif(self._direction == 180):
            self._position_y += 1
        elif(self._direction == 270):
            self._position_x -= 1

    def rotate_right(self):
        self._direction += 90

        if(self._direction > 270):
            self._direction = 0

    def rotate_left(self):
        self._direction -= 90

        if(self._direction < 0):
            self._direction = 270

    def _random_move(self):
        # y = self._position_y
        # x = self._position_x
        # max_y = self._max_position_y
        # max_x = self._max_position_x

        # if(y == 0 and x == 0):
        #     directions = [90, 180]
        # elif(y == 0 and x == max_x):
        #     directions = [180, 270]
        # elif(y == max_y and x == 0):
        #     directions = [0, 90]
        # elif(y == max_y and x == max_x):
        #     directions = [0, 270]
        # elif(y == 0):
        #     directions = [90, 180, 270]
        # elif(y == max_y):
        #     directions = [0, 90, 270]
        # elif(x == 0):
        #     directions = [0, 90, 180]
        # elif(x == max_x):
        #     directions = [0, 180, 270]
        directions = [0, 90, 180, 270]

        self._direction = choice(directions)
        self.move_v2()
