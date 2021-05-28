from cv2 import imread, threshold, THRESH_BINARY
from numpy.testing import assert_array_equal
from numpy.random import binomial, seed
from numpy import ones, size, uint8
import pytest

from Application.LangtonAlgorithm import LangtonAlgorithm


def test_creat_LangtonAlgorithm():
    la1 = LangtonAlgorithm()

    assert len(la1._image) == 0
    assert len(la1._image_reset) == 0


def test_generate_white_image():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    img_ref = ones((100, 100)) * 255

    assert_array_equal(la1._image, img_ref)


def test_generate_white_image_negative_size():
    la1 = LangtonAlgorithm()

    with pytest.raises(ValueError):
        la1.generate_white_image(-5, 100)


def test_read_image_from_file():
    la1 = LangtonAlgorithm()

    path = 'tests/test1.png'
    la1.read_image_from_file(path)
    img_ref = imread(path, 0)
    img_ref = threshold(img_ref, 128, 255, THRESH_BINARY)[1]

    assert_array_equal(la1._image, img_ref)


def test_read_image_from_file_wrong_type():
    la1 = LangtonAlgorithm()
    path = 0

    with pytest.raises(TypeError):
        la1.read_image_from_file(path)


def test_read_image_from_file_wrong_path():
    la1 = LangtonAlgorithm()
    path = 'sth'
    la1.read_image_from_file(path)

    assert_array_equal(la1._image, None)


def test_read_color_image_from_file():
    la1 = LangtonAlgorithm()

    path = 'tests/test2.png'
    la1.read_image_from_file(path)
    img_ref = imread(path, 0)
    img_ref = threshold(img_ref, 128, 255, THRESH_BINARY)[1]

    assert_array_equal(la1._image, img_ref)


def test_generate_random_image_size():
    la1 = LangtonAlgorithm()

    la1.generate_random_image(100, 100, 0.1)
    image = la1.get_image()

    assert size(image, 0) == 100
    assert size(image, 1) == 100


def test_generate_random_image_values():
    la1 = LangtonAlgorithm()

    la1.generate_random_image(100, 100, 0.1)
    image = la1.get_image().flatten()

    test = True
    for i in range(len(image)):
        if(image[i] not in [0, 255]):
            test = False

    assert test


def test_generate_random_image_negative_size():
    la1 = LangtonAlgorithm()

    with pytest.raises(ValueError):
        la1.generate_random_image(-5, 100, 0.1)


def test_generate_random_image_negative_probability():
    la1 = LangtonAlgorithm()

    with pytest.raises(ValueError):
        la1.generate_random_image(100, 100, -2)


def test_generate_random_image_seed():
    la1 = LangtonAlgorithm()

    la1.generate_random_image(100, 100, 0.1, 666)

    seed(666)
    img_ref = binomial(1, 1 - 0.1, (100, 100)).astype(uint8) * 255

    assert_array_equal(la1._image, img_ref)


def test_copy_image_to_reset():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    img_ref = la1._image

    la1.copy_image_to_reset()

    assert_array_equal(la1._image_reset, img_ref)


def test_copy_image_from_reset():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    la1.copy_image_to_reset()
    img_ref = la1._image_reset

    la1.copy_image_from_reset()

    assert_array_equal(la1._image, img_ref)


def test_isImageGenarated_true():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)

    assert la1.is_image_genarated()


def test_isImageGenarated_false():
    la1 = LangtonAlgorithm()

    assert not(la1.is_image_genarated())


def test_create_ant():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    la1.create_ant()

    assert la1._ant._max_position_y == 99
    assert la1._ant._max_position_x == 99

    assert la1._ant._position_y == 50
    assert la1._ant._position_x == 50

    assert la1._ant._direction == 0


def test_run_algorithm_white_image():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    img_ref = imread('tests/test3.png', 0)

    la1.create_ant()

    for i in range(1, 11001):
        la1.step_algorithm()

    assert_array_equal(la1._image, img_ref)
