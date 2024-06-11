import ui

#!/usr/bin/python

#from PyQt6.QtGui import QApplication
from PyQt6.QtWidgets import QApplication
from ui.sim import MainWindow

def main():
    import sys
    # exec.test()
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
