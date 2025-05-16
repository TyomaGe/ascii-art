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