ASCII_CHAR = list(' .",:;!~+-xmo*#W&8@')

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>ASCII Art</title>
  <style>
    body {{
      background-color: black;
      color: white;
      font-family: monospace;
      white-space: pre;
    }}
  </style>
</head>
<body>
{ascii_art}
</body>
</html>
"""

ARGPARSE_DESCRIPTION = (
    "Convert images to ASCII art. The program processes standard "
    "image formats (JPG, PNG, etc.)\nby converting each pixel to "
    "a corresponding ASCII character,\nproducing art that can be "
    "saved as a text or HTML file."
)

ARGPARSE_EPILOG = (
    "Examples:\n"
    " python -m master.core.main ./image.jpg\n"
    " python -m master.core.main ./image.jpg -sv ./output.txt\n"
    " python -m master.core.main ./image.jpg -sv ./output.html -c\n"
    " python -m master.core.main ./image.jpg -sv ./output.html -c -s 720 480\n"
    " python -m master.core.main ./image.jpg -i\n"
)
