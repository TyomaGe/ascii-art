import pytest
from PIL import Image
from master.ascii_image import ASCIIArtHandler
from master.models.exceptions import WrongPathException, InvalidImageException


class TestASCIIArtHandler:
    @pytest.fixture
    def handler(self):
        return ASCIIArtHandler()

    @pytest.fixture
    def coloured_handler(self):
        return ASCIIArtHandler(is_coloured=True)

    @pytest.fixture
    def ascii_art(self):
        return "@_@"

    def test_load_image_non_existent_file(self, handler):
        with pytest.raises(WrongPathException):
            handler.load_image("file.png")

    def test_load_image_file_is_not_an_image(self, handler, tmp_path):
        image_path = tmp_path / "not_image.txt"
        image_path.write_text("пем")
        with pytest.raises(InvalidImageException):
            handler.load_image(image_path)

    def test_load_image_empty_path(self, handler):
        with pytest.raises(WrongPathException):
            handler.load_image("")

    def test_load_image_valid_file(self, handler, tmp_path):
        image_path = tmp_path / "test.png"
        Image.new("RGB", (10, 10), "blue").save(image_path)
        image = handler.load_image(image_path)
        assert image is not None
        assert image.size == (10, 10)

    def test_save_to_file_non_txt_file(self, handler, ascii_art, tmp_path):
        image_path = tmp_path / "image.png"
        with pytest.raises(WrongPathException):
            handler.save_to_file(ascii_art, str(image_path))

    def test_save_to_file_success(self, handler, ascii_art, tmp_path):
        image_path = tmp_path / "art.txt"
        handler.save_to_file(ascii_art, str(image_path))
        assert image_path.exists()
        with open(image_path, 'r') as f:
            content = f.read()
        assert content.strip() == ascii_art.strip()

    def test_save_to_file_html_success(self, coloured_handler, ascii_art,
                                       tmp_path):
        file_path = tmp_path / "art.html"
        coloured_handler.save_to_file(ascii_art, str(file_path))
        assert file_path.exists()
        content = file_path.read_text()
        assert "@_@" in content

    def test_save_to_file_html_wrong_extension(self, coloured_handler,
                                               ascii_art, tmp_path):
        file_path = tmp_path / "wrong_format.txt"
        with pytest.raises(WrongPathException):
            coloured_handler.save_to_file(ascii_art, str(file_path))

    def test_save_to_file_invalid_directory(self, handler, ascii_art,
                                            tmp_path):
        bad_path = tmp_path / "nonexistent" / "art.txt"
        with pytest.raises(WrongPathException):
            handler.save_to_file(ascii_art, str(bad_path))
