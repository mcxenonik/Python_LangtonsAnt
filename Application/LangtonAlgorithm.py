from cv2 import imread, threshold, THRESH_BINARY
from numpy import ones, size, uint8
from numpy.random import binomial, seed

from Application.Const import COLOR_IMAGE_THRESHOLD_VALUE as CITVAL
from Application.Const import IMAGE_MAX_VALUE as IMAXVAL
from Application.Const import IMAGE_MIN_VALUE as IMINVAL
from Application.Ant import Ant


class LangtonAlgorithm():
    def __init__(self):
        self._image = []
        self._image_reset = []
        self._ant = None

    def get_image(self):
        return self._image

    def generate_white_image(self, height, width):
        self._image = ones((height, width), uint8) * IMAXVAL

    def read_image_from_file(self, path):
        self._image = imread(path, 0)
        self._image = threshold(self._image, CITVAL, IMAXVAL, THRESH_BINARY)[1]

    def generate_random_image(self, height, width, probabilty, _seed=None):
        seed(_seed)

        self._image = binomial(1, 1 - probabilty,
                               (height, width)).astype(uint8) * IMAXVAL

    def copy_image_to_reset(self):
        self._image_reset = self._image.copy()

    def copy_image_from_reset(self):
        self._image = self._image_reset.copy()

    def is_image_genarated(self):
        if(len(self._image) != 0):
            return True
        else:
            return False

    def create_ant(self):
        height = size(self._image, 0)
        width = size(self._image, 1)

        self._ant = Ant(height, width)

    def step_algorithm(self):
        if(self._image[self._ant.get_position()] == IMAXVAL):
            self._ant.rotate_left()
            self._image = self._ant.change_color(self._image)
            self._ant.move()
        elif(self._image[self._ant.get_position()] == IMINVAL):
            self._ant.rotate_right()
            self._image = self._ant.change_color(self._image)
            self._ant.move()

        return self._image
