from PIL import Image, ExifTags


def read_exif_tags(image: Image) -> dict:
    return {
        ExifTags.TAGS[k]: v
        for k, v in image.getexif().items()
        if k in ExifTags.TAGS
    }
