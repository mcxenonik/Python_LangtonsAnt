import random


class Ant():
    def __init__(self, board_size_y, board_size_x, direction=0):
        self._board_size_y = board_size_y
        self._board_size_x = board_size_x
        self._position_y = int(board_size_y / 2)
        self._position_x = int(board_size_x / 2)
        self._direction = direction

    def get_position(self):
        y = self._position_y
        x = self._position_x

        return (y, x)

    def change_color(self, board):
        y = self._position_y
        x = self._position_x

        board[y, x] = 255 if(board[y, x] == 0) else 0

        return board

    def move(self):
        max_y = self._board_size_y - 1
        max_x = self._board_size_x - 1
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

        if(self._position_y < 0 or self._position_x < 0
           or self._position_y > max_y
           or self._position_x > max_x):
            self._position_y = old_y
            self._position_x = old_x

            self._random_move()

    def rotate(self, angle):
        self._direction += angle

        if(self._direction < 0):
            self._direction = 270
        elif(self._direction > 270):
            self._direction = 0

    def _random_move(self):
        y = self._position_y
        x = self._position_x
        max_y = self._board_size_y - 1
        max_x = self._board_size_x - 1

        if(y == 0 and x == 0):
            directions = [90, 180]
        elif(y == 0 and x == max_x):
            directions = [180, 270]
        elif(y == max_y and x == 0):
            directions = [0, 90]
        elif(y == max_y and x == max_x):
            directions = [0, 270]
        elif(y == 0):
            directions = [90, 180, 270]
        elif(y == max_y):
            directions = [0, 90, 270]
        elif(x == 0):
            directions = [0, 90, 180]
        elif(x == max_x):
            directions = [0, 180, 270]

        direction = random.choice(directions)

        self._set_direction(direction)
        self.move()

    def _set_direction(self, new_direction):
        self._direction = new_direction
