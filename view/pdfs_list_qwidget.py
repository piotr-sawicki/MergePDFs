import os
import sys
from PyQt5.QtWidgets import QListWidget, QWidget, QGridLayout, QLabel, QToolButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

from settings import FILE_EXTENSION
from view.custom_functions import set_icon, try_block


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
        self.up_button = QToolButton()
        self.down_button = QToolButton()
        self.add_pdf = QToolButton()
        self.remove_pdf = QToolButton()
        self.initUI()

    def initUI(self):

        v_layout = QVBoxLayout()
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        v_layout.addWidget(self.up_button)
        v_layout.addWidget(self.down_button)
        v_layout.addWidget(self.add_pdf)
        v_layout.addWidget(self.remove_pdf)
        v_layout.addItem(vertical_spacer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.list)

        grid = QGridLayout()
        grid.addWidget(self.label, 0, 1)
        grid.addWidget(self.list, 1, 1)
        grid.addLayout(v_layout, 1, 0)

        self.setLayout(grid)

        set_icon(self.up_button, "SP_ArrowUp")
        set_icon(self.down_button, "SP_ArrowDown")
        set_icon(self.add_pdf, "SP_DirOpenIcon")
        set_icon(self.remove_pdf, "SP_DialogCancelButton")
