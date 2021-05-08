def validate_image_height(image_height):
    if(image_height not in list(range(1001))):
        return False
    else:
        return True


def validate_image_width(image_width):
    if(image_width not in list(range(1001))):
        return False
    else:
        return True


def validate_path_to_image(path_to_image):
    pass


def validate_probabilty(probabilty):
    if((probabilty * 1000) not in list(range(1001))):
        return False
    else:
        return True


def validate_save_iterations(save_iterations):
    if(save_iterations not in list(range(1001))):
        return False
    else:
        return True


def validate_number_of_iterations(number_of_iterations):
    if(number_of_iterations not in list(range(1000001))):
        return False
    else:
        return True
