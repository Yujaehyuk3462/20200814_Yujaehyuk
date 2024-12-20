# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quickSortingByAgeWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_quickSortingByAgeWindow(object):
    def setupUi(self, quickSortingByAgeWindow):
        if not quickSortingByAgeWindow.objectName():
            quickSortingByAgeWindow.setObjectName(u"quickSortingByAgeWindow")
        quickSortingByAgeWindow.resize(400, 326)
        self.tableView = QTableView(quickSortingByAgeWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 381, 281))
        self.pushButton = QPushButton(quickSortingByAgeWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 290, 100, 32))

        self.retranslateUi(quickSortingByAgeWindow)

        QMetaObject.connectSlotsByName(quickSortingByAgeWindow)
    # setupUi

    def retranslateUi(self, quickSortingByAgeWindow):
        quickSortingByAgeWindow.setWindowTitle(QCoreApplication.translate("quickSortingByAgeWindow", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("quickSortingByAgeWindow", u"\ub0b4\ub9bc\ucc28\uc21c \uc815\ub82c", None))
    # retranslateUi

