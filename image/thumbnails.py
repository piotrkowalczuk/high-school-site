from cStringIO import StringIO
from PIL import Image, ImageOps


def generate_thumbnail(image, height, width):

    target_size = width, height
    image = Image.open(StringIO(image.read()))

    image = image.thumbnail(target_size, Image.ANTIALIAS)
    #image = ImageOps.fit(image, target_size, Image.ANTIALIAS)

    return image


def get_pil_type(image):

    image_type = image.content_type

    if image_type == 'image/jpeg':
        return 'jpeg'
    elif image_type == 'image/png':
        return 'png'


def get_extension(image):

    image_type = image.content_type

    if image_type == 'image/jpeg':
        return 'jpg'
    elif image_type == 'image/png':
        return 'png'


def save(image, path, quality):
    pass
