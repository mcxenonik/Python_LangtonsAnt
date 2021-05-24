from cv2 import imread, threshold, THRESH_BINARY
from numpy import ones

from Application.LangtonAlgorithm import LangtonAlgorithm


def test_creat_LangtonAlgorithm():                  ###### Testy niepoprawnych danych, ale bez obsługi w kodzie
    la1 = LangtonAlgorithm()

    assert len(la1._image) == 0
    assert len(la1._image_reset) == 0


def test_generate_white_image():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    img_ref = ones((100, 100)) * 255

    assert all((la1._image == img_ref).flatten())


def test_read_image_from_file():
    la1 = LangtonAlgorithm()

    path = 'tests/test1.png'
    la1.read_image_from_file(path)
    img_ref = imread(path, 0)
    img_ref = threshold(img_ref, 128, 255, THRESH_BINARY)[1]

    assert all((la1._image == img_ref).flatten())


def test_read_color_image_from_file():
    la1 = LangtonAlgorithm()

    path = 'tests/test2.png'
    la1.read_image_from_file(path)
    img_ref = imread(path, 0)
    img_ref = threshold(img_ref, 128, 255, THRESH_BINARY)[1]

    assert all((la1._image == img_ref).flatten())


def test_generate_random_imag():        # ############### zadany rozmiar, czy są dwie wartości, generujemy pliki tekstowe z ziarnem, podanie ziarenka
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


def test_isImageGenarated_true():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)

    assert la1.isImageGenarated()


def test_isImageGenarated_false():
    la1 = LangtonAlgorithm()

    assert not(la1.isImageGenarated())


def test_save_image_to_file():                          ##### temporary directories
    pass


def test_run_algorithm_white_image():
    la1 = LangtonAlgorithm()

    la1.generate_white_image(100, 100)
    img_ref = imread('tests/test3.png', 0)

    la1.run_algorithm(11000)

    assert all((la1._image == img_ref).flatten())
