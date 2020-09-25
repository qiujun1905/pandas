from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLineEdit


class MyLineEdit(QLineEdit):
  clicked = pyqtSignal(QLineEdit)
  def mouseReleaseEvent(self, QMouseEvent):
    if QMouseEvent.button() == Qt.LeftButton:
      self.clicked.emit(self)