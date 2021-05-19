from ..LangtonAlgorithm import LangtonAlgorithm
import cv2
import numpy


def test_creat_LangtonAlgorithm():
    la1 = LangtonAlgorithm()

    assert len(la1._image) == 0
    assert len(la1._image_reset) == 0


def test_generate_white_image():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    img_ref = numpy.ones((100, 100)) * 255

    assert all((la1._image == img_ref).flatten())


def test_read_image_from_file():
    la1 = LangtonAlgorithm()

    path = 'tests/test1.png'
    la1.read_image_from_file(path)
    img_ref = cv2.imread(path, 0)
    img_ref = cv2.threshold(img_ref, 128, 255, cv2.THRESH_BINARY)[1]

    assert all((la1._image == img_ref).flatten())


def test_read_color_image_from_file():
    la1 = LangtonAlgorithm()

    path = 'tests/test2.png'
    la1.read_image_from_file(path)
    img_ref = cv2.imread(path, 0)
    img_ref = cv2.threshold(img_ref, 128, 255, cv2.THRESH_BINARY)[1]

    assert all((la1._image == img_ref).flatten())


def test_read_not_a_image_from_file():
    pass


def test_generate_random_imag():        ################
    la1 = LangtonAlgorithm()

    la1.generate_random_image(100, 100, 0.1)


def test_copy_image_to_reset():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    img_ref = la1._image
    
    la1.copy_image_to_reset()
    

    assert all((la1._image_reset == img_ref).flatten())


def test_copy_image_from_reset():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    la1.copy_image_to_reset()
    img_ref = la1._image_reset
    
    la1.copy_image_from_reset()
    
    assert all((la1._image == img_ref).flatten())


def test_show_image():
    pass


def test_isImageGenarated_true():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)

    assert la1.isImageGenarated()


def test_isImageGenarated_false():
    la1 = LangtonAlgorithm()

    assert not(la1.isImageGenarated())


def test_save_image_to_file():
    pass


def test_run_algorithm_white_image():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    img_ref = cv2.imread('tests/test3.png', 0)

    la1.run_algorithm(11000)

    assert all((la1._image == img_ref).flatten())
    