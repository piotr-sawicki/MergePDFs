from PyQt5.QtWidgets import QFileDialog


import sys, os
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QToolButton, QAbstractButton, QGridLayout, QStyle, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl
from settings import *

from view.pdfs_list_qwidget import PDFsListQWidget
from view.custom_functions import set_icon


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
        h_layout = QHBoxLayout()
        h_spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_layout.addItem(h_spacer)
        h_layout.addWidget(self.merge_button)

        grid.addWidget(self.listbox_view, 0, 0)
        grid.addLayout(h_layout, 1, 0)
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



