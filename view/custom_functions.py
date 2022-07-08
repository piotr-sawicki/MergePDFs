import os
import sys
from PyQt5.QtWidgets import QAbstractButton, QStyle
from PyQt5.QtGui import QIcon


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

def try_block(function, *args, **kwargs):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            print(function.__name__)
            print(sys.exc_info())
    return wrapper