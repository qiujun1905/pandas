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

if __name__ == '__main__':
    def calc(capital, rate_of_return, number_of_months):
      for month in range(1, number_of_months + 1):
        gain = capital * rate_of_return
        capital += gain
        print('第{0}个月本金加盈利共：{1},盈利为：{2}'.format(month, capital, gain,))
      return capital

    print(calc(100000, 0.1, 120))