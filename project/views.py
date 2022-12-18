# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI - Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import qApp



from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from PyQt5.QtCore import (
    Qt

)

from PyQt5.QtWidgets import (
    QMessageBox
)

from PyQt5 import (QtWidgets, QtCore)

class MessageView(QMessageBox):

    def __init__(self):
        QMessageBox.__init__(self)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)


    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass


    def mouseReleaseEvent(self, event):
        self.m_drag = False

    def set_title(self, title : str):
        self.title = title
        return self.title

    def set_message(self, message : str):
        self.message = message
        return self.message
    
    def set_status(self, status : str):
        self.status = status
        return self.status

    def setupUi(self):

        self.setWindowTitle(self.title)
        self.setMaximumSize(QtCore.QSize(437, 265))

        self.setText(self.message)
        self.setIcon(self.status)

        
        self.setStyleSheet(
            "QLabel{\n"
            "    font : 75 12pt \"Microsoft JhengHei UI\";\n"
            "    color : #FFFFFF;\n"
            "    border-radius : 0px;\n"
            "    text-align : left;\n"
            "    border : flat 0px;\n"
            "}\n"
            "\n"

            "QWidget {\n"
            "    background-color: #6B5876;\n"
            "    border : flat 1px;\n"
            "}\n"
            "\n"

            "QPushButton{\n"
            "    background-color : #D37242;\n"
            "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
            "    color : #FFFFFF;\n"
            "    border-radius : 0px;\n"
            "    border : flat 0px;\n"
            "    border-top-left-radius: 12px;\n"
            "    border-bottom-left-radius: 12px;\n"
            "    border-top-right-radius: 12px;\n"
            "    border-bottom-right-radius: 12px;\n"
            "    width : 60px;"
            "    text-align : center;\n"
            "    padding-left: 8px;\n"
            "    padding-right: 8px;\n"
            "    padding-top: 5px;\n"
            "    padding-bottom: 5px;\n"
            "}\n"
            "\n"

            "QPushButton:hover{\n"
            "    background-color: #FFFFFF;\n"
            "    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
            "    color : #000000;\n"
            "    border : flat 0px;\n"
            
            "    border-top-left-radius: 12px;\n"
            "    border-bottom-left-radius: 12px;\n"
            "    border-top-right-radius: 12px;\n"
            "    border-bottom-right-radius: 12px;\n"
            "}\n"
            "\n"

            "QFrame {\n"
            "    background-color: #6B5876;\n"
            #"    border: 2px solid;\n"
            #"    border-color : #D37242;\n"
            "}"

        )



class MainView(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        self.destroy()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() and Qt.LeftButton:
                self.move(event.globalPos()-self.m_DragPosition)
                event.accept()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        self.m_drag = False

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(812, 525)

        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frameWindowPanel = QtWidgets.QFrame(self.frame)
        self.frameWindowPanel.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frameWindowPanel.setStyleSheet("QFrame {\n"
"    background : #000000\n"
"}")
        self.frameWindowPanel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameWindowPanel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameWindowPanel.setLineWidth(0)
        self.frameWindowPanel.setObjectName("frameWindowPanel")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frameWindowPanel)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.framePushButtonWindowPanel = QtWidgets.QFrame(self.frameWindowPanel)
        self.framePushButtonWindowPanel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framePushButtonWindowPanel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.framePushButtonWindowPanel.setLineWidth(0)
        self.framePushButtonWindowPanel.setObjectName("framePushButtonWindowPanel")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.framePushButtonWindowPanel)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonClose = QtWidgets.QPushButton(self.framePushButtonWindowPanel)
        self.pushButtonClose.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonClose.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonClose.setStyleSheet("QPushButton {\n"
"    background-color : #A93226;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color : #87281E\n"
"}")
        self.pushButtonClose.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClose.setIcon(icon)
        self.pushButtonClose.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.gridLayout_4.addWidget(self.pushButtonClose, 0, 1, 1, 1)
        self.pushButtonMinimize = QtWidgets.QPushButton(self.framePushButtonWindowPanel)
        self.pushButtonMinimize.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonMinimize.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonMinimize.setStyleSheet("QPushButton {\n"
"    background-color : #000000;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color : #555555;\n"
"}")
        self.pushButtonMinimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonMinimize.setIcon(icon1)
        self.pushButtonMinimize.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonMinimize.setObjectName("pushButtonMinimize")
        self.gridLayout_4.addWidget(self.pushButtonMinimize, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.framePushButtonWindowPanel, 0, 2, 1, 1)
        self.labelWindowTitle = QtWidgets.QLabel(self.frameWindowPanel)
        self.labelWindowTitle.setStyleSheet("QLabel {\n"
"    font : 77 15pt \"Microsoft JhengHei UI\";\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    color : #4F6FA0;\n"
"}\n"
"")
        self.labelWindowTitle.setText("")
        self.labelWindowTitle.setObjectName("labelWindowTitle")
        self.gridLayout_3.addWidget(self.labelWindowTitle, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frameWindowPanel, 0, 0, 1, 2)
        self.frameSidebar = QtWidgets.QFrame(self.frame)
        self.frameSidebar.setMinimumSize(QtCore.QSize(0, 0))
        self.frameSidebar.setMaximumSize(QtCore.QSize(46, 16777215))
        self.frameSidebar.setStyleSheet("QFrame {\n"
"    background : #61364F;\n"
"}")
        self.frameSidebar.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameSidebar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameSidebar.setLineWidth(0)
        self.frameSidebar.setObjectName("frameSidebar")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frameSidebar)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.psuhButtonDownloads = QtWidgets.QPushButton(self.frameSidebar)
        self.psuhButtonDownloads.setStyleSheet("QPushButton{\n"
"    background-color: #61364F;\n"
"    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #80526D;\n"
"    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #DDDDDD;\n"
"    border-left : 5px solid #D37242;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-vertical-align-bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.psuhButtonDownloads.setIcon(icon2)
        self.psuhButtonDownloads.setIconSize(QtCore.QSize(24, 24))
        self.psuhButtonDownloads.setObjectName("psuhButtonDownloads")
        self.gridLayout_5.addWidget(self.psuhButtonDownloads, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 1, 0, 1, 1)
        self.pushButtonSwipeSidebar = QtWidgets.QPushButton(self.frameSidebar)
        self.pushButtonSwipeSidebar.setStyleSheet("QPushButton{\n"
"    background-color : #D37242;\n"
"    font : 75 13pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"\n"
"    text-align : left;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #BB673D;\n"
"    font : 75 13pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"}\n"
"")
        self.pushButtonSwipeSidebar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSwipeSidebar.setIcon(icon3)
        self.pushButtonSwipeSidebar.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonSwipeSidebar.setFlat(True)
        self.pushButtonSwipeSidebar.setObjectName("pushButtonSwipeSidebar")
        self.gridLayout_5.addWidget(self.pushButtonSwipeSidebar, 0, 0, 1, 1)
        self.pushButtonDownloader = QtWidgets.QPushButton(self.frameSidebar)
        self.pushButtonDownloader.setStyleSheet("QPushButton{\n"
"    background-color: #61364F;\n"
"    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #80526D;\n"
"    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #DDDDDD;\n"
"    border-left : 5px solid #D37242;\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-chevron-circle-right-alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDownloader.setIcon(icon4)
        self.pushButtonDownloader.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonDownloader.setObjectName("pushButtonDownloader")
        self.gridLayout_5.addWidget(self.pushButtonDownloader, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 5, 0, 1, 1)
        self.pushButtonHome = QtWidgets.QPushButton(self.frameSidebar)
        self.pushButtonHome.setStyleSheet("QPushButton{\n"
"    background-color: #61364F;\n"
"    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #80526D;\n"
"    font : 75 12pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #DDDDDD;\n"
"    border-left : 5px solid #D37242;\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonHome.setIcon(icon5)
        self.pushButtonHome.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.gridLayout_5.addWidget(self.pushButtonHome, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frameSidebar, 1, 0, 1, 1)

        self.frameContent = QtWidgets.QFrame(self.frame)
        self.frameContent.setStyleSheet("")
        self.frameContent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameContent.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameContent.setLineWidth(0)
        self.frameContent.setObjectName("frameContent")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frameContent)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frameContent)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageDownloads = QtWidgets.QWidget()
        self.pageDownloads.setObjectName("pageDownloads")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.pageDownloads)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frameDownloads = QtWidgets.QFrame(self.pageDownloads)
        self.frameDownloads.setStyleSheet("QFrame {\n"
"    background : #FFFFFF;\n"
"}")
        self.frameDownloads.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameDownloads.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameDownloads.setLineWidth(0)
        self.frameDownloads.setObjectName("frameDownloads")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frameDownloads)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.labelDownloads = QtWidgets.QLabel(self.frameDownloads)
        self.labelDownloads.setMinimumSize(QtCore.QSize(0, 46))
        self.labelDownloads.setMaximumSize(QtCore.QSize(16777215, 46))
        self.labelDownloads.setStyleSheet("QLabel{\n"
"    background-color: #222222;\n"
"    font : 77 17pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.labelDownloads.setObjectName("labelDownloads")
        self.gridLayout_9.addWidget(self.labelDownloads, 0, 0, 1, 1)
        self.frameDownloadsContent = QtWidgets.QFrame(self.frameDownloads)
        self.frameDownloadsContent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDownloadsContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDownloadsContent.setObjectName("frameDownloadsContent")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frameDownloadsContent)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tableWidgetDownloads = QtWidgets.QTableWidget(self.frameDownloadsContent)
        self.tableWidgetDownloads.setStyleSheet("QTableWidget {\n"
"    background-color : #F0F0F0;\n"
"    font : 75 13pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #D37242;\n"
"    border-radius : 0px;\n"
"    padding-left : 50px;\n"
"    text-align : left;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color : #6178B2;\n"
"    font : 75 13pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"}")
        self.tableWidgetDownloads.setObjectName("tableWidgetDownloads")
        self.gridLayout_11.addWidget(self.tableWidgetDownloads, 1, 0, 1, 3)


        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.frameDownloadsContent, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frameDownloads, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageDownloads)
        self.pageHome = QtWidgets.QWidget()
        self.pageHome.setObjectName("pageHome")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.pageHome)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frameHome = QtWidgets.QFrame(self.pageHome)
        self.frameHome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameHome.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameHome.setLineWidth(0)
        self.frameHome.setObjectName("frameHome")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frameHome)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.labelHome = QtWidgets.QLabel(self.frameHome)
        self.labelHome.setMinimumSize(QtCore.QSize(0, 46))
        self.labelHome.setMaximumSize(QtCore.QSize(16777215, 46))
        self.labelHome.setStyleSheet("QLabel{\n"
"    background-color: #222222;\n"
"    font : 77 17pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.labelHome.setObjectName("labelHome")
        self.gridLayout_13.addWidget(self.labelHome, 0, 0, 1, 1)
        self.frameImage = QtWidgets.QFrame(self.frameHome)
        self.frameImage.setStyleSheet("QFrame {\n"
"    background : #FFFFFF;\n"
"}")
        self.frameImage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameImage.setLineWidth(0)
        self.frameImage.setObjectName("frameImage")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frameImage)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem4, 0, 0, 1, 1)
        self.labelHomeImage = QtWidgets.QLabel(self.frameImage)
        self.labelHomeImage.setMinimumSize(QtCore.QSize(500, 420))
        self.labelHomeImage.setText("")
        self.labelHomeImage.setPixmap(QtGui.QPixmap("resources/img/downloader.png"))
        self.labelHomeImage.setScaledContents(False)
        self.labelHomeImage.setWordWrap(False)
        self.labelHomeImage.setObjectName("labelHomeImage")
        self.gridLayout_14.addWidget(self.labelHomeImage, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_13.addWidget(self.frameImage, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frameHome, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageHome)
        self.pageDownloader = QtWidgets.QWidget()
        self.pageDownloader.setObjectName("pageDownloader")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.pageDownloader)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frameDownloader = QtWidgets.QFrame(self.pageDownloader)
        self.frameDownloader.setStyleSheet("QFrame {\n"
"    background : #FFFFFF;\n"
"}")
        self.frameDownloader.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameDownloader.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameDownloader.setLineWidth(0)
        self.frameDownloader.setObjectName("frameDownloader")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frameDownloader)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.labelDownloader = QtWidgets.QLabel(self.frameDownloader)
        self.labelDownloader.setMinimumSize(QtCore.QSize(0, 46))
        self.labelDownloader.setMaximumSize(QtCore.QSize(16777215, 46))
        self.labelDownloader.setStyleSheet("QLabel{\n"
"    background-color: #222222;\n"
"    font : 77 17pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"    text-align : left;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.labelDownloader.setObjectName("labelDownloader")
        self.gridLayout_10.addWidget(self.labelDownloader, 0, 0, 1, 1)
        self.groupBoxDownloader = QtWidgets.QGroupBox(self.frameDownloader)
        self.groupBoxDownloader.setStyleSheet("QGroupBox {\n"
"\n"
"    font: 76 13pt \"Microsoft JhengHei UI\";\n"
"    font-weight: bold;\n"
"    color: #D37242;\n"
"}\n"
"\n"
"")
        self.groupBoxDownloader.setTitle("")
        self.groupBoxDownloader.setObjectName("groupBoxDownloader")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBoxDownloader)
        self.gridLayout_23.setContentsMargins(18, -1, 18, -1)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.line = QtWidgets.QFrame(self.groupBoxDownloader)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_23.addWidget(self.line, 3, 0, 1, 3)
        self.lineEditURL = QtWidgets.QLineEdit(self.groupBoxDownloader)
        self.lineEditURL.setMinimumSize(QtCore.QSize(500, 0))
        self.lineEditURL.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEditURL.setStyleSheet("QLineEdit {\n"
"    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
"}")
        self.lineEditURL.setObjectName("lineEditURL")
        self.gridLayout_23.addWidget(self.lineEditURL, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem6, 7, 0, 1, 3)
        self.radioButtonAudioOption = QtWidgets.QRadioButton(self.groupBoxDownloader)
        self.radioButtonAudioOption.setStyleSheet("QRadioButton {\n"
"    font : 75 13pt \"Microsoft JhengHei UI\";\n"
"    color : #000000;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    color : #3A609B;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton::checked {\n"
"    color : #3A609B;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    color : #3A609B;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    color : #3A609B;\n"
"}")
        self.radioButtonAudioOption.setObjectName("radioButtonAudioOption")
        self.gridLayout_23.addWidget(self.radioButtonAudioOption, 5, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem7, 11, 0, 1, 3)
        self.labelFormat = QtWidgets.QLabel(self.groupBoxDownloader)
        self.labelFormat.setStyleSheet("QLabel {\n"
"    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
"}")
        self.labelFormat.setObjectName("labelFormat")
        self.gridLayout_23.addWidget(self.labelFormat, 5, 0, 1, 1)
        self.radioButtonVideoOption = QtWidgets.QRadioButton(self.groupBoxDownloader)
        self.radioButtonVideoOption.setStyleSheet("QRadioButton {\n"
"    font : 75 13pt \"Microsoft JhengHei UI\";\n"
"    color : #000000;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    color : #3A609B;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton::checked {\n"
"    color : #3A609B;\n"
"    border-radius : 0px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    color : #3A609B;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    color : #3A609B;\n"
"}")
        self.radioButtonVideoOption.setObjectName("radioButtonVideoOption")
        self.gridLayout_23.addWidget(self.radioButtonVideoOption, 6, 1, 1, 1)
        self.labelURL = QtWidgets.QLabel(self.groupBoxDownloader)
        self.labelURL.setStyleSheet("QLabel {\n"
"    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
"}")
        self.labelURL.setObjectName("labelURL")
        self.gridLayout_23.addWidget(self.labelURL, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem8, 0, 0, 1, 3)
        self.line_5 = QtWidgets.QFrame(self.groupBoxDownloader)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_23.addWidget(self.line_5, 8, 0, 1, 3)
        self.progressBarDownload = QtWidgets.QProgressBar(self.groupBoxDownloader)
        self.progressBarDownload.setStyleSheet(
                "QProgressBar\n"
                "{\n"
                "    border: 2px solid #D37242;\n"
                "    border-radius: 5px;\n"
                "    text-align: center;\n"
                "    font : 77 12pt \"Microsoft JhengHei UI\" bold;\n"
                "    color : #999999\n"
                "}\n"
                "QProgressBar::chunk\n"
                "{\n"
                "    background-color: #61364F;\n"
                "    margin: 0.5px;\n"
                "}")
        self.progressBarDownload.setMinimum(0)
        self.progressBarDownload.setMaximum(100)
        self.progressBarDownload.setProperty("value", 0)
        self.progressBarDownload.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.progressBarDownload.setOrientation(QtCore.Qt.Horizontal)
        self.progressBarDownload.setInvertedAppearance(False)
        self.progressBarDownload.setObjectName("progressBarDownload")
        self.gridLayout_23.addWidget(self.progressBarDownload, 10, 0, 1, 2)


        #self.progressBarDownload.valueChanged.connect(self.onValueChanged)





        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_23.addItem(spacerItem9, 4, 0, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem10, 16, 0, 1, 3)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_23.addItem(spacerItem11, 2, 0, 1, 3)
        self.pushButtonDownload = QtWidgets.QPushButton(self.groupBoxDownloader)
        self.pushButtonDownload.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButtonDownload.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButtonDownload.setStyleSheet("QPushButton{\n"
"    background-color : #D37242;\n"
"    font : 75 13pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"    border-radius : 0px;\n"
"\n"
"    text-align : left;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #BB673D;\n"
"    font : 75 13pt \"Microsoft JhengHei UI\" bold;\n"
"    color : #FFFFFF;\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-vertical-align-bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDownload.setIcon(icon6)
        self.pushButtonDownload.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonDownload.setObjectName("pushButtonDownload")
        self.gridLayout_23.addWidget(self.pushButtonDownload, 15, 0, 1, 1)
        self.labelDownload = QtWidgets.QLabel(self.groupBoxDownloader)
        self.labelDownload.setStyleSheet("QLabel {\n"
"    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
"}")
        self.labelDownload.setText("")
        self.labelDownload.setObjectName("labelDownload")
        self.gridLayout_23.addWidget(self.labelDownload, 9, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBoxDownloader, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frameDownloader, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageDownloader)
        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frameContent, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def onValueChanged(self, value):
        self.progressBarDownload.setFormat('%.02f%%' % (self.prefixFloat))

    def setValue(self, value):
        self.prefixFloat = value
        QtGui.QProgressBar.setValue(self, int(value))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.psuhButtonDownloads.setText(_translate("MainWindow", "Mis descargas"))
        self.pushButtonDownloader.setText(_translate("MainWindow", "Audio"))
        self.pushButtonHome.setText(_translate("MainWindow", "Inicio"))
        self.labelDownloads.setText(_translate("MainWindow", "Descargas"))
        self.labelHome.setText(_translate("MainWindow", "Inicio"))
        self.labelDownloader.setText(_translate("MainWindow", "Descargador"))
        self.radioButtonAudioOption.setText(_translate("MainWindow", "Audio"))
        self.labelFormat.setText(_translate("MainWindow", "Formato"))
        self.radioButtonVideoOption.setText(_translate("MainWindow", "Video"))
        self.labelURL.setText(_translate("MainWindow", "URL"))
        self.pushButtonDownload.setText(_translate("MainWindow", "Descargar"))



class View:

    def __init__(self, Controller):

        self.MessageView = MessageView()
        self.MainView = MainView()

        self.Controller = Controller


    def get_main_window_view(self):
        self.MainView.setupUi()
        self.MainView.setWindowTitle('VZDownloader')
            
        # Components

        self.timer = QtCore.QTimer(self.MainView)
        self.timer.timeout.connect(self.Controller.main_window_title)
        self.timer.start(1000)

            
            
        self.MainView.pushButtonClose.clicked.connect(qApp.quit)
        self.MainView.pushButtonMinimize.clicked.connect(self.MainView.showMinimized)

        self.MainView.stackedWidget.setCurrentWidget(self.MainView.pageHome)
            
        self.MainView.pushButtonSwipeSidebar.clicked.connect(self.Controller.swipe_sidebar)
            
        self.MainView.pushButtonDownloader.clicked.connect(lambda : self.MainView.stackedWidget.setCurrentWidget(self.MainView.pageDownloader))
        self.MainView.pushButtonHome.clicked.connect(lambda : self.MainView.stackedWidget.setCurrentWidget(self.MainView.pageHome))
        self.MainView.psuhButtonDownloads.clicked.connect(lambda : self.MainView.stackedWidget.setCurrentWidget(self.MainView.pageDownloads))

        self.MainView.pushButtonDownload.clicked.connect(self.Controller.download)

        #self.MainView.pushButton.clicked.connect(self.Controller.select_data)

        
        




            
            
        self.MainView.lineEditURL.setPlaceholderText('Ingresa la URL de youtube')
            
        return self.MainView.show()


    def get_message_view(self, title: str, message : str, status : str):
        try:
        
            
            '''
            STATUS >
                        Question
                        Information
                        Warning
                        Critical
            '''
            self.MessageView.set_title(title)
            self.MessageView.set_status(status)
            self.MessageView.set_message(message)

            self.MessageView.setupUi()
            
            return self.MessageView.show()

        except Exception as exc:
            # Logger
            pass