import numpy as np
from PIL import Image, ImageEnhance
from skimage.filters import threshold_otsu


class Processor:
    """Handles image processing tasks."""

    def __init__(self, settings):
        self.settings = settings

    @staticmethod
    def enhance_sharpness(img, factor):
        """Enhance the sharpness of an image."""
        enhancer = ImageEnhance.Sharpness(img)
        return enhancer.enhance(factor)

    @staticmethod
    def apply_otsu_threshold(img_path):
        """Apply Otsu's thresholding method to an image."""
        img = Image.open(img_path)
        img_array = np.array(img)
        gray_img = np.mean(img_array, axis=2)
        gray_threshold = threshold_otsu(gray_img)
        mask = np.mean(img_array, axis=2) > gray_threshold
        img_array[mask] = img_array[mask] + (255 - img_array[mask]) * 0.5
        img_array = np.clip(img_array, 0, 255)
        return Image.fromarray(img_array.astype('uint8'))
