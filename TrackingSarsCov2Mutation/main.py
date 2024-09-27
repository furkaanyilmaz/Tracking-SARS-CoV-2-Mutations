
from operator import le
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QSizeGrip,QMessageBox
from PyQt5.QtCore import Qt,QEasingCurve, QPropertyAnimation,QSize,pyqtSignal
from PyQt5 import QtGui, QtCore, QtWidgets
#from PyQt5.QtWebEngineWidgets import QWebEngineView
from click import confirm
import requests
from requests.structures import CaseInsensitiveDict
from pyqtgraph import PlotWidget, plot,PlotItem,PlotWidget
from main_ui import Ui_MainWindow
from database import database
import smtplib
import ssl
from random import randint
from configparser import ConfigParser

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        # apply_stylesheet(app,theme='dark_cyan.xml')
        QSizeGrip(self.ui.size_window)

        self.parser = ConfigParser()
        self.parser.read("config.ini")

        self.database = database(self.parser["mysql"]["host"],
                                 self.parser["mysql"]["user"],
                                 self.parser["mysql"]["password"])

        self.database.create()

        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_button.clicked.connect(lambda: self.close())
        self.ui.restore_button.clicked.connect(lambda: self.restore_or_maximize_window())
        self.play_gif()

        self.ui.login_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_page))
        self.ui.sign_in_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.register_page))
        self.ui.logout_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.login_main_page))
        self.ui.login_button_2.clicked.connect(self.check_user)
        self.ui.sign_in_button_2.clicked.connect(self.check_blanks)
        self.ui.login_button_4.clicked.connect(self.confirm_stopAnimation )
        self.ui.search_button.clicked.connect(self.search)
        self.ui.add_mutation_save_button.clicked.connect(self.add_mutation)
        self.ui.search_mutation_3.clicked.connect(self.add_mutation_succesfully_end)
        self.ui.search_mutation.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search_page))
        self.ui.add_mutation_save_button_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_mutation_page))
        self.ui.new_mutation_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_mutation_page))
        self.ui.search_mutation_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search_page))

        self.ui.tableWidget.setColumnWidth(0,100)
        self.ui.tableWidget.setColumnWidth(1,200)
        self.ui.tableWidget.setColumnWidth(2,200)
        self.ui.tableWidget.setColumnWidth(3,185)
        self.ui.tableWidget.setColumnWidth(4,185)
        self.ui.login_button_3.clicked.connect(self.check_confirmation_code)


        def moveWindow(e):
            if self.isMaximized()==False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos()+ e.globalPos()-self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.navbar_frame.mouseMoveEvent = moveWindow


    def check_confirmation_code(self):
        confirmation_code = self.ui.confirmation_line.text()
        if str(confirmation_code) == str(self.confirmation_code):
            self.ui.stackedWidget.setCurrentWidget(self.ui.register_confirmation_page)
            self.database.update_confirmation(self.email)
            self.play_confirm_gif()
        else:   
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('confirmation codes do not match.')
            msg.setWindowTitle("Error")
            msg.exec_()


    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row+1)
        col = 0
        for item in row_data:
            cell = QtWidgets.QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            cell.setForeground(QtGui.QColor(255,255,255))
            cell.setTextAlignment(Qt.AlignHCenter)
            col += 1


    def add_mutation(self):
        val1 = self.ui.voc_vol.text()
        val2 = self.ui.effect_vaccine.text()
        val3 = self.ui.Infectiousness.text()
        val4 = self.ui.death_rate.text()
        val5 = self.ui.antibody.text()
        val6 = self.ui.mutation_name.text()
        val7 = self.ui.doi_number.text()
        self.database.add_mutation(val6,val1,val2,val3,val4,val5,val7)
        self.add_mutation_movie = QtGui.QMovie(u"other_icons/add_new_mutation.gif")
        self.ui.label_6.setMovie(self.add_mutation_movie)
        self.add_mutation_movie.start()
        self.ui.stackedWidget.setCurrentWidget(self.ui.mutation_added)


    def check_user(self):
        email = self.ui.login_email.text()
        passwd = self.ui.login_password.text()
        result = self.database.get_user(email,passwd)
        if result:
             self.ui.stackedWidget.setCurrentWidget(self.ui.search_page)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('username or password is incorrect.')
            msg.setWindowTitle("Error")
            msg.exec_()


    def search(self):
        text = self.ui.search_line_edit.text()
        result = self.database.search_mutation(text)
        if len(result) == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.not_found_mutation)

        else:
            while (self.ui.tableWidget.rowCount() > 0): 
                self.ui.tableWidget.removeRow(0)
            for i in result:
                self.addTableRow(self.ui.tableWidget, i)
            self.ui.stackedWidget.setCurrentWidget(self.ui.found_mutation)

    def add_mutation_succesfully_end(self):
        self.add_mutation_movie.stop()
        self.ui.stackedWidget.setCurrentWidget(self.ui.search_page)

    def check_blanks(self):
        name = self.ui.signin_name.text()
        surname = self.ui.signin_surname.text()
        email = self.ui.signin_email.text()
        passwd = self.ui.signin_password.text()
        re_passwd = self.ui.signin_confirm.text()
        confirmation_code = randint(100000,999999)
        if name != "" and surname != "" and email != "" and passwd != "" and re_passwd != "":
            if passwd == re_passwd:
                if "@" in email:
                    self.database.add_user(email,passwd,name,surname,confirmation_code)
                    self.ui.stackedWidget.setCurrentWidget(self.ui.register_page_confirmation)
                    self.send_mail(email,confirmation_code,name,surname)
                    self.confirmation_code = confirmation_code
                    self.email= email
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText('email address is invalid')
                    msg.setWindowTitle("Error")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('password and confirmation password must be the same.')
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('check for spaces')
            msg.setWindowTitle("Error")
            msg.exec_()

    def play_gif(self):
        self.movie = QtGui.QMovie(u"other_icons/giphy.gif")
        self.ui.login_main_gif.setMovie(self.movie)
        self.startAnimation()

    def startAnimation(self):   
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()

    def play_confirm_gif(self):
        self.confirm_gif = QtGui.QMovie(u"other_icons/comfrim_giphy.gif")
        self.ui.confirmation_gif.setMovie(self.confirm_gif)
        self.confirm_startAnimation()

    def confirm_startAnimation(self):   
        self.confirm_gif.start()

    def confirm_stopAnimation(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)
        self.confirm_gif.stop()


    def send_mail(self,email,code,name,surname):
        port = 587  

        smtp_server = "smtp-mail.outlook.com"
        sender = self.parser["email"]["sender_email_address"]
        recipient = email
        sender_password = self.parser["email"]["sender_email_password"]

        message = """

        Dear {} {},

        Your verification code is given below

        Verification Code : {}""".format(name,surname,code)

        SSL_context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=SSL_context)
            server.login(sender, sender_password)
            server.sendmail(sender, recipient, message)


    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
