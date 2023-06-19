from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

         # кнопка для возвращения на предыдущую форму 

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 600, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        
        # кнопка для вызова процедуры для подсчета общей стоимости заказа

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 485, 200, 23))
        self.pushButton_5.setObjectName("pushButton_5")

         # таблица
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 600, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)

        self.tableWidget.setColumnWidth(0,150)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

         # заголовки

        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(20, 330, 200, 30))
        self.label_0.setObjectName("label")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 330, 200, 30))
        self.label_8.setObjectName("label")

         # поля ввода для добавления данных в бд
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 405, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 380, 100, 16))
        self.label.setObjectName("label")

         # кнопка для добавления данных в бд
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 445, 111, 23))
        self.pushButton.setObjectName("pushButton")

        # кнопка для удаления данных из бд
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 445, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        # поле для ввода номера для удаления данных из бд
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 405, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 380, 61, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Карточки заказов"))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код карточки заказа"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Стоимость"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Код клиента"))

        self.label_0.setText(_translate("MainWindow", "Добавление карточки"))
        self.label_0.setFont(QFont('Arial', 14))

        self.label_8.setText(_translate("MainWindow", "Удаление карточки"))
        self.label_8.setFont(QFont('Arial', 14))

        self.label.setText(_translate("MainWindow", "Код клиента"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))

        self.label_2.setText(_translate("MainWindow", "Код"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_4.setText(_translate("MainWindow", "Назад"))
        self.pushButton_5.setText(_translate("MainWindow", "Расчитать общую стоимость заказа"))
        
