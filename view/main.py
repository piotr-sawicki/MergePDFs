from PyQt5.QtWidgets import QFileDialog


import sys, os
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QToolButton, QAbstractButton, QGridLayout, QStyle, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl
from settings import *

from view.pdfs_list_qwidget import PDFsListQWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.listbox_view = PDFsListQWidget()
        self.merge_button = QPushButton("Merge PDFs")
        self.up_button = QToolButton()
        self.down_button = QToolButton()
        self.add_pdf = QToolButton()
        self.remove_pdf = QToolButton()

        self.merge_button.clicked.connect(self.merge_pdfs)



        self.createUI()



    def createUI(self):

        # set layout
        widget = QWidget()
        grid = QGridLayout()

        v_layout = QVBoxLayout()
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        v_layout.addWidget(self.up_button)
        v_layout.addWidget(self.down_button)
        v_layout.addWidget(self.add_pdf)
        v_layout.addWidget(self.remove_pdf)
        v_layout.addItem(vertical_spacer)

        grid.addWidget(self.listbox_view, 0, 1)
        grid.addLayout(v_layout, 0, 0)
        grid.addWidget(self.merge_button, 1, 1)

        widget.setLayout(grid)

        self.setCentralWidget(widget)

        set_icon(self.merge_button, "SP_MessageBoxCritical")
        set_icon(self.up_button, "SP_ArrowUp")
        set_icon(self.down_button, "SP_ArrowDown")
        set_icon(self.add_pdf, "SP_DirOpenIcon")
        set_icon(self.remove_pdf, "SP_DialogCancelButton")

        # set style
        qss = r'view/style.css'
        with open(qss, "r") as f:
            self.setStyleSheet(f.read())




    def merge_pdfs(self):
        pass

    def getSelectedItem(self):
        pass


def set_icon(button: QAbstractButton, icon_name: str) -> QAbstractButton:
    """
    sets icon for button from the file or predefined PyQt5`s icons
    :param button:
    :param icon_name:
    :return: button with the icon
    """

    if os.path.isfile(icon_name):
        icon = QIcon(icon_name)
    else:
        try:
            pixmapi = getattr(QStyle, icon_name)
            icon = button.style().standardIcon(pixmapi)
        except AttributeError:
            icon = QIcon()
    button.setIcon(icon)
    return button
