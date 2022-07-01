import sys
from view.main import MainWindow
from PyQt5.QtWidgets import QApplication
from settings import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationDisplayName(f'{APP_NAME} - {APP_VERSION}')

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
