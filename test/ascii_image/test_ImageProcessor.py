import pytest
from PIL import Image
from master.ascii_image import ImageProcessor
from master.models.exceptions import *


class TestImageProcessor:
    @pytest.fixture
    def handler(self):
        return ImageProcessor()

    @pytest.fixture
    def image(self):
        image = Image.new("L", (2, 2))
        image.putdata([0, 85, 170, 255])
        return image

    @pytest.fixture
    def test_size_none(self):
        return None

    @pytest.fixture
    def new_size(self):
        return 123, 456

    @pytest.fixture
    def invalid_value_size(self):
        return "country road", "take me home"

    @pytest.fixture
    def non_positive_width_values(self):
        return -23, 233

    @pytest.fixture
    def non_positive_height_values(self):
        return 123, 0

    def test_handle_size_none_size(self, handler, image, test_size_none):
        width, height = image.size
        assert handler.handle_size(image, test_size_none) == (
            width, height // 2)

    def test_handle_size_new_size(self, handler, image, new_size):
        assert handler.handle_size(image, new_size) == new_size

    def test_handle_size_invalid_width_value(self, handler, image,
                                             invalid_value_size):
        with pytest.raises(InvalidSizeValueException):
            handler.handle_size(image, invalid_value_size)

    def test_handle_size_non_positive_width(self, handler, image,
                                            non_positive_width_values):
        with pytest.raises(WrongImageWidthException):
            handler.handle_size(image, non_positive_width_values)

    def test_handle_size_non_positive_height(self, handler, image,
                                             non_positive_height_values):
        with pytest.raises(WrongImageHeightException):
            handler.handle_size(image, non_positive_height_values)

    def test_resize_image_via_grayscale(self, handler, image, new_size):
        gray_image = handler.convert_to_grayscale(image, new_size)
        assert gray_image.size == new_size

    def test_convert_to_grayscale_returns_grayscale(self, handler, image):
        gray_image = handler.convert_to_grayscale(image, image.size)
        assert gray_image.mode == "L"

    def test_convert_to_grayscale_preserves_data(self, handler, image):
        gray_image = handler.convert_to_grayscale(image, image.size)
        assert len(list(gray_image.getdata())) == 4
