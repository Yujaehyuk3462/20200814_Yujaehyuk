# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentProgramMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(308, 418)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_selectionSort = QPushButton(self.centralwidget)
        self.pushButton_selectionSort.setObjectName(u"pushButton_selectionSort")
        self.pushButton_selectionSort.setGeometry(QRect(90, 60, 100, 32))
        self.pushButton_insertionSort = QPushButton(self.centralwidget)
        self.pushButton_insertionSort.setObjectName(u"pushButton_insertionSort")
        self.pushButton_insertionSort.setGeometry(QRect(90, 110, 100, 32))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 210, 100, 32))
        self.pushButton_quickSort = QPushButton(self.centralwidget)
        self.pushButton_quickSort.setObjectName(u"pushButton_quickSort")
        self.pushButton_quickSort.setGeometry(QRect(90, 160, 100, 32))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 260, 100, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 308, 36))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_selectionSort.clicked.connect(MainWindow.selectionSort_clicked)
        self.pushButton_insertionSort.clicked.connect(MainWindow.insertionSort_clicked)
        self.pushButton_quickSort.clicked.connect(MainWindow.quickSort_clicked)
        self.pushButton_3.clicked.connect(MainWindow.radixSort_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_selectionSort.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\uc815\ub82c", None))
        self.pushButton_insertionSort.setText(QCoreApplication.translate("MainWindow", u"\uc0bd\uc785\uc815\ub82c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc218\uc815\ub82c(\uc131\uc801)", None))
        self.pushButton_quickSort.setText(QCoreApplication.translate("MainWindow", u"\ud035\uc815\ub82c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
    # retranslateUi

