class Ant():
    def __init__(self, position, direction='N'):
        self._position = position
        self._direction = direction

    def move_right(self):
        if(self._direction == 'N'):
            self._position[1] += 1
            self._direction = 'E'
        elif(self._direction == 'E'):
            self._position[0] += 1
            self._direction = 'S'
        elif(self._direction == 'S'):
            self._position[1] -= 1
            self._direction = 'W'
        elif(self._direction == 'W'):
            self._position[0] -= 1
            self._direction = 'N'

    def move_left(self):
        if(self._direction == 'N'):
            self._position[1] -= 1
            self._direction = 'W'
        elif(self._direction == 'E'):
            self._position[0] -= 1
            self._direction = 'N'
        elif(self._direction == 'S'):
            self._position[1] += 1
            self._direction = 'E'
        elif(self._direction == 'W'):
            self._position[0] += 1
            self._direction = 'S'

    def get_position(self):
        return tuple(self._position)

    def change_color(self, board):
        y = self._position[0]
        x = self._position[1]

        board[y, x] = 255 if(board[y, x] == 0) else 0

        return board
