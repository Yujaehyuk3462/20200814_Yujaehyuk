# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quickSortingByNameWindow.ui'
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

class Ui_quickSortingByNameWindow(object):
    def setupUi(self, quickSortingByNameWindow):
        if not quickSortingByNameWindow.objectName():
            quickSortingByNameWindow.setObjectName(u"quickSortingByNameWindow")
        quickSortingByNameWindow.resize(400, 326)
        self.tableView = QTableView(quickSortingByNameWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 381, 281))
        self.pushButton = QPushButton(quickSortingByNameWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 290, 100, 32))

        self.retranslateUi(quickSortingByNameWindow)

        QMetaObject.connectSlotsByName(quickSortingByNameWindow)
    # setupUi

    def retranslateUi(self, quickSortingByNameWindow):
        quickSortingByNameWindow.setWindowTitle(QCoreApplication.translate("quickSortingByNameWindow", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("quickSortingByNameWindow", u"\ub0b4\ub9bc\ucc28\uc21c \uc815\ub82c", None))
    # retranslateUi

