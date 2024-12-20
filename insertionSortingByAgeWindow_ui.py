# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'insertionSortingByAgeWindow.ui'
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

class Ui_insertionSortingByAgeWindow(object):
    def setupUi(self, insertionSortingByAgeWindow):
        if not insertionSortingByAgeWindow.objectName():
            insertionSortingByAgeWindow.setObjectName(u"insertionSortingByAgeWindow")
        insertionSortingByAgeWindow.resize(400, 326)
        self.tableView = QTableView(insertionSortingByAgeWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 381, 281))
        self.pushButton = QPushButton(insertionSortingByAgeWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 290, 100, 32))

        self.retranslateUi(insertionSortingByAgeWindow)

        QMetaObject.connectSlotsByName(insertionSortingByAgeWindow)
    # setupUi

    def retranslateUi(self, insertionSortingByAgeWindow):
        insertionSortingByAgeWindow.setWindowTitle(QCoreApplication.translate("insertionSortingByAgeWindow", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("insertionSortingByAgeWindow", u"\ub0b4\ub9bc\ucc28\uc21c \uc815\ub82c", None))
    # retranslateUi

