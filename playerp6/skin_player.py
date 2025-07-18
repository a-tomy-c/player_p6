# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'skin_player.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_SkinPlayer(object):
    def setupUi(self, SkinPlayer):
        if not SkinPlayer.objectName():
            SkinPlayer.setObjectName(u"SkinPlayer")
        SkinPlayer.resize(512, 367)
        SkinPlayer.setStyleSheet(u"* {\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"QFrame {\n"
"	background-color: rgb(30, 30, 30);\n"
"}\n"
"QLabel {\n"
"	font: 9pt \"Segoe UI\";\n"
"	color: rgb(226, 226, 226);\n"
"}\n"
"QPushButton {\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	color: rgb(226, 226, 226);\n"
"	background-color: rgb(50, 52, 50);\n"
"}\n"
"QFrame #frame_video {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton::Pressed{\n"
"	background-color: rgb(10, 12, 10);\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(SkinPlayer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fm_video = QFrame(SkinPlayer)
        self.fm_video.setObjectName(u"fm_video")
        self.fm_video.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_video.setFrameShadow(QFrame.Shadow.Plain)

        self.verticalLayout.addWidget(self.fm_video)

        self.fm_control = QFrame(SkinPlayer)
        self.fm_control.setObjectName(u"fm_control")
        self.fm_control.setMaximumSize(QSize(16777215, 18))
        self.fm_control.setFrameShape(QFrame.Shape.NoFrame)
        self.fm_control.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.fm_control)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_play = QPushButton(self.fm_control)
        self.bt_play.setObjectName(u"bt_play")
        self.bt_play.setMinimumSize(QSize(26, 18))
        self.bt_play.setMaximumSize(QSize(26, 18))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        self.bt_play.setFont(font)

        self.horizontalLayout_3.addWidget(self.bt_play)

        self.sw = QStackedWidget(self.fm_control)
        self.sw.setObjectName(u"sw")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_2 = QHBoxLayout(self.page)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sld_tiempo = QSlider(self.page)
        self.sld_tiempo.setObjectName(u"sld_tiempo")
        self.sld_tiempo.setMinimumSize(QSize(0, 18))
        self.sld_tiempo.setMaximumSize(QSize(16777215, 18))
        self.sld_tiempo.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_tiempo)

        self.lb_time = QLabel(self.page)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setMinimumSize(QSize(52, 18))
        self.lb_time.setMaximumSize(QSize(52, 18))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.lb_time.setFont(font1)
        self.lb_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_time)

        self.sld_vol = QSlider(self.page)
        self.sld_vol.setObjectName(u"sld_vol")
        self.sld_vol.setMinimumSize(QSize(60, 18))
        self.sld_vol.setMaximumSize(QSize(60, 18))
        self.sld_vol.setMaximum(100)
        self.sld_vol.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.sld_vol)

        self.lb_vol = QLabel(self.page)
        self.lb_vol.setObjectName(u"lb_vol")
        self.lb_vol.setMinimumSize(QSize(20, 18))
        self.lb_vol.setMaximumSize(QSize(20, 18))
        self.lb_vol.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_vol)

        self.bt_stop = QPushButton(self.page)
        self.bt_stop.setObjectName(u"bt_stop")
        self.bt_stop.setMinimumSize(QSize(26, 18))
        self.bt_stop.setMaximumSize(QSize(26, 18))
        self.bt_stop.setFont(font)

        self.horizontalLayout.addWidget(self.bt_stop)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.sw.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_6 = QHBoxLayout(self.page_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_time_t = QLabel(self.page_2)
        self.lb_time_t.setObjectName(u"lb_time_t")
        self.lb_time_t.setMinimumSize(QSize(72, 18))
        self.lb_time_t.setMaximumSize(QSize(72, 18))
        self.lb_time_t.setFont(font1)
        self.lb_time_t.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lb_time_t)

        self.bt_prev = QPushButton(self.page_2)
        self.bt_prev.setObjectName(u"bt_prev")
        self.bt_prev.setMinimumSize(QSize(26, 18))
        self.bt_prev.setMaximumSize(QSize(26, 18))
        self.bt_prev.setFont(font)

        self.horizontalLayout_5.addWidget(self.bt_prev)

        self.bt_next = QPushButton(self.page_2)
        self.bt_next.setObjectName(u"bt_next")
        self.bt_next.setMinimumSize(QSize(26, 18))
        self.bt_next.setMaximumSize(QSize(26, 18))
        self.bt_next.setFont(font)

        self.horizontalLayout_5.addWidget(self.bt_next)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.bt_rewind = QPushButton(self.page_2)
        self.bt_rewind.setObjectName(u"bt_rewind")
        self.bt_rewind.setMinimumSize(QSize(26, 18))
        self.bt_rewind.setMaximumSize(QSize(26, 18))
        self.bt_rewind.setFont(font)

        self.horizontalLayout_5.addWidget(self.bt_rewind)

        self.bt_forward = QPushButton(self.page_2)
        self.bt_forward.setObjectName(u"bt_forward")
        self.bt_forward.setMinimumSize(QSize(26, 18))
        self.bt_forward.setMaximumSize(QSize(26, 18))
        self.bt_forward.setFont(font)

        self.horizontalLayout_5.addWidget(self.bt_forward)

        self.lb_time_rem = QLabel(self.page_2)
        self.lb_time_rem.setObjectName(u"lb_time_rem")
        self.lb_time_rem.setMinimumSize(QSize(72, 18))
        self.lb_time_rem.setMaximumSize(QSize(72, 18))
        self.lb_time_rem.setFont(font1)
        self.lb_time_rem.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lb_time_rem)

        self.bt_cap = QPushButton(self.page_2)
        self.bt_cap.setObjectName(u"bt_cap")
        self.bt_cap.setMinimumSize(QSize(26, 18))
        self.bt_cap.setMaximumSize(QSize(26, 18))
        self.bt_cap.setFont(font)

        self.horizontalLayout_5.addWidget(self.bt_cap)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.sw.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.sw)

        self.bt_toggle = QPushButton(self.fm_control)
        self.bt_toggle.setObjectName(u"bt_toggle")
        self.bt_toggle.setMinimumSize(QSize(26, 18))
        self.bt_toggle.setMaximumSize(QSize(26, 18))
        self.bt_toggle.setFont(font)

        self.horizontalLayout_3.addWidget(self.bt_toggle)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.fm_control)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(SkinPlayer)

        self.sw.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SkinPlayer)
    # setupUi

    def retranslateUi(self, SkinPlayer):
        SkinPlayer.setWindowTitle(QCoreApplication.translate("SkinPlayer", u"Form", None))
        self.bt_play.setText(QCoreApplication.translate("SkinPlayer", u"P", None))
        self.lb_time.setText(QCoreApplication.translate("SkinPlayer", u"00:00:00", None))
        self.lb_vol.setText(QCoreApplication.translate("SkinPlayer", u"100", None))
        self.bt_stop.setText(QCoreApplication.translate("SkinPlayer", u"S", None))
        self.lb_time_t.setText(QCoreApplication.translate("SkinPlayer", u"00:00:00.000", None))
        self.bt_prev.setText(QCoreApplication.translate("SkinPlayer", u"<", None))
        self.bt_next.setText(QCoreApplication.translate("SkinPlayer", u">", None))
        self.bt_rewind.setText(QCoreApplication.translate("SkinPlayer", u"R", None))
        self.bt_forward.setText(QCoreApplication.translate("SkinPlayer", u"F", None))
        self.lb_time_rem.setText(QCoreApplication.translate("SkinPlayer", u"00:00:00.000", None))
        self.bt_cap.setText(QCoreApplication.translate("SkinPlayer", u"C", None))
        self.bt_toggle.setText(QCoreApplication.translate("SkinPlayer", u"T", None))
    # retranslateUi
