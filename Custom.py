from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLineEdit, QMenu


class MyLineEdit(QLineEdit):

  clicked = pyqtSignal(QLineEdit)
  def mouseReleaseEvent(self, QMouseEvent):
    if QMouseEvent.button() == Qt.LeftButton:
      self.clicked.emit(self)


class Menu(QMenu):
  def focusInEvent(self, event):
    print("事件--------->", event)