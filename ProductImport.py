# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductImport.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProdWindow(object):
    def setupUi(self, ProdWindow):
        ProdWindow.setObjectName("ProdWindow")
        ProdWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ProdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_prod_import = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_prod_import.setMinimumSize(QtCore.QSize(220, 0))
        self.pushButton_prod_import.setMaximumSize(QtCore.QSize(220, 16777215))
        self.pushButton_prod_import.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_prod_import.setObjectName("pushButton_prod_import")
        self.horizontalLayout.addWidget(self.pushButton_prod_import)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.treeWidget_prod_import = QtWidgets.QTreeWidget(self.frame_3)
        self.treeWidget_prod_import.setAlternatingRowColors(True)
        self.treeWidget_prod_import.setObjectName("treeWidget_prod_import")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_prod_import)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_prod_import)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_prod_import)
        self.gridLayout_5.addWidget(self.treeWidget_prod_import, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        ProdWindow.setCentralWidget(self.centralwidget)
        self.menuBar_prod_import = QtWidgets.QMenuBar(ProdWindow)
        self.menuBar_prod_import.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar_prod_import.setNativeMenuBar(False)
        self.menuBar_prod_import.setObjectName("menuBar_prod_import")
        self.menuOptions = QtWidgets.QMenu(self.menuBar_prod_import)
        self.menuOptions.setObjectName("menuOptions")
        ProdWindow.setMenuBar(self.menuBar_prod_import)
        self.actionPOS_Terminal_prod_import = QtWidgets.QAction(ProdWindow)
        self.actionPOS_Terminal_prod_import.setObjectName("actionPOS_Terminal_prod_import")
        self.actionCustomer_Import_prod_import = QtWidgets.QAction(ProdWindow)
        self.actionCustomer_Import_prod_import.setObjectName("actionCustomer_Import_prod_import")
        self.actionSettings = QtWidgets.QAction(ProdWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionHelp = QtWidgets.QAction(ProdWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtWidgets.QAction(ProdWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuOptions.addAction(self.actionPOS_Terminal_prod_import)
        self.menuOptions.addAction(self.actionCustomer_Import_prod_import)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionSettings)
        self.menuOptions.addAction(self.actionHelp)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionExit)
        self.menuBar_prod_import.addAction(self.menuOptions.menuAction())

        self.retranslateUi(ProdWindow)
        QtCore.QMetaObject.connectSlotsByName(ProdWindow)

    def retranslateUi(self, ProdWindow):
        _translate = QtCore.QCoreApplication.translate
        ProdWindow.setWindowTitle(_translate("ProdWindow", "Product Import"))
        self.label.setText(_translate("ProdWindow", "Product Import"))
        self.pushButton_prod_import.setToolTip(_translate("ProdWindow", "Import product (I)"))
        self.pushButton_prod_import.setText(_translate("ProdWindow", "Import Product from Internet"))
        self.pushButton_prod_import.setShortcut(_translate("ProdWindow", "I"))
        self.treeWidget_prod_import.headerItem().setText(0, _translate("ProdWindow", "Product ID"))
        self.treeWidget_prod_import.headerItem().setText(1, _translate("ProdWindow", "Product Name"))
        self.treeWidget_prod_import.headerItem().setText(2, _translate("ProdWindow", "Quantity"))
        self.treeWidget_prod_import.headerItem().setText(3, _translate("ProdWindow", "Value"))
        self.treeWidget_prod_import.headerItem().setText(4, _translate("ProdWindow", "Availability"))
        __sortingEnabled = self.treeWidget_prod_import.isSortingEnabled()
        self.treeWidget_prod_import.setSortingEnabled(False)
        self.treeWidget_prod_import.topLevelItem(0).setText(0, _translate("ProdWindow", "1121313"))
        self.treeWidget_prod_import.topLevelItem(0).setText(1, _translate("ProdWindow", "A"))
        self.treeWidget_prod_import.topLevelItem(0).setText(2, _translate("ProdWindow", "10"))
        self.treeWidget_prod_import.topLevelItem(0).setText(3, _translate("ProdWindow", "100"))
        self.treeWidget_prod_import.topLevelItem(0).setText(4, _translate("ProdWindow", "Yes"))
        self.treeWidget_prod_import.topLevelItem(1).setText(0, _translate("ProdWindow", "1122323"))
        self.treeWidget_prod_import.topLevelItem(1).setText(1, _translate("ProdWindow", "B"))
        self.treeWidget_prod_import.topLevelItem(1).setText(2, _translate("ProdWindow", "20"))
        self.treeWidget_prod_import.topLevelItem(1).setText(3, _translate("ProdWindow", "250"))
        self.treeWidget_prod_import.topLevelItem(1).setText(4, _translate("ProdWindow", "Yes"))
        self.treeWidget_prod_import.topLevelItem(2).setText(0, _translate("ProdWindow", "1121324"))
        self.treeWidget_prod_import.topLevelItem(2).setText(1, _translate("ProdWindow", "C"))
        self.treeWidget_prod_import.topLevelItem(2).setText(2, _translate("ProdWindow", "0"))
        self.treeWidget_prod_import.topLevelItem(2).setText(3, _translate("ProdWindow", "200"))
        self.treeWidget_prod_import.topLevelItem(2).setText(4, _translate("ProdWindow", "No"))
        self.treeWidget_prod_import.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("ProdWindow", "?? Bit Byte Technology"))
        self.menuOptions.setTitle(_translate("ProdWindow", "Options"))
        self.actionPOS_Terminal_prod_import.setText(_translate("ProdWindow", "POS Terminal"))
        self.actionCustomer_Import_prod_import.setText(_translate("ProdWindow", "Customer Import"))
        self.actionSettings.setText(_translate("ProdWindow", "Settings"))
        self.actionHelp.setText(_translate("ProdWindow", "Help"))
        self.actionExit.setText(_translate("ProdWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProdWindow = QtWidgets.QMainWindow()
    ui = Ui_ProdWindow()
    ui.setupUi(ProdWindow)
    ProdWindow.show()
    sys.exit(app.exec_())
