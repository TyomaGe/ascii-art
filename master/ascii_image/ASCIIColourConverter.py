from master.utilities import ASCII_CHAR


class ASCIIColourConverter:
    def __init__(self):
        self.__ascii_chars = ASCII_CHAR

    def pixels_to_coloured_ascii(self, image, invert=False):
        pixels = list(image.getdata())
        proportion = 255 // (len(self.__ascii_chars) - 1)
        ascii_chars = list(
            reversed(self.__ascii_chars)) if invert else self.__ascii_chars
        cache = {}
        result = []
        for r, g, b in pixels:
            key = (r, g, b)
            if key in cache:
                result.append(cache[key])
                continue
            brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
            char = ascii_chars[
                min(brightness // proportion, len(ascii_chars) - 1)]
            html_char = f'<span style="color: rgb({r},{g},{b})">{char}</span>'
            cache[key] = html_char
            result.append(html_char)
        return result

    def create_html_ascii_art(self, ascii_data, size):
        width = size[0]
        lines = [
            "".join(ascii_data[i:i + width])
            for i in range(0, len(ascii_data), width)
        ]
        return "<br>".join(lines)
