# import configparser
#
# config = configparser.ConfigParser()
# config.read('FILE.INI')
# print(config['DEFAULT']['path'])     # -> "/path/name/"
# config['DEFAULT']['path'] = '/var/shared/'    # update
# config['DEFAULT']['default_message'] = 'Hey! help me!!'   # create
#
# with open('FILE.INI', 'w') as configfile:    # save
#     config.write(configfile)

# import configparser
# from os import path
#
# config = configparser.ConfigParser()
#
# print(path.exists("../POS_Django/FILE.INI"))
#
# if not (path.exists("../POS_Django/FILE.INI")):
#     config['DEFAULT']['user_id'] = ''   # create
#     config['DEFAULT']['token'] = ''
#     config['DEFAULT']['login_status'] = "False"
#     with open("FILE.ini", "w") as configFile:
#         config.write(configFile)
# else:
#     config.read('FILE.INI')
#     print("Status: "+str(config['DEFAULT']['login_status']))


# import sys
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtWidgets import QLabel, QApplication, QWidget
#
#
# class LoadingGif(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(62, 62)
#         self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
#         self.label_animation = QLabel(self)
#         self.movie = QMovie('91.gif')
#         self.label_animation.setMovie(self.movie)
#         timer = QTimer(self)
#         self.startAnimation()
#         timer.singleShot(3000, self.stopAnimation)
#         self.show()
#
#     def startAnimation(self):
#         self.movie.start()
#
#     def stopAnimation(self):
#         self.movie.stop()
#         self.close()
#
#
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         label = QLabel('<font size=12> OK! </font>', self)
#         label.setGeometry(100, 100, 100, 50)
#
#
# # app = QApplication(sys.argv)
# # demo = LoadingGif()
# # sys.exit(app.exec_())

# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import Qt
#
#
# class LoadingGif(object):
#
#     def mainUI(self, FrontWindow):
#         FrontWindow.setObjectName("FTwindow")
#         FrontWindow.resize(320, 300)
#         self.centralwidget = QtWidgets.QWidget(FrontWindow)
#         self.centralwidget.setObjectName("main-widget")
#
#         # Label Create
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
#         self.label.setMinimumSize(QtCore.QSize(250, 250))
#         self.label.setMaximumSize(QtCore.QSize(250, 250))
#         self.label.setObjectName("lb1")
#         FrontWindow.setCentralWidget(self.centralwidget)
#
#         # Loading the GIF
#         self.movie = QMovie("91.gif")
#         self.label.setMovie(self.movie)
#
#         self.startAnimation()
#
#     # Start Animation
#
#     def startAnimation(self):
#         self.movie.start()
#
#     # Stop Animation(According to need)
#     def stopAnimation(self):
#         self.movie.stop()
#
#
# app = QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QMainWindow()
# demo = LoadingGif()
# demo.mainUI(window)
# window.show()
# sys.exit(app.exec_())


# config.read('FILE.INI')
#
# config['DEFAULT']['user_id'] = ''   # create
# config['DEFAULT']['token'] = ''
# config['DEFAULT']['login_status'] = "False"
#
#
# with open('FILE.INI', 'w') as configfile:    # save
#     config.write(configfile)
import sqlite3
import json


# def DBSETTINGS():
#     conn = sqlite3.connect('test.db')
#     print("Opened database successfully")
#
#     conn.execute('''CREATE TABLE IF NOT EXISTS USERS
#             (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#             USERS          json    NOT NULL);''')
#     print("Table created successfully")
#
#     conn.close()
#
#
# def PUSHDB(data):
#     print(str(data[0]["id"]))
#     conn = sqlite3.connect('test.db')
#     print("Opened database successfully")
#     c = conn.cursor()
#     c.execute("insert into USERS values (?,?)", [1, json.dumps(data)])
#     conn.commit()
#     conn.close()
#
#
# def RETRIEVE_DATA_FROM_SQL():
#     # select data from countries
#     conn = sqlite3.connect('test.db')
#     print("Opened database successfully")
#     c = conn.cursor()
#     c.execute("select USERS from USERS")
#     rows = c.fetchall()
#     datas = json.loads(rows[0][0])
#     # datas[0]["id"] = 12 //setter
#     print(str(datas[0]["id"]))
#
#
# from woocommerce import API
#
# wcapi = API(
#     url="http://pos.sharpwp.com/",
#     consumer_key="ck_b1438481a2274b8cf70afaa3b1d74f11087fe3cd",
#     consumer_secret="cs_ef6b3e25f5e31ed2279f927042726b5657de97e4",
#     wp_api=True,
#     version="wc/v3",
# )

# customers = wcapi.get("customers").json()
# PUSHDB(customers)
# DBSETTINGS()
# RETRIEVE_DATA_FROM_SQL()


# print("Customer id is:- "+str(customers[0]["_links"]["self"][0]["href"]))
# print("Customers api data length is: "+ str(len(customers)))


# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
#
# #open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read())


# import json
#
# class User:
#     def __init__(self, name, username):
#         self.name = name
#         self.username = username
#
#     def to_json(self):
#         return json.dumps(self.__dict__)
#
#     @classmethod
#     def from_json(cls, json_str):
#         json_dict = json.loads(json_str)
#         return cls(**json_dict)
#
# # example usage
# User("tbrown", "Tom Brown").to_json()
# User.from_json(User("tbrown", "Tom Brown").to_json()).to_json()


# import json
#
#
# class Object:
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
#


import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen
from PyQt5.QtCore import QTimer

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.b1 = QPushButton('Display screensaver')
        self.b1.clicked.connect(self.flashSplash)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.b1)

    def flashSplash(self):
        self.splash = QSplashScreen(QPixmap('D:/_Qt/img/pyqt.jpg'))

        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

        self.splash.show()

        # Close SplashScreen after 2 seconds (2000 ms)
        QTimer.singleShot(2000, self.splash.close)
        print("HERE it will go to next page")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Dialog()
    main.show()
    sys.exit(app.exec_())