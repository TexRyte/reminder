# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reminder.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHeaderView,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 800)
        print(MainWindow.size())
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ScheduleWidget = QTableWidget(self.centralwidget)
        if (self.ScheduleWidget.columnCount() < 8):
            self.ScheduleWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.ScheduleWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ScheduleWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ScheduleWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ScheduleWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ScheduleWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ScheduleWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ScheduleWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ScheduleWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.ScheduleWidget.setObjectName(u"ScheduleWidget")
        self.ScheduleWidget.setGeometry(QRect(0, 0, 800, 800))
        font = QFont()
        font.setFamilies([u"Agu Display"])
        font.setPointSize(10)
        font.setBold(False)
        self.ScheduleWidget.setFont(font)
        self.ScheduleWidget.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: none grey none none")
        self.ScheduleWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.ScheduleWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.ScheduleWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ScheduleWidget.horizontalHeader().setDefaultSectionSize(100)
        self.InteractionBox = QGroupBox(self.centralwidget)
        self.InteractionBox.setObjectName(u"InteractionBox")
        self.InteractionBox.setGeometry(QRect(800, 0, 200, 800))
        self.InteractionBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"padding: 1px\n"
"")
        self.scrollArea = QScrollArea(self.InteractionBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 200, 700))
        self.scrollArea.setMinimumSize(QSize(200, 700))
        self.scrollArea.setStyleSheet(u"border-width: 0px;\n"
"border-style: hidden;\n"
"border-color: None None None grey;")
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 198, 698))
        self.InfoBox = QGroupBox(self.scrollAreaWidgetContents)
        self.InfoBox.setObjectName(u"InfoBox")
        self.InfoBox.setGeometry(QRect(0, 0, 200, 700))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QFrame(self.InteractionBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 700, 200, 1))
        self.line.setMinimumSize(QSize(200, 1))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: grey;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.ButtonsBox = QGroupBox(self.InteractionBox)
        self.ButtonsBox.setObjectName(u"ButtonsBox")
        self.ButtonsBox.setGeometry(QRect(0, 700, 200, 100))
        self.ButtonsBox.setMinimumSize(QSize(200, 100))
        self.ButtonsBox.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.pushButton_2 = QPushButton(self.ButtonsBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(25, 55, 150, 30))
        self.pushButton_2.setStyleSheet(u"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(0, 115, 191);\n"
"color: rgb(255, 255, 255);\n"
"font: bold;\n"
"")
        self.pushButton_3 = QPushButton(self.ButtonsBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(25, 15, 150, 30))
        self.pushButton_3.setStyleSheet(u"border-radius: 10px;\n"
"padding: 5px;\n"
"background-color: rgb(0, 115, 191);\n"
"color: rgb(255, 255, 255);\n"
"font: bold;\n"
"")
        self.scrollArea.raise_()
        self.ButtonsBox.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.InteractionBox.raise_()
        self.ScheduleWidget.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Reminder", None))
        ___qtablewidgetitem = self.ScheduleWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c/\u0412\u0440\u0435\u043c\u044f", None));
        ___qtablewidgetitem1 = self.ScheduleWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a", None));
        ___qtablewidgetitem2 = self.ScheduleWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a", None));
        ___qtablewidgetitem3 = self.ScheduleWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u0430", None));
        ___qtablewidgetitem4 = self.ScheduleWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0433", None));
        ___qtablewidgetitem5 = self.ScheduleWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u044f\u0442\u043d\u0438\u0446\u0430", None));
        ___qtablewidgetitem6 = self.ScheduleWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u0431\u0431\u043e\u0442\u0430", None));
        ___qtablewidgetitem7 = self.ScheduleWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435", None));
        self.InteractionBox.setTitle("")
        self.InfoBox.setTitle("")
        self.ButtonsBox.setTitle("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi
        

def Start():
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


Start()