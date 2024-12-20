# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectionSortingWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_selectionSortingWindow(object):
    def setupUi(self, selectionSortingWindow):
        if not selectionSortingWindow.objectName():
            selectionSortingWindow.setObjectName(u"selectionSortingWindow")
        selectionSortingWindow.resize(228, 219)
        self.pushButton_sortingName = QPushButton(selectionSortingWindow)
        self.pushButton_sortingName.setObjectName(u"pushButton_sortingName")
        self.pushButton_sortingName.setGeometry(QRect(60, 30, 100, 32))
        self.pushButton_sortingAge = QPushButton(selectionSortingWindow)
        self.pushButton_sortingAge.setObjectName(u"pushButton_sortingAge")
        self.pushButton_sortingAge.setGeometry(QRect(60, 80, 100, 32))
        self.pushButton_sortingGrade = QPushButton(selectionSortingWindow)
        self.pushButton_sortingGrade.setObjectName(u"pushButton_sortingGrade")
        self.pushButton_sortingGrade.setGeometry(QRect(60, 130, 100, 32))

        self.retranslateUi(selectionSortingWindow)
        self.pushButton_sortingName.clicked.connect(selectionSortingWindow.selectionSortingByName)
        self.pushButton_sortingAge.clicked.connect(selectionSortingWindow.selectionSortingByAge)
        self.pushButton_sortingGrade.clicked.connect(selectionSortingWindow.selectionSortingByGrade)

        QMetaObject.connectSlotsByName(selectionSortingWindow)
    # setupUi

    def retranslateUi(self, selectionSortingWindow):
        selectionSortingWindow.setWindowTitle(QCoreApplication.translate("selectionSortingWindow", u"Form", None))
        self.pushButton_sortingName.setText(QCoreApplication.translate("selectionSortingWindow", u"\uc774\ub984 \uc815\ub82c", None))
        self.pushButton_sortingAge.setText(QCoreApplication.translate("selectionSortingWindow", u"\ub098\uc774 \uc815\ub82c", None))
        self.pushButton_sortingGrade.setText(QCoreApplication.translate("selectionSortingWindow", u"\uc131\uc801 \uc815\ub82c", None))
    # retranslateUi

