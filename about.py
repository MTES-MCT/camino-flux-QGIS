# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen
# créé mars 2020 version 1.0

import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from . import bibli_camino
from .bibli_camino import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,595,480).size()).expandedTo(Dialog.minimumSizeHint()))
        
        iconSource = bibli_camino.getThemeIcon("camino.png")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconSource), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 400, 30))
        self.label_2.setAlignment(Qt.AlignCenter)        
        font = QtGui.QFont()
        font.setPointSize(15) 
        font.setWeight(50) 
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        
        self.labelImage = QtWidgets.QLabel(Dialog)
        myPath = os.path.dirname(__file__)+"/icons/camino2.jpg";
        myDefPath = myPath.replace("\\","/");
        carIcon = QtGui.QImage(myDefPath)
        self.labelImage.setPixmap(QtGui.QPixmap.fromImage(carIcon))
        self.labelImage.setGeometry(QtCore.QRect(10, 10, 266, 178))
        self.labelImage.setObjectName("labelImage")

        self.labelImage2 = QtWidgets.QLabel(Dialog)
        myPath = os.path.dirname(__file__)+"/icons/camino3.jpg";
        myDefPath = myPath.replace("\\","/");
        carIcon2 = QtGui.QImage(myDefPath)
        self.labelImage2.setPixmap(QtGui.QPixmap.fromImage(carIcon2))
        self.labelImage2.setGeometry(QtCore.QRect(328, 200, 266, 178))
        self.labelImage2.setObjectName("labelImage2")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(0,0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)
        self.textEdit.setPalette(palette)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.width = 300
        self.textEdit.height = 100
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textEdit.setGeometry(QtCore.QRect(10, 200, 266, 300))

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(410, 400, 100, 25))
        self.pushButton.clicked.connect(Dialog.reject)

        self.retranslateUi(Dialog)

    def retranslateUi(self, Dialog):
        MonHtml = ""
        MonHtml += "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        MonHtml += "p, li { white-space: pre-wrap; }\n"
        MonHtml += "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
        MonHtml += "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><span style=\" font-weight:600;\">"
        mVERSION = " = version 1.6"
        MonHtml1 = QtWidgets.QApplication.translate("camino_about", "CAMINO (mining titles)", None) 
        MonHtml1 += mVERSION
        MonHtml1 += "<br><br>"
        MonHtml += MonHtml1
        MonHtml += "</span>" 
        MonHtml2 = QtWidgets.QApplication.translate("camino_about", "CAMINO manages", None)
        MonHtml2 += "<br><br>"
        MonHtml2 += QtWidgets.QApplication.translate("camino_about", "valid mining titles and initial or related public and pending applications.", None)
        MonHtml2 += "<br><br>"
        MonHtml2 += QtWidgets.QApplication.translate("camino_about", "operating licenses in Guyana.", None)
        MonHtml += MonHtml2
        MonHtml += "<br><br>"
        MonHtml3 = QtWidgets.QApplication.translate("camino_about", "Open mining data to share information on projects and facilitate their management.", None) 
        MonHtml += MonHtml3
        MonHtml += "</p></td></tr></table>"
        MonHtml += "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
        MonHtml += "<p style=\"margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
        MonHtml += "<font color='#0000FF'><b><u>Didier LECLERC</u></b></font><br><br>"
        MonHtml += "<b>"
        MonHtml4 = QtWidgets.QApplication.translate("camino_about", "MTES / MCTRCT", None) 
        MonHtml += MonHtml4
        MonHtml += "</b><br><b>"
        MonHtml5 = QtWidgets.QApplication.translate("camino_about", "digital service", None) 
        MonHtml += MonHtml5
        MonHtml += "</b><br>"
        MonHtml6 = QtWidgets.QApplication.translate("camino_about", "digital service SG/SNUM/UNI/DRC - Rouen site.", None) 
        MonHtml += MonHtml6
        MonHtml += "<br><br><i>"
        MonHtml7 = QtWidgets.QApplication.translate("camino_about", "Development in 2020 / QGIS 3.12", None) 
        MonHtml += MonHtml7
        MonHtml += "</i></p></body></html>"

    
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("camino_about", "CAMINO (mining titles)", None))
        self.label_2.setText(QtWidgets.QApplication.translate("camino_about", "CAMINO (mining titles)", None))
        self.textEdit.setHtml(QtWidgets.QApplication.translate("camino_about", MonHtml, None))
        self.pushButton.setText(QtWidgets.QApplication.translate("camino_about", "OK", None))
