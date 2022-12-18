


import sys
import os

from PyQt5.QtWidgets import QApplication                                                                                                                                                                                                                                                                                                                                                                                                                                               
from project.controller import Controller


qApp = QApplication(sys.argv)


environment = {
    'controller' : Controller(),
    'model' : Controller().Model,
    'view' : Controller().View
}


def main() -> bool:
    try:

        environment['controller'].get_main_window_view()
        qApp.exec_()

        return True

    except:
        return False


if __name__ == '__main__':
    main()