from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QMessageBox


class LoadingGif(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(80, 80)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_animation = QLabel(self)
        self.movie = QMovie('spinner.gif')
        self.label_animation.setMovie(self.movie)
        timer = QTimer(self)
        self.startAnimation()
        # timer.singleShot(3000, self.stopAnimation)
        # self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()

    def pop_up(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText(str(message))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)

        msg.buttonClicked.connect(self.button_click)

        x = msg.exec_()

    def button_click(self, i):
        print(i.text())
        print("DONE")
        self.close()
