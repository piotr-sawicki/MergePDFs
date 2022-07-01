import os
import sys
from PyQt5.QtWidgets import QListWidget, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from settings import FILE_EXTENSION


def try_block(function, *args, **kwargs):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            print(function.__name__)
            print(sys.exc_info())
    return wrapper


class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    @try_block
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    @try_block
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    @try_block
    def dropEvent(self, event, *args, **kwargs):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    file_path = str(url.toLocalFile())
                    _, file_extension = os.path.splitext(file_path)
                    if file_extension.lower() == FILE_EXTENSION:
                        links.append(file_path)
            self.addItems(links)
        else:
            event.ignore()


class PDFsListQWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("List of PDFs to merge:")
        self.list = ListBoxWidget()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.list)
        self.setLayout(layout)
