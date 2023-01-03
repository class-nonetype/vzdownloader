# -*- coding: utf-8 -*-

EXCEPTIONS = []


import sys


from PyQt5 import (QtCore, QtGui, QtWidgets)
from PyQt5.QtCore import (Qt)
from PyQt5.QtWidgets import (qApp, QApplication)

import platform
import time
import os
import getpass

try:
    import youtube_dl

except:

    if platform.system() == 'Windows':
        os.system('python -m pip install youtube_dl')
    
    elif platform.system() == 'Linux':
        os.system('python3 -m pip install youtube_dl')

finally:
    import youtube_dl



###########################################################################
#                                                                         #
#                                  Modelo                                 #
#                                                                         #
###########################################################################

class Model:

    def __init__(self):


        self.attributes = {
            'system'        : {
                'user'          : getpass.getuser(),
                'os'            : platform.system(),
                'system'        : platform.system(),
                'version'       : platform.version(),
                'processor'     : platform.processor(),
                'node'          : platform.node(),
                'machine'       : platform.machine(),
                'architecture'  : platform.architecture(),
                'platform'      : platform.platform()
            },
            'download'      : {
                'path' : {
                    'download_directory'    : str(None),
                    'download_file'         : str(None)
                },
                'file' : {
                    'name'                  : str(None)
                }
            },
            'downloads'     : []
        }





###########################################################################
#                                                                         #
#                                  Vista                                  #
#                                                                         #
###########################################################################



class MessageView(QtWidgets.QMessageBox):

    def __init__(self):
        QtWidgets.QMessageBox.__init__(self)

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
        except AttributeError as exc:
            EXCEPTIONS.append(exc)
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




class SideGrip(QtWidgets.QWidget):

    def __init__(self, parent, edge):
        QtWidgets.QWidget.__init__(self, parent)

        self.WidgetSideGrip = QtWidgets.QWidget(self)
        self.WidgetSideGrip.setObjectName('WidgetSideGrip')
        self.WidgetSideGrip.setStyleSheet('''
            QWidget#WidgetSideGrip {
                background: #D37242;
                border-radius: 20px;
                border: 14px solid #D37242;                   
            }
        ''')

        self.BoxLayoutSideGrip = QtWidgets.QVBoxLayout(self)
        self.BoxLayoutSideGrip.setContentsMargins(0, 0, 0, 0)
        self.BoxLayoutSideGrip.addWidget(self.WidgetSideGrip)

        if edge == QtCore.Qt.LeftEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunction = self.resizeLeft

        elif edge == QtCore.Qt.TopEdge:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunction = self.resizeTop

        elif edge == QtCore.Qt.RightEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunction = self.resizeRight

        else:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunction = self.resizeBottom

        self.mousePos = None

    def resizeLeft(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() - delta.x())
        geo = window.geometry()
        geo.setLeft(geo.right() - width)
        window.setGeometry(geo)

    def resizeTop(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() - delta.y())
        geo = window.geometry()
        geo.setTop(geo.bottom() - height)
        window.setGeometry(geo)

    def resizeRight(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() + delta.x())
        window.resize(width, window.height())

    def resizeBottom(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() + delta.y())
        window.resize(window.width(), height)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None:
            delta = event.pos() - self.mousePos
            self.resizeFunction(delta)

    def mouseReleaseEvent(self, event):
        self.mousePos = None



class MainView(QtWidgets.QMainWindow):
    _gripSize = 1

    def __init__(self, Controller):
        super().__init__()

        self.Controller = Controller

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
        self.sideGrips = [
            SideGrip(self, QtCore.Qt.LeftEdge), 
            SideGrip(self, QtCore.Qt.TopEdge), 
            SideGrip(self, QtCore.Qt.RightEdge), 
            SideGrip(self, QtCore.Qt.BottomEdge), 
        ]
        self.cornerGrips = [QtWidgets.QSizeGrip(self) for i in range(4)]

    @property
    def gripSize(self):
        return self._gripSize

    def setGripSize(self, size):
        if size == self._gripSize:
            return
        self._gripSize = max(2, size)
        self.updateGrips()

    def updateGrips(self):
        self.setContentsMargins(*[self.gripSize] * 4)

        outRect = self.rect()
        inRect = outRect.adjusted(self.gripSize, self.gripSize,
            -self.gripSize, -self.gripSize)

        # top left
        self.cornerGrips[0].setGeometry(
            QtCore.QRect(outRect.topLeft(), inRect.topLeft()))

        # top right
        self.cornerGrips[1].setGeometry(
            QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())

        # bottom right
        self.cornerGrips[2].setGeometry(
            QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))

        # bottom left
        self.cornerGrips[3].setGeometry(
            QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

        # left edge
        self.sideGrips[0].setGeometry(
            0, inRect.top(), self.gripSize, inRect.height())

        # top edge
        self.sideGrips[1].setGeometry(
            inRect.left(), 0, inRect.width(), self.gripSize)

        # right edge
        self.sideGrips[2].setGeometry(
            inRect.left() + inRect.width(), 
            inRect.top(), self.gripSize, inRect.height())

        # bottom edge
        self.sideGrips[3].setGeometry(
            self.gripSize, inRect.top() + inRect.height(), 
            inRect.width(), self.gripSize)

    def closeEvent(self, event):
        self.destroy()

    def resizeEvent(self, event):
        QtWidgets.QMainWindow.resizeEvent(self, event)
        self.updateGrips()

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
        except AttributeError as exc:
            EXCEPTIONS.append(exc)
            pass

    def mouseReleaseEvent(self, event):
        self.m_drag = False

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            qApp.quit()

        elif event.key() == QtCore.Qt.Key_F1:
            return self.stackedWidget.setCurrentWidget(self.pageHome)

        elif event.key() == QtCore.Qt.Key_F2:
            return self.stackedWidget.setCurrentWidget(self.pageDownloader)

        elif event.key() == QtCore.Qt.Key_F3:
            return self.stackedWidget.setCurrentWidget(self.pageDownloads)

        else:
            super().keyPressEvent(event)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(800, 530)
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
        self.frameWindowPanel.setStyleSheet(
                "QFrame {\n"
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
        self.pushButtonClose.setStyleSheet(
                "QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButtonClose, 0, 2, 1, 1)


        self.pushButtonMinimize = QtWidgets.QPushButton(self.framePushButtonWindowPanel)
        self.pushButtonMinimize.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonMinimize.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonMinimize.setStyleSheet(
                "QPushButton {\n"
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

        self.pushButtonRestore = QtWidgets.QPushButton(self.framePushButtonWindowPanel)
        self.pushButtonRestore.setMinimumSize(QtCore.QSize(42, 42))
        self.pushButtonRestore.setMaximumSize(QtCore.QSize(42, 42))
        self.pushButtonRestore.setStyleSheet(
                "QPushButton {\n"
                "    background-color : #000000;\n"
                "}\n"
                "\n"
                "QPushButton:hover {\n"
                "    background-color : #555555;\n"
                "}")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-window-restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButtonRestore.setIcon(icon2)
        self.pushButtonRestore.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonRestore.setObjectName("pushButtonRestore")

        self.gridLayout_4.addWidget(self.pushButtonRestore, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.framePushButtonWindowPanel, 0, 2, 1, 1)


        self.labelWindowTitle = QtWidgets.QLabel(self.frameWindowPanel)
        self.labelWindowTitle.setStyleSheet(
                "QLabel {\n"
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
        self.frameSidebar.setStyleSheet(
                "QFrame {\n"
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

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 1, 0, 1, 1)


        self.pushButtonSwipeSidebar = QtWidgets.QPushButton(self.frameSidebar)
        self.pushButtonSwipeSidebar.setStyleSheet(
                "QPushButton{\n"
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

        self.pushButtonDownloads = QtWidgets.QPushButton(self.frameSidebar)
        self.pushButtonDownloads.setStyleSheet(
                "QPushButton{\n"
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
        icon4.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-vertical-align-bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButtonDownloads.setIcon(icon4)
        self.pushButtonDownloads.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonDownloads.setObjectName("pushButtonDownloads")

        self.gridLayout_5.addWidget(self.pushButtonDownloads, 4, 0, 1, 1)

        self.pushButtonHome = QtWidgets.QPushButton(self.frameSidebar)
        self.pushButtonHome.setStyleSheet(
                "QPushButton{\n"
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

        self.pushButtonDownloader = QtWidgets.QPushButton(self.frameSidebar)
        self.pushButtonDownloader.setStyleSheet(
                "QPushButton{\n"
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

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-chevron-circle-right-alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButtonDownloader.setIcon(icon6)
        self.pushButtonDownloader.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonDownloader.setObjectName("pushButtonDownloader")

        self.gridLayout_5.addWidget(self.pushButtonDownloader, 3, 0, 1, 1)
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
        self.frameDownloads.setStyleSheet(
                "QFrame {\n"
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
        self.labelDownloads.setStyleSheet(
                "QLabel{\n"
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

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_11.addItem(spacerItem3, 0, 1, 1, 1)


        self.tableWidgetDownloads = QtWidgets.QTableWidget(self.frameDownloadsContent)
        self.tableWidgetDownloads.setStyleSheet(
                "QTableView {\n"
                "    background-color : #FFFFFF;\n"
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
        self.tableWidgetDownloads.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidgetDownloads.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidgetDownloads.setLineWidth(2)
        self.tableWidgetDownloads.setMidLineWidth(0)
        self.tableWidgetDownloads.setObjectName("tableWidgetDownloads")
        self.tableWidgetDownloads.setColumnCount(0)
        self.tableWidgetDownloads.setRowCount(0)


        self.gridLayout_11.addWidget(self.tableWidgetDownloads, 1, 0, 1, 3)
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
        self.labelHome.setStyleSheet(
                "QLabel{\n"
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
        self.frameImage.setStyleSheet(
                "QFrame {\n"
                "    background : #FFFFFF;\n"
                "}")
        self.frameImage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameImage.setLineWidth(0)
        self.frameImage.setObjectName("frameImage")

        self.gridLayout_14 = QtWidgets.QGridLayout(self.frameImage)
        self.gridLayout_14.setObjectName("gridLayout_14")

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem4, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem5, 0, 0, 1, 3)

        self.labelHomeImage = QtWidgets.QLabel(self.frameImage)
        self.labelHomeImage.setMinimumSize(QtCore.QSize(300, 300))
        self.labelHomeImage.setMaximumSize(QtCore.QSize(300, 300))
        self.labelHomeImage.setText("")
        self.labelHomeImage.setPixmap(QtGui.QPixmap("resources/img/downloader.png"))
        self.labelHomeImage.setScaledContents(True)
        self.labelHomeImage.setWordWrap(False)
        self.labelHomeImage.setObjectName("labelHomeImage")


        self.gridLayout_14.addWidget(self.labelHomeImage, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem6, 3, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem7, 2, 0, 1, 1)

        self.labelVersion = QtWidgets.QLabel(self.frameImage)
        self.labelVersion.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelVersion.setStyleSheet(
                "QLabel {\n"
                "    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
                "}")
        self.labelVersion.setScaledContents(True)
        self.labelVersion.setObjectName("labelVersion")

        self.gridLayout_14.addWidget(self.labelVersion, 1, 2, 1, 1)
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
        self.frameDownloader.setStyleSheet(
                "QFrame {\n"
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


        self.groupBoxDownloader = QtWidgets.QGroupBox(self.frameDownloader)
        self.groupBoxDownloader.setStyleSheet(
                "QGroupBox {\n"
                "\n"
                "    font: 76 13pt \"Microsoft JhengHei UI\";\n"
                "    font-weight: bold;\n"
                "    color: #D37242;\n"
                "}\n"
                "\n"
                "")
        self.groupBoxDownloader.setTitle("")
        self.groupBoxDownloader.setObjectName("groupBoxDownloader")


        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBoxDownloader)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.groupBoxYoutubeURL = QtWidgets.QGroupBox(self.groupBoxDownloader)
        self.groupBoxYoutubeURL.setStyleSheet(
                "QGroupBox {\n"
                "    font: 26 14pt \"Microsoft YaHei UI Light\";\n"
                "}\n"
                "")
        self.groupBoxYoutubeURL.setObjectName("groupBoxYoutubeURL")

        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBoxYoutubeURL)
        self.gridLayout_18.setObjectName("gridLayout_18")

        self.lineEditURL = QtWidgets.QLineEdit(self.groupBoxYoutubeURL)
        self.lineEditURL.setMinimumSize(QtCore.QSize(550, 0))
        self.lineEditURL.setMaximumSize(QtCore.QSize(550, 16777215))
        self.lineEditURL.setAutoFillBackground(False)
        self.lineEditURL.setStyleSheet(
                "QLineEdit {\n"
                "    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
                "}")
        self.lineEditURL.setObjectName("lineEditURL")
        self.gridLayout_18.addWidget(self.lineEditURL, 2, 0, 1, 1)


        self.labelURL = QtWidgets.QLabel(self.groupBoxYoutubeURL)
        self.labelURL.setStyleSheet(
                "QLabel {\n"
                "    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
                "}")
        self.labelURL.setObjectName("labelURL")
        self.gridLayout_18.addWidget(self.labelURL, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_18.addItem(spacerItem8, 3, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_18.addItem(spacerItem9, 5, 0, 1, 1)


        self.pushButtonDownload = QtWidgets.QPushButton(self.groupBoxYoutubeURL)
        self.pushButtonDownload.setMinimumSize(QtCore.QSize(200, 46))
        self.pushButtonDownload.setMaximumSize(QtCore.QSize(200, 46))
        self.pushButtonDownload.setStyleSheet(
                "QPushButton{\n"
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

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/icons/24x24/cil-vertical-align-bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)


        self.pushButtonDownload.setIcon(icon7)
        self.pushButtonDownload.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonDownload.setObjectName("pushButtonDownload")

        self.gridLayout_18.addWidget(self.pushButtonDownload, 4, 0, 1, 1)


        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        self.gridLayout_18.addItem(spacerItem10, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBoxYoutubeURL, 1, 1, 1, 1)


        self.groupBoxDownload = QtWidgets.QGroupBox(self.groupBoxDownloader)
        self.groupBoxDownload.setStyleSheet(
                "QGroupBox {\n"
                "    font: 26 14pt \"Microsoft YaHei UI Light\";\n"
                "}\n"
                "")
        self.groupBoxDownload.setObjectName("groupBoxDownload")


        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBoxDownload)
        self.gridLayout_17.setObjectName("gridLayout_17")


        self.labelTitle = QtWidgets.QLabel(self.groupBoxDownload)
        self.labelTitle.setMinimumSize(QtCore.QSize(0, 24))
        self.labelTitle.setMaximumSize(QtCore.QSize(16777215, 24))
        self.labelTitle.setStyleSheet(
                "QLabel {\n"
                "    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
                "    color: #D37242;\n"
                "}")
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout_17.addWidget(self.labelTitle, 1, 0, 1, 1)


        self.labelDirectory = QtWidgets.QLabel(self.groupBoxDownload)
        self.labelDirectory.setMinimumSize(QtCore.QSize(0, 24))
        self.labelDirectory.setMaximumSize(QtCore.QSize(16777215, 24))
        self.labelDirectory.setStyleSheet(
                "QLabel {\n"
                "    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
                "    color: #D37242;\n"
                "}")
        self.labelDirectory.setText("")
        self.labelDirectory.setObjectName("labelDirectory")

        self.gridLayout_17.addWidget(self.labelDirectory, 2, 0, 1, 1)


        self.progressBarDownload = QtWidgets.QProgressBar(self.groupBoxDownload)
        self.progressBarDownload.setMinimumSize(QtCore.QSize(550, 0))
        self.progressBarDownload.setMaximumSize(QtCore.QSize(550, 16777215))
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

        self.gridLayout_17.addWidget(self.progressBarDownload, 5, 0, 1, 1)


        self.labelDownload = QtWidgets.QLabel(self.groupBoxDownload)
        self.labelDownload.setMaximumSize(QtCore.QSize(16777215, 24))
        self.labelDownload.setStyleSheet(
                "QLabel {\n"
                "    font: 25 11pt \"Microsoft YaHei UI Light\";\n"
                "    color: #D37242;\n"
                "}")
        self.labelDownload.setText("")
        self.labelDownload.setObjectName("labelDownload")
        self.gridLayout_17.addWidget(self.labelDownload, 4, 0, 1, 1)


        spacerItem11 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem11, 3, 0, 1, 1)


        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_17.addItem(spacerItem12, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBoxDownload, 4, 0, 1, 2)


        self.groupBoxOptions = QtWidgets.QGroupBox(self.groupBoxDownloader)
        self.groupBoxOptions.setStyleSheet(
                "QGroupBox {\n"
                "    font: 26 14pt \"Microsoft YaHei UI Light\";\n"
                "}\n"
                "")
        self.groupBoxOptions.setObjectName("groupBoxOptions")


        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBoxOptions)
        self.gridLayout_15.setObjectName("gridLayout_15")


        self.radioButtonAudioOption = QtWidgets.QRadioButton(self.groupBoxOptions)
        self.radioButtonAudioOption.setMinimumSize(QtCore.QSize(550, 0))
        self.radioButtonAudioOption.setMaximumSize(QtCore.QSize(550, 16777215))
        self.radioButtonAudioOption.setStyleSheet(
                "QRadioButton {\n"
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

        self.gridLayout_15.addWidget(self.radioButtonAudioOption, 1, 0, 1, 1)

        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem13, 3, 0, 1, 1)


        self.radioButtonVideoOption = QtWidgets.QRadioButton(self.groupBoxOptions)
        self.radioButtonVideoOption.setMinimumSize(QtCore.QSize(550, 0))
        self.radioButtonVideoOption.setMaximumSize(QtCore.QSize(550, 16777215))
        self.radioButtonVideoOption.setStyleSheet(
                "QRadioButton {\n"
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

        self.gridLayout_15.addWidget(self.radioButtonVideoOption, 2, 0, 1, 1)

        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem14, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBoxOptions, 3, 0, 1, 2)

        spacerItem15 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_16.addItem(spacerItem15, 5, 0, 1, 2)

        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_16.addItem(spacerItem16, 0, 1, 1, 1)

        self.gridLayout_10.addWidget(self.groupBoxDownloader, 1, 0, 1, 1)

        self.labelDownloader = QtWidgets.QLabel(self.frameDownloader)
        self.labelDownloader.setMinimumSize(QtCore.QSize(0, 46))
        self.labelDownloader.setMaximumSize(QtCore.QSize(16777215, 46))
        self.labelDownloader.setStyleSheet(
                "QLabel{\n"
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
        self.gridLayout_8.addWidget(self.frameDownloader, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageDownloader)
        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frameContent, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButtonHome.setText(_translate("MainWindow", "\t\tInicio"))
        self.pushButtonDownloader.setText(_translate("MainWindow", "\t\tDescargador de Youtube"))
        self.pushButtonDownloads.setText(_translate("MainWindow", "\t\tMis descargas"))

        self.groupBoxDownload.setTitle(_translate("MainWindow", "Descarga"))
        self.groupBoxOptions.setTitle(_translate("MainWindow", "Formato"))
        self.groupBoxYoutubeURL.setTitle(_translate("MainWindow", "Youtube"))

        self.labelHome.setText(_translate("MainWindow", "Inicio"))
        self.labelDownloader.setText(_translate("MainWindow", "Descargador de Youtube"))
        self.labelVersion.setText(_translate("MainWindow", "version 1.0.0"))

        self.labelURL.setText(_translate("MainWindow", "URL"))

        self.radioButtonAudioOption.setText(_translate("MainWindow", "Audio"))
        self.radioButtonVideoOption.setText(_translate("MainWindow", "Video"))

        self.pushButtonDownload.setText(_translate("MainWindow", "Descargar"))


        self.labelDownloads.setText(_translate("MainWindow", "Mis descargas"))


class View:

    def __init__(self, Controller):
        self.Controller = Controller

        self.MessageView = MessageView()
        self.MainView = MainView(self.Controller)

    def get_main_window_view(self):
        self.MainView.setupUi()
        self.MainView.setWindowTitle('VZDownloader')
            
        # Components

        self.Controller.main_window_restore()

        self.timer = QtCore.QTimer(self.MainView)
        self.timer.timeout.connect(self.Controller.main_window_title)
        self.timer.start(1000)

        self.MainView.pushButtonClose.clicked.connect(qApp.quit)
        self.MainView.pushButtonMinimize.clicked.connect(self.MainView.showMinimized)
        self.MainView.pushButtonRestore.clicked.connect(lambda : self.Controller.main_window_status_restore())

        self.MainView.stackedWidget.setCurrentWidget(self.MainView.pageHome)
            
        self.MainView.pushButtonSwipeSidebar.clicked.connect(self.Controller.swipe_sidebar)
            
        self.MainView.pushButtonDownloader.clicked.connect(lambda : self.MainView.stackedWidget.setCurrentWidget(self.MainView.pageDownloader))
        self.MainView.pushButtonHome.clicked.connect(lambda : self.MainView.stackedWidget.setCurrentWidget(self.MainView.pageHome))
        self.MainView.pushButtonDownloads.clicked.connect(lambda : self.MainView.stackedWidget.setCurrentWidget(self.MainView.pageDownloads))

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
            EXCEPTIONS.append(exc)
            pass



###########################################################################
#
#                               Controlador                               #
#
###########################################################################
class Controller:

    def __init__(self):
        self.Model = Model()
        self.View = View(self)

    def main_window_title(self):
        self.View.MainView.labelWindowTitle.setText(
            f'''{time.asctime()} - {os.getlogin()}'''
        )
    
    def get_main_window_view(self):
        return self.View.get_main_window_view()

    def swipe_sidebar(self):
        if True:
            width = self.View.MainView.frameSidebar.width()
            normal = 46

            if width == 46:
                extend = 250
            else:
                extend = normal

            self.animation_menu_panel = QtCore.QPropertyAnimation(self.View.MainView.frameSidebar, b'minimumWidth')
            self.animation_menu_panel.setDuration(350)
            self.animation_menu_panel.setStartValue(width)
            self.animation_menu_panel.setEndValue(extend)
            self.animation_menu_panel.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_menu_panel.start()

    def download(self):
        url = self.View.MainView.lineEditURL.text()

        if self.View.MainView.radioButtonAudioOption.isChecked():
            directory = QtWidgets.QFileDialog.getExistingDirectory(
                self.View.MainView, 
                "Selecciona el destino", 
                QtCore.QDir.currentPath()
            )

            if directory:
                #self.View.MainView.lineEditDownloadPath.setText(directory)

                self.Model.attributes['download']['path']['download_directory'] = directory

                try:
                    video = youtube_dl.YoutubeDL().extract_info(
                        url = url, download = False
                    )

                    self.Model.attributes['download']['file']['name'] = video['title'] + '.mp3'
            
                    file_path =\
                        str(
                            self.Model.attributes['download']['path']['download_directory'] +
                            '\\' +
                            self.Model.attributes['download']['file']['name']
                        )
                    file_path = str(file_path).replace('/', '\\')

                    self.Model.attributes['download']['path']['download_file'] = file_path


                    options = {
                        'format'    : 'bestaudio/best',
                        'keepvideo' : False,
                        'postprocessors': [
                            {
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '320',
                            }
                        ],
                        'progress_hooks': [self.download_percent],
                        'outtmpl'   : f'{file_path}',
                        'quiet' : True,
                        'external_downloader_args': ['-loglevel', 'panic', '--verbose']
                    }

                    with youtube_dl.YoutubeDL(options) as ydl:
                        ydl.download([video['webpage_url']])

                    self.View.MainView.lineEditURL.clear()
                    
                    return self.View.get_message_view(
                        status = QtWidgets.QMessageBox.Information,
                        title = 'Descarga finalizada',
                        message = f'Se ha descargado correctamente el archivo en la ruta:\n{file_path}\n'
                    )
                
                except Exception as exc:
                    EXCEPTIONS.append(exc)
                    return self.View.get_message_view(
                        status = QtWidgets.QMessageBox.Critical,
                        title = 'Descarga interrumpida',
                        message = f'Se ha interrumpido la descarga\n{exc}\n'
                    )


        if self.View.MainView.radioButtonVideoOption.isChecked():
            directory = QtWidgets.QFileDialog.getExistingDirectory(
                self.View.MainView, 
                "Selecciona el destino", 
                QtCore.QDir.currentPath()
            )

            if directory:
                self.Model.attributes['download']['path']['download_directory'] = directory

                try:
                    video = youtube_dl.YoutubeDL().extract_info(
                        url = url, download = False
                    )


                    for obj in os.scandir(self.Model.attributes['download']['path']['download_directory']):
                        print(obj.path)

                    #self.Model.download_file_name = video['title'] + '.mp4'

                    #file_path = str(directory + '/' + self.Model.download_file_name)

                    #self.Model.download_file_path = file_path

                    options = {
                        'format' : 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
                        'progress_hooks': [self.download_percent],
                        #'outtmpl'   : f'{file_path}',
                        'quiet' : True,
                        'external_downloader_args': ['-loglevel', 'panic', '--verbose']

                    }

                    with youtube_dl.YoutubeDL(options) as ydl:
                        ydl.download([video['webpage_url']])

                    self.View.MainView.lineEditURL.clear()
                    
                    return self.View.get_message_view(
                        status = QtWidgets.QMessageBox.Information,
                        title = 'Descarga finalizada',
                        message = f'Se ha descargado correctamente el archivo en la ruta:\n'
                        #message = f'Se ha descargado correctamente el archivo en la ruta:\n{file_path}\n'
                    )
                
                except Exception as exc:
                    EXCEPTIONS.append(exc)
                    return self.View.get_message_view(
                        status = QtWidgets.QMessageBox.Critical,
                        title = 'Descarga interrumpida',
                        message = f'Se ha interrumpido la descarga\n{exc}\n'
                    )

    def download_percent(self, download):
        

        if download['status'] == 'downloading':
            percent = download['_percent_str']
            percent = percent.replace('%', '')
            
            try:

                self.View.MainView.labelDownload.setText(
                    f'''{download['_speed_str']} de {download['_total_bytes_str']}'''
                )
                self.View.MainView.labelDirectory.setText(
                    f'''{self.Model.attributes['download']['path']['download_directory']}'''
                )
                self.View.MainView.labelTitle.setText(
                    f'''{self.Model.attributes['download']['file']['name']}'''
                )

                download_percent = int(float(percent))
                self.View.MainView.progressBarDownload.setValue(int(download_percent))
                self.View.MainView.progressBarDownload.setFormat('%.02f%%' % (float(percent)))
            except Exception as exc:
                
                EXCEPTIONS.append(exc)
                pass
            
            QtWidgets.QApplication.processEvents()
        
        
        if download['status'] == 'finished':

            self.View.MainView.labelDownload.setText('')
            self.View.MainView.labelDirectory.setText('')
            self.View.MainView.labelTitle.setText('')
            self.View.MainView.progressBarDownload.setValue(0)
            self.View.MainView.progressBarDownload.setFormat('%.02f%%' % (float(0)))


            self.Model.attributes['download']['path']['download_directory'] = str(self.Model.attributes['download']['path']['download_directory']).replace('/', '\\')

            self.Model.attributes['downloads'].append(
                [
                    time.ctime(os.path.getmtime(self.Model.attributes['download']['path']['download_file'])),
                    self.Model.attributes['download']['path']['download_directory'],
                    self.Model.attributes['download']['file']['name'],
                    self.Model.attributes['download']['path']['download_file'],
                    f'''{int(float(os.path.getsize(self.Model.attributes['download']['path']['download_file']) / 1024))}MB'''
                ]
            )

            

            header = [
                'Fecha de creacion',
                'Ubicacion de la descarga',
                'Nombre del archivo',
                'Ubicacion del archivo',
                'Tamaño del archivo'
            ]

            self.View.MainView.tableWidgetDownloads.setColumnCount(len(header))
            self.View.MainView.tableWidgetDownloads.setHorizontalHeaderLabels(header)

            self.View.MainView.tableWidgetDownloads.setRowCount(len(self.Model.attributes['downloads']))

            for row in range(len(self.Model.attributes['downloads'])):
                for column in range(len(header)):
                    self.View.MainView.tableWidgetDownloads.setItem(
                        row, column, QtWidgets.QTableWidgetItem(
                            str(
                                self.Model.attributes['downloads'][row][column]
                            )
                        )
                    )
                    self.View.MainView.tableWidgetDownloads.horizontalHeader().setSectionResizeMode(column, QtWidgets.QHeaderView.ResizeToContents)
            self.View.MainView.tableWidgetDownloads.cellClicked.connect(self.clicked_cell)
            self.View.MainView.tableWidgetDownloads.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            
    def clicked_cell(self, row, column):
        item = ''
        item = self.View.MainView.tableWidgetDownloads.item(row, column)

        try:
            if column == 1 or column == 3:
                os.startfile(f'''{item.text()}''')
        
        except Exception as exc:
            EXCEPTIONS.append(exc)
            pass

    def main_window_restore(self):
        def dobleClickMaximizeRestore(event):
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(8, lambda: self.main_window_status_restore())
                
        self.View.MainView.frameWindowPanel.mouseDoubleClickEvent = dobleClickMaximizeRestore

    def main_window_status_restore(self):
        def main_window_maximize():
            return self.View.MainView.showMaximized()

        def main_window_minimize():
            return self.View.MainView.showNormal()
        
        if self.View.MainView.windowState() == QtCore.Qt.WindowState.WindowNoState:
            
            main_window_maximize()
            
            self.View.MainView.pushButtonRestore.setToolTip('Restore')
            
            _icon = QtGui.QIcon()
            _icon.addPixmap(
                QtGui.QPixmap('resources/icons/24x24/cil-window-restore.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            
            self.View.MainView.pushButtonRestore.setIcon(_icon)
            self.View.MainView.pushButtonRestore.setIconSize(QtCore.QSize(20, 20))
        
        else:
            
            main_window_minimize()
            
            self.View.MainView.pushButtonRestore.setToolTip('Maximize')
            
            _icon = QtGui.QIcon()
            _icon.addPixmap(
                QtGui.QPixmap(u'resources/icons/24x24/cil-window-maximize.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            
            self.View.MainView.pushButtonRestore.setIcon(_icon)
            self.View.MainView.pushButtonRestore.setIconSize(QtCore.QSize(20, 20))











#   Main function
def main():
    qApp = QApplication(sys.argv)

    

    try:
        attr = {
            'controller' : Controller(),
            'model'      : Controller().Model,
            'view'       : Controller().View
        }
        attr['controller'].get_main_window_view()

        return qApp.exec_()

    except Exception as exc:
        EXCEPTIONS.append(
            exc
        )
if __name__ == '__main__':
    main()
