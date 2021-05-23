from cv2 import imread, imwrite, imshow, waitKey, threshold, THRESH_BINARY
from numpy import ones, ndarray, size, uint8
from random import randint

from Application.Ant import Ant


class LangtonAlgorithm():
    def __init__(self):
        self._image = []
        self._image_reset = []

    def generate_white_image(self, height, width):
        self._image = ones((height, width), uint8) * 255

    def read_image_from_file(self, path):
        self._image = imread(path, 0)
        self._image = threshold(self._image, 128, 255, THRESH_BINARY)[1]

    def generate_random_image(self, height, width, probabilty):
        self._image = ndarray(height * width, uint8)

        for i in range(len(self._image)):
            test = randint(1, 1000)
            self._image[i] = 0 if(test / 1000 < probabilty) else 255

        self._image.resize((height, width))

    def copy_image_to_reset(self):
        self._image_reset = self._image.copy()

    def copy_image_from_reset(self):
        self._image = self._image_reset.copy()

    def show_image(self):
        imshow('Image', self._image)
        waitKey(0)

    def isImageGenarated(self):
        if(len(self._image) != 0):
            return True
        else:
            return False

    def _save_image_to_file(self, image, iter):
        path = f'out/out_{iter}.png'
        imwrite(path, image)

    def run_algorithm(self, num_of_iters, isSave=False, saveIters=1):
        height = size(self._image, 0)
        width = size(self._image, 1)

        stefan = Ant(height, width)

        for i in range(1, num_of_iters + 1):
            if(self._image[stefan.get_position()] == 255):
                stefan.rotate_left()
                self._image = stefan.change_color(self._image)
                stefan.move()
            elif(self._image[stefan.get_position()] == 0):
                stefan.rotate_right()
                self._image = stefan.change_color(self._image)
                stefan.move()

            if(isSave and (i % saveIters == 0 or i in [1, num_of_iters])):
                self._save_image_to_file(self._image, i)
