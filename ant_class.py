class Ant():
    def __init__(self, board_size_y, board_size_x, direction='N'):
        self._board_size_y = board_size_y
        self._board_size_x = board_size_x
        self._position_y = int(board_size_y / 2)
        self._position_x = int(board_size_x / 2)
        self._direction = direction

    def move_right(self):
        if(self._direction == 'N'):
            self._position_x += 1
            self._direction = 'E'
        elif(self._direction == 'E'):
            self._position_y += 1
            self._direction = 'S'
        elif(self._direction == 'S'):
            self._position_x -= 1
            self._direction = 'W'
        elif(self._direction == 'W'):
            self._position_y -= 1
            self._direction = 'N'

    def move_left(self):
        if(self._direction == 'N'):
            self._position_x -= 1
            self._direction = 'W'
        elif(self._direction == 'E'):
            self._position_y -= 1
            self._direction = 'N'
        elif(self._direction == 'S'):
            self._position_x += 1
            self._direction = 'E'
        elif(self._direction == 'W'):
            self._position_y += 1
            self._direction = 'S'

    def get_position(self):
        y = self._position_y
        x = self._position_x
        return (y, x)

    def set_position_x(self, x):
        self._position_x = x

    def set_position_y(self, y):
        self._position_y = y

    def change_color(self, board):
        y = self._position_y
        x = self._position_x

        board[y, x] = 255 if(board[y, x] == 0) else 0

        return board
