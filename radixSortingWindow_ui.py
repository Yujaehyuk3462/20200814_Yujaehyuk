# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radixSortingWindow.ui'
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

class Ui_radixSortingWindow(object):
    def setupUi(self, radixSortingWindow):
        if not radixSortingWindow.objectName():
            radixSortingWindow.setObjectName(u"radixSortingWindow")
        radixSortingWindow.resize(400, 326)
        self.tableView = QTableView(radixSortingWindow)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 381, 281))
        self.pushButton = QPushButton(radixSortingWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 290, 100, 32))

        self.retranslateUi(radixSortingWindow)

        QMetaObject.connectSlotsByName(radixSortingWindow)
    # setupUi

    def retranslateUi(self, radixSortingWindow):
        radixSortingWindow.setWindowTitle(QCoreApplication.translate("radixSortingWindow", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("radixSortingWindow", u"\ub0b4\ub9bc\ucc28\uc21c \uc815\ub82c", None))
    # retranslateUi

