from Ant import Ant
import cv2
import numpy
import random


class LangtonAlgorithm():
    def __init__(self):
        pass

    def generate_white_image(self, height, width):
        image = numpy.ones((height, width)) * 255

        return image


    def read_image_from_file(self, path):
        image = cv2.imread(path, 0)
        image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]

        return image


    def generate_random_image(self, height, width, probabilty):
        image = numpy.ndarray(height * width)

        for i in range(len(image)):
            test = random.randint(1, 1000)
            image[i] = 0 if(test / 1000 < probabilty) else 255

        image.resize((height, width))

        return image


    def _save_image_to_file(self, image, iter):
        path = f'out/out_{iter}.png'
        cv2.imwrite(path, image)


    def run_algorithm(self, image, number_of_iterations, isSave=False, saveIter=1):
        height = numpy.size(image, 0)
        width = numpy.size(image, 1)

        stefan = Ant(height, width)

        for i in range(1, number_of_iterations + 1):
            if(image[stefan.get_position()] == 255):
                stefan.rotate(-90)
                image = stefan.change_color(image)
                stefan.move()
            elif(image[stefan.get_position()] == 0):
                stefan.rotate(90)
                image = stefan.change_color(image)
                stefan.move()

            if(isSave and (i % saveIter == 0 or i in [1, number_of_iterations])):
                self._save_image_to_file(image, i)

        cv2.imshow('Image', image)
        cv2.waitKey(0)
