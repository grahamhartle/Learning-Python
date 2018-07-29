import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l1.setText('Hello World')
    l2.setPixmap(QtGui.QPixmap('Globe.png'))
    w.setWindowTitle('PyQt5 Lesson 1')
    w.setGeometry(100, 100, 300, 200)
    l1.move(110, 20)
    l2.move(100, 65)
    w.show()
    sys.exit(app.exec_())

window()