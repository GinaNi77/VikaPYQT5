import sys
from PyQt5 import QtWidgets, QtSql
from getpass import getpass
from mysql.connector import connect, Error
from PyQt5.QtWidgets import QDialog, QApplication
import menu, customer_data, product_data, instwork_data, payment_data, order_menu, ordercard_data, order_data
import config, db_table, db_procedures, db_triggers, create_db
from datetime import date

class Main(QtWidgets.QMainWindow, menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def order_menu(self):
        self.tour_menu = OrderMenu()
        self.tour_menu.show()
        self.hide()

    def product_data(self):
        self.product_data = ProductData()
        self.product_data.show()
        self.hide()

    def customer_data(self):
        self.customer_data = CustomerData()
        self.customer_data.show()
        self.hide()   

    def instwork_data(self):
        self.instwork_data = InstworkData()
        self.instwork_data.show()
        self.hide()

    def payment_data(self):
        self.payment_data = PaymentData()
        self.payment_data.show()
        self.hide()

    def create_db(self):
        self.create_db = CreateDB()
        self.create_db.show()
        self.hide()

    def init(self):
        self.pushButton.clicked.connect(self.customer_data)
        self.pushButton_4.clicked.connect(self.order_menu)
        self.pushButton_2.clicked.connect(self.product_data)
        self.pushButton_5.clicked.connect(self.payment_data)
        self.pushButton_3.clicked.connect(self.instwork_data)
        self.pushButton_6.clicked.connect(self.create_db)

class OrderMenu(QtWidgets.QMainWindow, order_menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.ordercard_data)
        self.pushButton_2.clicked.connect(self.order_data)

    def order_data(self):
        self.order_data = OrderData()
        self.order_data.show()
        self.hide()

    def ordercard_data(self):
        self.ordercard_data = OrdercardData()
        self.ordercard_data.show()
        self.hide() 

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()
        self.init()
     
        
class CustomerData(QtWidgets.QMainWindow, customer_data.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
    
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from customer"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 4):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO customer (name, surname, phone) VALUES (%s, %s, %s)"
                insert_tuple = [(name, surname, phone)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from customer where idCustomer = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()
    
    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class ProductData(QtWidgets.QMainWindow, product_data.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete) 

    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from product"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 6):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        name = self.lineEdit.text()
        description = self.lineEdit_3.text()
        material = self.lineEdit_4.text()
        size = self.lineEdit_5.text()
        costProduct = self.lineEdit_6.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO product (name, description, material, size, costProduct) VALUES (%s, %s, %s, %s, %s)"
                insert_tuple = [(name, description, material, size, costProduct)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from product where idProduct = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb() 

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class OrderData(QtWidgets.QMainWindow, order_data.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)

    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from `order`"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        idOrderCard = self.lineEdit.text()
        idProduct = self.lineEdit_3.text()
        amount = self.lineEdit_4.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO `order` (idOrderCard, idProduct, amount) VALUES (%s, %s, %s)"
                insert_tuple = [(idOrderCard, idProduct, amount,)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from `order` where idOrder = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb() 

    def back(self):
        self.createDB = OrderMenu()
        self.createDB.show()
        self.hide()

class OrdercardData(QtWidgets.QMainWindow, ordercard_data.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_5.clicked.connect(self.cost_ordercard)
    
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from ordercard"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 3):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        idCustomer = self.lineEdit.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO ordercard (idCustomer) VALUES (%s)"
                insert_tuple = [(idCustomer,)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from ordercard where idOrderCard = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()
    
    def cost_ordercard(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            query = "call calculate_ordercard_cost()"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                self.showdb() 

    def back(self):
        self.createDB = OrderMenu()
        self.createDB.show()
        self.hide()

class PaymentData(QtWidgets.QMainWindow, payment_data.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        self.pushButton_5.clicked.connect(self.cost_payment) 
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from payment"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 4):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        paymentDate = self.lineEdit.text()
        idOrderCard = self.lineEdit_3.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO payment (paymentDate, idOrderCard) VALUES (%s, %s)"
                insert_tuple = [(paymentDate, idOrderCard)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from payment where idPayment = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def cost_payment(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            query = "call calculate_payment_cost()"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                self.showdb()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class InstworkData(QtWidgets.QMainWindow, instwork_data.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from installationwork"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 5):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        beginDate = self.lineEdit.text()
        endDate = self.lineEdit_3.text()
        idOrderCard = self.lineEdit_4.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO installationwork (beginDate, endDate, idOrderCard) VALUES (%s, %s, %s)"
                insert_tuple = [(beginDate, endDate, idOrderCard)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_4.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from installationwork where idInstallationWork = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class CreateDB(QtWidgets.QMainWindow, create_db.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        #назначаем действия по кнопкам
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.create_table)
        self.pushButton_2.clicked.connect(self.create_triggers)
        self.pushButton_3.clicked.connect(self.create_procedures)

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

    def create_table(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
        ) as connection:
            query = db_table.script
            with connection.cursor() as cursor:
                cursor.execute(query)

    def create_procedures(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database = config.db,
        ) as connection:
            query = db_procedures.procedures
            with connection.cursor() as cursor:
                cursor.execute(query)

    def create_triggers(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database = config.db,
        ) as connection:
            query = db_triggers.triggers
            with connection.cursor() as cursor:
                cursor.execute(query)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()

if __name__ == '__main__':
    main()
