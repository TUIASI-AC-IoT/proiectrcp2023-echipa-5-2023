# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerPbixBc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(547, 430)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_address = QLabel(Form)
        self.label_address.setObjectName(u"label_address")

        self.verticalLayout.addWidget(self.label_address)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.input_text_address = QLineEdit(Form)
        self.input_text_address.setObjectName(u"input_text_address")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_text_address.sizePolicy().hasHeightForWidth())
        self.input_text_address.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.input_text_address)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_4.setStretch(0, 40)
        self.horizontalLayout_4.setStretch(1, 20)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_rootfolder = QLabel(Form)
        self.label_rootfolder.setObjectName(u"label_rootfolder")

        self.verticalLayout.addWidget(self.label_rootfolder)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.input_text_rootfolder = QLineEdit(Form)
        self.input_text_rootfolder.setObjectName(u"input_text_rootfolder")
        sizePolicy.setHeightForWidth(self.input_text_rootfolder.sizePolicy().hasHeightForWidth())
        self.input_text_rootfolder.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.input_text_rootfolder)

        self.button_browse = QPushButton(Form)
        self.button_browse.setObjectName(u"button_browse")

        self.horizontalLayout_5.addWidget(self.button_browse)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_5.setStretch(0, 40)
        self.horizontalLayout_5.setStretch(1, 10)
        self.horizontalLayout_5.setStretch(2, 10)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.button_start = QPushButton(Form)
        self.button_start.setObjectName(u"button_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.button_start)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 10)
        self.verticalLayout.setStretch(5, 10)
        self.verticalLayout.setStretch(6, 10)
        self.verticalLayout.setStretch(7, 10)
        self.verticalLayout.setStretch(8, 10)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_address.setText(QCoreApplication.translate("Form", u"Address", None))
        self.label_rootfolder.setText(QCoreApplication.translate("Form", u"Root Folder", None))
        self.button_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.button_start.setText(QCoreApplication.translate("Form", u"Start", None))
    # retranslateUi

