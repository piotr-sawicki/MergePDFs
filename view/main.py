from PyQt5.QtWidgets import QFileDialog


import sys, os
from PyQt5.QtWidgets import QMainWindow, QWidget, QListWidget, QListWidgetItem, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt, QUrl
from settings import *

from view.pdfs_list_qwidget import PDFsListQWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.listbox_view = PDFsListQWidget()
        self.merge_button = QPushButton("Merge PDFs")
        self.merge_button.clicked.connect(self.merge_pdfs)

        self.createUI()



    def createUI(self):

        # set layout
        widget = QWidget()
        grid = QGridLayout()
        grid.addWidget(self.listbox_view, 0, 0, 2, 2)
        grid.addWidget(self.merge_button, 3, 1)
        widget.setLayout(grid)

        self.setCentralWidget(widget)
        # set style
        qss = r'view/style.css'
        with open(qss, "r") as f:
            self.setStyleSheet(f.read())


    def merge_pdfs(self):
        pass

    def getSelectedItem(self):
        pass


