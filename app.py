import sys
from view.main import AppDemo
from PyQt5.QtWidgets import QApplication
from settings import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationDisplayName(f'{APP_NAME} - {APP_VERSION}')

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())