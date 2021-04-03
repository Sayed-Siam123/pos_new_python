import os
import configparser
import sys

from os import path

from PyQt5 import QtWidgets

from LicenceKey import Ui_LicenceWindow
from PosTerminal import Ui_PosWindow
from api_provider import ApiProvider
from db_provider import DBProvider
from constant import system_path, db_path, document_path, db_name
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QSplashScreen, QMainWindow
from PyQt5.QtCore import QTimer, Qt
from PosTerminal import Ui_PosWindow

config = configparser.ConfigParser()
status = ""

API = ApiProvider()
DB = DBProvider()

print(path.exists(document_path))
print(path.exists(system_path + "/config.INI"))


def initDB():
    print(DB.db_connect(db_name, db_path))


def initDBTables():
    DB.createProductsTable(db_path + "POS.db")
    DB.createCustomersTable(db_path + "POS.db")


def FetchfromAPI():
    customerList = API.getCustomer()
    productList = API.getProduct()
    print(customerList[0]['id'])
    print(productList[0]['id'])
    # DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
    # print(path.basename().lower)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = QtWidgets.QMainWindow()
        self.PosUi = Ui_PosWindow()
        self.LicenceUi = Ui_LicenceWindow()


        self.splash = QSplashScreen(QPixmap('pos.jpg'))

        if not (path.exists(system_path)):
            os.makedirs(system_path)
            os.makedirs(db_path)
            initDB()
            initDBTables()
            if not (path.exists(system_path + "config.INI")):
                config['DEFAULT']['user_id'] = ''  # create
                config['DEFAULT']['token'] = ''
                config['DEFAULT']['login_status'] = "False"
                status = "False"
                with open(system_path + "config.INI", "w") as configFile:
                    config.write(configFile)
        else:
            config.read(system_path + 'config.INI')
            print("Status: " + str(config['DEFAULT']['login_status']))

        self.splash.show()
        QTimer.singleShot(5000, self.navigate)

    def navigate(self):
        if status == "False" or str(config['DEFAULT']['login_status']) == "False":
            self.window = QtWidgets.QMainWindow()
            self.LicenceUi = Ui_LicenceWindow()
            self.LicenceUi.setupUi(self.window)
            self.window.show()
            self.splash.hide()
        else:
            self.window = QtWidgets.QMainWindow()
            self.PosUi = Ui_PosWindow()
            self.PosUi.setupUi(self.window)
            self.window.show()
            self.splash.hide()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
