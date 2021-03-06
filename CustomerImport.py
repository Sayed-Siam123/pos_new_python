# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CustomerImport.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

from ModelObject import ModelObject
from api_provider import ApiProvider
from constant import db_path
from db_provider import DBProvider
from HelperClass import LoadingGif

API = ApiProvider()
DB = DBProvider()


class Ui_CustomerWindow(object):

    def setupUi(self, CustomerWindow):
        CustomerWindow.setObjectName("CustomerWindow")
        CustomerWindow.resize(800, 674)
        self.centralwidget = QtWidgets.QWidget(CustomerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_cus_import = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_cus_import.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_cus_import.setObjectName("pushButton_cus_import")

        # Button event START

        # TODO:: Customer Import Button Event

        self.pushButton_cus_import.clicked.connect(self.customer_import_btn_click)

        # Button event END

        self.gridLayout_2.addWidget(self.pushButton_cus_import, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(494, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.treeWidget_cus_import = QtWidgets.QTreeWidget(self.frame_6)
        self.treeWidget_cus_import.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.treeWidget_cus_import.setAlternatingRowColors(True)
        self.treeWidget_cus_import.setObjectName("treeWidget_cus_import")
        self.gridLayout_4.addWidget(self.treeWidget_cus_import, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_6, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.lineEdit_username = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout_6.addWidget(self.lineEdit_username)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.lineEdit_firstname = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_firstname.setObjectName("lineEdit_firstname")
        self.verticalLayout_5.addWidget(self.lineEdit_firstname)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.lineEdit_lastname = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.verticalLayout_4.addWidget(self.lineEdit_lastname)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.lineEdit_emailField = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_emailField.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_emailField.setObjectName("lineEdit_emailField")
        self.verticalLayout_7.addWidget(self.lineEdit_emailField)
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.lineEdit_contactField = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_contactField.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_contactField.setObjectName("lineEdit_contactField")
        self.verticalLayout_7.addWidget(self.lineEdit_contactField)
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.textEdit_addressField = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_addressField.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_addressField.setTabChangesFocus(True)
        self.textEdit_addressField.setObjectName("textEdit_addressField")
        self.verticalLayout_7.addWidget(self.textEdit_addressField)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_submit_cus_import = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_submit_cus_import.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_submit_cus_import.setObjectName("pushButton_submit_cus_import")

        # Button event START

        # TODO:: Customer create submit Button Event

        self.pushButton_submit_cus_import.clicked.connect(self.submit)

        # Button event END

        self.horizontalLayout.addWidget(self.pushButton_submit_cus_import)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.gridLayout_3.addWidget(self.frame_7, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        CustomerWindow.setCentralWidget(self.centralwidget)
        self.menuBar_cus_Import = QtWidgets.QMenuBar(CustomerWindow)
        self.menuBar_cus_Import.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar_cus_Import.setNativeMenuBar(False)
        self.menuBar_cus_Import.setObjectName("menuBar_cus_Import")
        self.menu_Options = QtWidgets.QMenu(self.menuBar_cus_Import)
        self.menu_Options.setObjectName("menu_Options")
        CustomerWindow.setMenuBar(self.menuBar_cus_Import)
        self.actionPOS_Terminal_cus_import = QtWidgets.QAction(CustomerWindow)
        self.actionPOS_Terminal_cus_import.setObjectName("actionPOS_Terminal_cus_import")
        self.actionProduct_Import_cus_import = QtWidgets.QAction(CustomerWindow)
        self.actionProduct_Import_cus_import.setObjectName("actionProduct_Import_cus_import")
        self.actionSettings = QtWidgets.QAction(CustomerWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionHelp = QtWidgets.QAction(CustomerWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtWidgets.QAction(CustomerWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(CustomerWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menu_Options.addAction(self.actionPOS_Terminal_cus_import)
        self.menu_Options.addAction(self.actionProduct_Import_cus_import)
        self.menu_Options.addSeparator()
        self.menu_Options.addAction(self.actionSettings)
        self.menu_Options.addAction(self.actionHelp)
        self.menu_Options.addSeparator()
        self.menu_Options.addAction(self.actionExit_2)
        self.menuBar_cus_Import.addAction(self.menu_Options.menuAction())

        self.retranslateUi(CustomerWindow)
        QtCore.QMetaObject.connectSlotsByName(CustomerWindow)
        CustomerWindow.setTabOrder(self.pushButton_cus_import, self.treeWidget_cus_import)
        CustomerWindow.setTabOrder(self.treeWidget_cus_import, self.lineEdit_emailField)
        CustomerWindow.setTabOrder(self.lineEdit_emailField, self.lineEdit_contactField)
        CustomerWindow.setTabOrder(self.lineEdit_contactField, self.textEdit_addressField)
        CustomerWindow.setTabOrder(self.textEdit_addressField, self.pushButton_submit_cus_import)

    def retranslateUi(self, CustomerWindow):
        _translate = QtCore.QCoreApplication.translate
        CustomerWindow.setWindowTitle(_translate("CustomerWindow", "Customer Import"))
        self.label_2.setText(_translate("CustomerWindow", "Customer Import"))
        self.pushButton_cus_import.setToolTip(_translate("CustomerWindow", "Import Customer (I/i)"))
        self.pushButton_cus_import.setText(_translate("CustomerWindow", "Import customer from internet"))
        self.pushButton_cus_import.setShortcut(_translate("CustomerWindow", "I"))
        self.treeWidget_cus_import.headerItem().setText(0, _translate("CustomerWindow", "Customer ID"))
        self.treeWidget_cus_import.headerItem().setText(1, _translate("CustomerWindow", "Customer Name"))
        self.treeWidget_cus_import.headerItem().setText(2, _translate("CustomerWindow", "Email"))
        self.treeWidget_cus_import.headerItem().setText(3, _translate("CustomerWindow", "Phone"))
        self.treeWidget_cus_import.headerItem().setText(4, _translate("CustomerWindow", "Address"))
        __sortingEnabled = self.treeWidget_cus_import.isSortingEnabled()
        self.treeWidget_cus_import.setSortingEnabled(False)
        self.treeWidget_cus_import.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("CustomerWindow", "Username"))
        self.lineEdit_username.setPlaceholderText(_translate("CustomerWindow", "username1002"))
        self.label_3.setText(_translate("CustomerWindow", "First Name"))
        self.lineEdit_firstname.setPlaceholderText(_translate("CustomerWindow", "Fred"))
        self.label_7.setText(_translate("CustomerWindow", "Last Name"))
        self.lineEdit_lastname.setPlaceholderText(_translate("CustomerWindow", "Nerks"))
        self.label_4.setText(_translate("CustomerWindow", "Email"))
        self.lineEdit_emailField.setPlaceholderText(_translate("CustomerWindow", "fred@gmail.com"))
        self.label_5.setText(_translate("CustomerWindow", "Contact Number"))
        self.lineEdit_contactField.setPlaceholderText(_translate("CustomerWindow", "+880"))
        self.label_6.setText(_translate("CustomerWindow", "Address"))
        self.pushButton_submit_cus_import.setToolTip(_translate("CustomerWindow", "Submit (S)"))
        self.pushButton_submit_cus_import.setText(_translate("CustomerWindow", "Submit"))
        self.pushButton_submit_cus_import.setShortcut(_translate("CustomerWindow", "S"))
        self.label.setText(_translate("CustomerWindow", "?? Bit Byte Technology"))
        self.menu_Options.setTitle(_translate("CustomerWindow", "Options"))
        self.actionPOS_Terminal_cus_import.setText(_translate("CustomerWindow", "POS Terminal"))
        self.actionPOS_Terminal_cus_import.setStatusTip(_translate("CustomerWindow", "POS Terminal"))
        self.actionPOS_Terminal_cus_import.setWhatsThis(_translate("CustomerWindow", "POS Terminal"))
        self.actionProduct_Import_cus_import.setText(_translate("CustomerWindow", "Product Import"))
        self.actionSettings.setText(_translate("CustomerWindow", "Settings"))
        self.actionHelp.setText(_translate("CustomerWindow", "Help"))
        self.actionExit.setText(_translate("CustomerWindow", "Exit"))
        self.actionExit_2.setText(_translate("CustomerWindow", "Exit"))
        self.customerTableDataFetch()

    def customer_import_btn_click(self):
        print("Customer import clicked!")
        self.w = LoadingGif()
        self.w.show()
        timer = QTimer()
        data = API.getCustomer()
        DB.PUSHDB_CUSTOMER(db_path+"POS.db", data)
        self.customerTableDataFetch()
        timer.singleShot(3000, self.nextWork)

    def nextWork(self):
        print("Printed after 4 secs")
        self.w.stopAnimation()
        self.w.pop_up("Customer import successfull")
        # self.openWindow()

    def submit(self):
        print("SUBMIT DATA")
        # me = ModelObject()
        # me.name = "Onur"
        # me.age = 35
        # me.dog = ModelObject()
        # me.dog.name = "Apollo"
        #
        # print(me.toJSON())

        user = ModelObject()
        user.billing = ModelObject()
        user.shipping = ModelObject()

        user.email = self.lineEdit_emailField.text()
        user.first_name = self.lineEdit_firstname.text()
        user.last_name = self.lineEdit_lastname.text()
        user.username = self.lineEdit_username.text()

        user.billing.first_name = self.lineEdit_firstname.text()
        user.billing.last_name = self.lineEdit_lastname.text()
        user.billing.company = "N/A"
        user.billing.address_1 = "969 Market"
        user.billing.address_2 = ""
        user.billing.city = "San Francisco"
        user.billing.state = "CA"
        user.billing.postcode = "94103"
        user.billing.country = "US"
        user.billing.email = self.lineEdit_emailField.text()
        user.billing.phone = self.lineEdit_contactField.text()

        user.shipping.first_name = self.lineEdit_firstname.text()
        user.shipping.last_name = self.lineEdit_lastname.text()
        user.shipping.company = "N/A"
        user.shipping.address_1 = "969 Market"
        user.shipping.address_2 = ""
        user.shipping.city = "San Francisco"
        user.shipping.state = "CA"
        user.shipping.postcode = "94103"
        user.shipping.country = "US"
        user.shipping.email = self.lineEdit_emailField.text()
        user.shipping.phone = self.lineEdit_contactField.text()

        if self.lineEdit_contactField.text() == "" or self.lineEdit_firstname.text() == "":
            print("NULL")
        else:
            DB.updateCustomerStatus("../wenv/db/POS.db", "TRUE")
            API.createUser(user.toJSON())
            print(str(user.toJSON()))

    def customerTableDataFetch(self):
        _translate = QtCore.QCoreApplication.translate
        print("Initial")
        print("Here it goes from outside")
        datas = DB.getALlCustomer(db_path+"POS.db")
        #print(len(datas))
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_cus_import)
        # self.treeWidget_cus_import.topLevelItem(0).setText(0, _translate("CustomerWindow", "ddd"))
        # self.treeWidget_cus_import.topLevelItem(0).setText(1, _translate("CustomerWindow", "ssss"))
        # self.treeWidget_cus_import.topLevelItem(0).setText(2, _translate("CustomerWindow", "sss"))
        # self.treeWidget_cus_import.topLevelItem(0).setText(3, _translate("CustomerWindow", "sss"))
        # self.treeWidget_cus_import.topLevelItem(0).setText(4, _translate("CustomerWindow", "sss"))
        if(datas != 0):
            for i in range(len(datas)):
                item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_cus_import)

                self.treeWidget_cus_import.topLevelItem(i).setText(0, _translate("CustomerWindow", str(datas[i]["id"])))
                self.treeWidget_cus_import.topLevelItem(i).setText(1, _translate("CustomerWindow", str(datas[i]["first_name"] + " " + datas[0]["last_name"])))
                self.treeWidget_cus_import.topLevelItem(i).setText(2, _translate("CustomerWindow", str(datas[i]["email"])))
                self.treeWidget_cus_import.topLevelItem(i).setText(3, _translate("CustomerWindow", str(datas[i]["billing"]["phone"])))
                self.treeWidget_cus_import.topLevelItem(i).setText(4, _translate("CustomerWindow", str(datas[i]["billing"]["address_1"])))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CustomerWindow = QtWidgets.QMainWindow()
    ui = Ui_CustomerWindow()
    ui.setupUi(CustomerWindow)
    CustomerWindow.show()
    sys.exit(app.exec_())
