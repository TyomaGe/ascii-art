import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea
from PyQt6.QtCore import Qt, QTimer


class ASCIIArtViewer:
    def __init__(self, ascii_art, size):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.ascii_art = ascii_art
        self.size = size
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.window.setCentralWidget(self.scroll)
        self.main_label = QLabel()
        self.scroll.setWidget(self.main_label)
        self.__init_window_config()
        self.__load_art()
        self.__window_open()
        QTimer.singleShot(100, self.__finalize_setup)
        self.__window_close()

    def __init_window_config(self):
        self.window.setWindowTitle("ASCII Art Viewer")
        self.window.setGeometry(0, 0, self.size[0], self.size[1] * 2)
        font = self.main_label.font()
        font.setFamily("Courier New")
        font.setPointSize(1)
        font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
        self.main_label.setFont(font)
        self.main_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.main_label.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.main_label.setUpdatesEnabled(True)

    def __finalize_setup(self):
        self.main_label.adjustSize()
        self.window.update()

    def __window_open(self):
        self.window.show()

    def __window_close(self):
        sys.exit(self.app.exec())

    def __load_art(self):
        self.main_label.setText(self.ascii_art)
        self.main_label.setUpdatesEnabled(False)
        self.main_label.setText(self.ascii_art)
        self.main_label.setUpdatesEnabled(True)