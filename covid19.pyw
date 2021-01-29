# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covid19.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
import sys
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(295, 358)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button.setEnabled(True)
        self.Button.setObjectName("Button")
        self.horizontalLayout.addWidget(self.Button)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 281, 231))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 60, 271, 213))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblinfo = QtWidgets.QLabel(self.widget)
        self.lblinfo.setText("")
        self.lblinfo.setTextFormat(QtCore.Qt.AutoText)
        self.lblinfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblinfo.setObjectName("lblinfo")
        self.verticalLayout_3.addWidget(self.lblinfo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblcase = QtWidgets.QLabel(self.widget)
        self.lblcase.setText("")
        self.lblcase.setIndent(-1)
        self.lblcase.setObjectName("lblcase")
        self.verticalLayout.addWidget(self.lblcase)
        self.lbltocase = QtWidgets.QLabel(self.widget)
        self.lbltocase.setText("")
        self.lbltocase.setObjectName("lbltocase")
        self.verticalLayout.addWidget(self.lbltocase)
        self.lbldeath = QtWidgets.QLabel(self.widget)
        self.lbldeath.setText("")
        self.lbldeath.setObjectName("lbldeath")
        self.verticalLayout.addWidget(self.lbldeath)
        self.lbltodeath = QtWidgets.QLabel(self.widget)
        self.lbltodeath.setText("")
        self.lbltodeath.setObjectName("lbltodeath")
        self.verticalLayout.addWidget(self.lbltodeath)
        self.lblrecover = QtWidgets.QLabel(self.widget)
        self.lblrecover.setText("")
        self.lblrecover.setObjectName("lblrecover")
        self.verticalLayout.addWidget(self.lblrecover)
        self.lbltest = QtWidgets.QLabel(self.widget)
        self.lbltest.setText("")
        self.lbltest.setObjectName("lbltest")
        self.verticalLayout.addWidget(self.lbltest)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblcase1 = QtWidgets.QLabel(self.widget)
        self.lblcase1.setText("")
        self.lblcase1.setObjectName("lblcase1")
        self.verticalLayout_2.addWidget(self.lblcase1)
        self.lbltocase1 = QtWidgets.QLabel(self.widget)
        self.lbltocase1.setText("")
        self.lbltocase1.setObjectName("lbltocase1")
        self.verticalLayout_2.addWidget(self.lbltocase1)
        self.lbldeath1 = QtWidgets.QLabel(self.widget)
        self.lbldeath1.setText("")
        self.lbldeath1.setObjectName("lbldeath1")
        self.verticalLayout_2.addWidget(self.lbldeath1)
        self.lbltodeath1 = QtWidgets.QLabel(self.widget)
        self.lbltodeath1.setText("")
        self.lbltodeath1.setObjectName("lbltodeath1")
        self.verticalLayout_2.addWidget(self.lbltodeath1)
        self.lblrecover1 = QtWidgets.QLabel(self.widget)
        self.lblrecover1.setText("")
        self.lblrecover1.setObjectName("lblrecover1")
        self.verticalLayout_2.addWidget(self.lblrecover1)
        self.lbltest1 = QtWidgets.QLabel(self.widget)
        self.lbltest1.setText("")
        self.lbltest1.setObjectName("lbltest1")
        self.verticalLayout_2.addWidget(self.lbltest1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        icon = QtGui.QIcon("covid19.png")
        MainWindow.setWindowIcon(icon)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        countries = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
        source = json.loads(countries.content)
        list_ = []
        for coun in source:
            list_.append(coun["country"])
            
        self.comboBox.addItems(list_)

        self.Button.clicked.connect(self.result_)
        
    def result_(self):
        content = self.comboBox.currentText()
        countries = requests.get("https://coronavirus-19-api.herokuapp.com/countries/"+content)
        data = json.loads(countries.content)
        self.lblinfo.setText("Information "+ str(data['country']) +" COVID-19")
        self.lblcase1.setText(str(data['cases']))
        self.lbltocase1.setText(str(data['todayCases']))
        self.lbldeath1.setText(str(data['deaths']))
        self.lbltodeath1.setText(str(data['todayDeaths']))
        self.lblrecover1.setText(str(data['recovered']))
        self.lbltest1.setText(str(data['totalTests']))
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Country:"))
        self.Button.setText(_translate("MainWindow", "Enter"))
        self.lblcase.setText(_translate("MainWindow", "     Cases:"))
        self.lbltocase.setText(_translate("MainWindow", "     Today Cases:"))
        self.lbldeath.setText(_translate("MainWindow", "     Deaths:"))
        self.lbltodeath.setText(_translate("MainWindow", "     Today Deaths:"))
        self.lblrecover.setText(_translate("MainWindow", "     Recovered:"))
        self.lbltest.setText(_translate("MainWindow", "     Total Tests:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
