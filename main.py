import glob
import os

from PIL import Image
from loguru import logger

import exif

WATERMARK_HEIGHT_IN_PIXELS = 23

PATH_TO_SOURCE_IMAGES = f"{os.getcwd()}/source"


def get_source_images():
    return glob.iglob(f"{PATH_TO_SOURCE_IMAGES}/*.jpg")


def crop_watermark(image: Image) -> Image:
    width, height = image.size
    box = (0, 0, width, height - WATERMARK_HEIGHT_IN_PIXELS)
    logger.info(f"Cropped {image.filename} image on {box} size")
    return image.crop(box)


def save_cropped_image(image: Image, filename: str) -> None:
    path = f"{os.getcwd()}/output/{filename}"
    if not os.path.exists("output"):
        os.mkdir("output")

    logger.info(f"Save cropped image to {path}")

    image.save(path)


if __name__ == "__main__":
    for path in get_source_images():
        logger.debug(f"Trying to open image: {path}")
        image = Image.open(path)

        logger.debug(f"Read exif from source image: {exif.read_exif_tags(image)}")

        cropped_image = crop_watermark(image)
        save_cropped_image(cropped_image, os.path.basename(image.filename))
