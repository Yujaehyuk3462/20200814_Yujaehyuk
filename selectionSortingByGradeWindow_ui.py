# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectionSortingByGradeWindow.ui'
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

class Ui_selectionSortingByGradeWindow(object):
    def setupUi(self, selectionSortingByGradeWindow):
        if not selectionSortingByGradeWindow.objectName():
            selectionSortingByGradeWindow.setObjectName(u"selectionSortingByGradeWindow")
        selectionSortingByGradeWindow.resize(400, 326)
        self.tableView = QTableView(selectionSortingByGradeWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 381, 281))
        self.pushButton = QPushButton(selectionSortingByGradeWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 290, 100, 32))

        self.retranslateUi(selectionSortingByGradeWindow)

        QMetaObject.connectSlotsByName(selectionSortingByGradeWindow)
    # setupUi

    def retranslateUi(self, selectionSortingByGradeWindow):
        selectionSortingByGradeWindow.setWindowTitle(QCoreApplication.translate("selectionSortingByGradeWindow", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("selectionSortingByGradeWindow", u"\ub0b4\ub9bc\ucc28\uc21c \uc815\ub82c", None))
    # retranslateUi

