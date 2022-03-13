import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.1'
__author__ = 'Fluxt'

class PyCalcUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

def main():
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()