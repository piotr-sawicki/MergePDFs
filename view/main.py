from PyQt5.QtWidgets import QFileDialog


import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt, QUrl
from settings import *


class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    file_path = str(url.toLocalFile())
                    _, file_extension = os.path.splitext(file_path)
                    if file_extension.lower() == FILE_EXTENSION:
                        links.append(str(url.toLocalFile()))
            self.addItems(links)
        else:
            event.ignore()


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):

        self.label = QLabel("List of PDFs to merge:")
        self.listbox_view = ListBoxWidget(self)

        self.btn = QPushButton("get")
        self.btn.clicked.connect(self.getSelectedItem)

        self.merge_button = QPushButton("Merge PDFs")
        self.merge_button.clicked.connect(self.merge_pdfs)

        # set layout
        grid = QGridLayout()
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.listbox_view, 1, 0, 2, 2)
        grid.addWidget(self.btn, 3, 0)
        grid.addWidget(self.merge_button, 3, 1)
        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 150)

        qss = r'view/style.css'
        with open(qss, "r") as f:
            self.setStyleSheet(f.read())




    def merge_pdfs(self):
        list_of_pdfs_to_merge = []

    def getSelectedItem(self):
        item = QListWidgetItem(self.listbox_view.currentItem())
        return item.text()


