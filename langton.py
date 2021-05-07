from ant_class import Ant
import cv2
import numpy
import random

#######################################
# height = 250
# width = 250

# image = numpy.ones((height, width)) * 255
#######################################

#######################################
# image = cv2.imread('test.png', 0)
# image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
# height = numpy.size(image, 0)
# width = numpy.size(image, 1)
#######################################

#######################################
probabilty = 0.1
height = 500
width = 500

image = numpy.ndarray(height * width)

for i in range(len(image)):
    test = random.randint(1, 1000)
    image[i] = 0 if(test / 1000 < probabilty) else 255

image.resize((height, width))
#######################################

ant1 = Ant([int(height / 2), int(width / 2)])

for i in range(110000):
    if(image[ant1.get_position()] == 255):
        image = ant1.change_color(image)
        ant1.move_left()
    elif(image[ant1.get_position()] == 0):
        image = ant1.change_color(image)
        ant1.move_right()

cv2.imshow('Image', image)
cv2.waitKey(0)

# cv2.imwrite('test2.jpg', im)
