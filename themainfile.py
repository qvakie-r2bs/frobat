# импорты
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


def action():
    print('ДОВОЛЕН?')


def application():
    # создали саму приложуху и главное окно
    app = QApplication(sys.argv)
    window = QMainWindow()

    # название \ местоположение + размер окна
    window.setWindowTitle('toadbats')
    window.setGeometry(800, 400, 500, 500)

    button = QtWidgets.QPushButton(window)
    button.move(175, 200)
    button.setFixedHeight(100)
    button.setFixedWidth(150)
    button.setText('НАЖМИ ГАНДОН')
    button.clicked.connect(action)

    are = QtWidgets.QCheckBox(window)  

    main_text = QtWidgets.QLabel(window)
    main_text.setText('Просто тестирую надписи')
    main_text.move(250, 0)
    main_text.adjustSize()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()