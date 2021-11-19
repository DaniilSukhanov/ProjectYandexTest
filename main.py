import sys


from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import uic
from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.draw_flag = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.draw_flag = True
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw()
        self.qp.end()

    def draw(self):
        if self.draw_flag:
            self.qp.setBrush(QColor(255, 255, 0))
            for _ in range(10):
                k = randint(30, 60)
                x, y = (
                    randint(0, self.width() - k),
                    randint(0, self.height() - k)
                )
                self.qp.drawEllipse(x, y, k, k)
                self.draw_flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
