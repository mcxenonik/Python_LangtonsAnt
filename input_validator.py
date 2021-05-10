def validate_image_height(image_height):
    if(not(image_height.isnumeric())
       or int(image_height) not in list(range(1, 1001))):
        return False
    else:
        return True


def validate_image_width(image_width):
    if(not(image_width.isnumeric())
       or int(image_width) not in list(range(1, 1001))):
        return False
    else:
        return True


def validate_path_to_image(path_to_image):
    pass


def validate_probabilty(proba):
    if(not(proba.replace('.', '', 1).isnumeric())
       or (float(proba) * 1000) not in list(range(1, 1001))):
        return False
    else:
        return True


def validate_save_iterations(save_iter):
    if(not(save_iter.isnumeric)
       or int(save_iter) not in list(range(1, 1001))):
        return False
    else:
        return True


def validate_num_of_iter(num_of_iter):
    if(not(num_of_iter.isnumeric())
       or int(num_of_iter) not in list(range(1, 1000001))):
        return False
    else:
        return True
