from Ant import Ant
import cv2
import numpy
import random


class LangtonAlgorithm():
    def __init__(self):
        self._image = []
        self._image_reset = []

    def generate_white_image(self, height, width):
        self._image = numpy.ones((height, width)) * 255

    def read_image_from_file(self, path):
        self._image = cv2.imread(path, 0)
        self._image = cv2.threshold(self._image, 128, 255, cv2.THRESH_BINARY)[1]

    def generate_random_image(self, height, width, probabilty):
        self._image = numpy.ndarray(height * width)

        for i in range(len(self._image)):
            test = random.randint(1, 1000)
            self._image[i] = 0 if(test / 1000 < probabilty) else 255

        self._image.resize((height, width))

    def copy_image_to_reset(self):
        self._image_reset = self._image.copy()

    def copy_image_from_reset(self):
        self._image = self._image_reset.copy()

    def show_image(self):
        cv2.imshow('Image', self._image)
        cv2.waitKey(0)

    def isImageGenarated(self):
        if(len(self._image) != 0):
            return True
        else:
            return False

    def _save_image_to_file(self, image, iter):
        path = f'out/out_{iter}.png'
        cv2.imwrite(path, image)

    def run_algorithm(self, number_of_iterations, isSave=False, saveIters=1):
        height = numpy.size(self._image, 0)
        width = numpy.size(self._image, 1)

        stefan = Ant(height, width)

        for i in range(1, number_of_iterations + 1):
            if(self._image[stefan.get_position()] == 255):
                stefan.rotate(-90)
                self._image = stefan.change_color(self._image)
                stefan.move()
            elif(self._image[stefan.get_position()] == 0):
                stefan.rotate(90)
                self._image = stefan.change_color(self._image)
                stefan.move()

            if(isSave and (i % saveIters == 0 or i in [1, number_of_iterations])):
                self._save_image_to_file(self._image, i)

        self.show_image()
