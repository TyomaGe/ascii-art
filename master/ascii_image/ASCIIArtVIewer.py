import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea
from PyQt6.QtCore import Qt, QTimer


class ASCIIArtViewer:
    def __init__(self, ascii_art, size):
        self.__app = QApplication(sys.argv)
        self.__window = QMainWindow()
        self.__ascii_art = ascii_art
        self.__size = size
        self.__setup_ui_components()
        self.__init_window_config()
        self.__setup_font()
        self.__load_art()
        self.__window_open()
        QTimer.singleShot(100, self.__finalize_setup)
        self.__window_close()

    def __setup_ui_components(self):
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.__window.setCentralWidget(self.scroll)
        self.main_label = QLabel()
        self.scroll.setWidget(self.main_label)

    def __setup_font(self):
        font = self.main_label.font()
        font.setFamily("Courier New")
        font.setPointSize(1)
        font.setStyleStrategy(QFont.StyleStrategy.PreferDefault)
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 0)
        font.setWordSpacing(0)
        self.main_label.setFont(font)

    def __init_window_config(self):
        self.__window.setWindowTitle("ASCII Art Viewer")
        self.__window.setGeometry(0, 0, self.__size[0], self.__size[1] * 2)
        self.main_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.main_label.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.main_label.setUpdatesEnabled(True)

    def __finalize_setup(self):
        self.main_label.adjustSize()
        self.__window.update()

    def __window_open(self):
        self.__window.show()

    def __window_close(self):
        sys.exit(self.__app.exec())

    def __load_art(self):
        self.main_label.setUpdatesEnabled(False)
        self.main_label.setText(self.__ascii_art)
        self.main_label.setUpdatesEnabled(True)
