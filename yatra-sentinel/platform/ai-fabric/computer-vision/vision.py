"""Placeholder computer vision utilities."""

from PIL import Image


def thumbnail(path: str, size=(128, 128)) -> Image.Image:
    """Return a thumbnail of an image without saving."""
    img = Image.open(path)
    img.thumbnail(size)
    return img
