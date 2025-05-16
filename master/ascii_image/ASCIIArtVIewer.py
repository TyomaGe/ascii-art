import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea
from PyQt6.QtCore import Qt, QTimer


class ASCIIArtViewer:
    def __init__(self, ascii_art, size, is_coloured=False):
        print(f"\n\033[92mThe image is rendering . . .\033[0m\n")
        self.__app = QApplication(sys.argv)
        self.__window = QMainWindow()
        self.__ascii_art = ascii_art
        self.__size = size
        self.__is_coloured = is_coloured
        self.__setup_ui_components()
        self.__init_window_config()
        self.__setup_font()
        self.__load_art()
        self.__window_open()
        QTimer.singleShot(100, self.__finalize_setup)
        self.__window_close()

    def __load_art(self):
        self.__main_label.setUpdatesEnabled(False)
        if self.__is_coloured:
            self.__main_label.setTextFormat(Qt.TextFormat.RichText)
            self.__main_label.setTextInteractionFlags(
                Qt.TextInteractionFlag.NoTextInteraction)
            self.__main_label.setStyleSheet(
                "QLabel { background-color: black; }")
            self.__main_label.setText(f"<pre>{self.__ascii_art}</pre>")
        else:
            self.__main_label.setTextFormat(Qt.TextFormat.PlainText)
            self.__main_label.setText(self.__ascii_art)
        self.__main_label.setUpdatesEnabled(True)

    def __setup_ui_components(self):
        self.__scroll = QScrollArea()
        self.__scroll.setWidgetResizable(True)
        self.__window.setCentralWidget(self.__scroll)
        self.__main_label = QLabel()
        self.__scroll.setWidget(self.__main_label)

    def __setup_font(self):
        font = self.__main_label.font()
        font.setFamily("Courier New")
        font.setPointSize(1)
        font.setStyleStrategy(QFont.StyleStrategy.PreferDefault)
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 0)
        font.setWordSpacing(0)
        self.__main_label.setFont(font)

    def __init_window_config(self):
        self.__window.setWindowTitle("ASCII Art Viewer")
        self.__window.setGeometry(0, 0, self.__size[0], self.__size[1] * 2)
        self.__main_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.__main_label.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.__main_label.setUpdatesEnabled(True)

    def __finalize_setup(self):
        self.__main_label.adjustSize()
        self.__window.update()

    def __window_open(self):
        self.__window.show()

    def __window_close(self):
        sys.exit(self.__app.exec())
