# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen
# créé mars 2020 version 1.0


from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox, QFileDialog, QPlainTextEdit, QDialog, QDockWidget, QVBoxLayout, QTabWidget, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel

from . import bibli_ihm_camino
from .bibli_ihm_camino import *
from . import bibli_camino
from .bibli_camino import *

from qgis.core import *
from qgis.gui import *

import qgis
import os
import subprocess

class Ui_Dialog_Camino_onglet(object):
    def __init__(self):
        self.iface = qgis.utils.iface
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.lScreenDialog, self.hScreenDialog = 810, 640
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,self.lScreenDialog, self.hScreenDialog).size()).expandedTo(Dialog.minimumSizeHint()))
        Dialog.setWindowTitle("CAMINO (mining titles) International...")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        iconSource = bibli_camino.getThemeIcon("camino2.png")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconSource), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        #=====================================================
        #Path user profil camino
        self.initDirCaminoParam = QgsApplication.qgisSettingsDirPath().replace("\\","/") + "camino3param"
     
        #=====================================================
        #Image
        self.labelImage = QtWidgets.QLabel(Dialog)
        myPath = os.path.dirname(__file__)+"/icons/camino2.jpg";
        myDefPath = myPath.replace("\\","/");
        carIcon = QtGui.QImage(myDefPath)
        self.labelImage.setPixmap(QtGui.QPixmap.fromImage(carIcon))
        self.labelImage.setGeometry(QtCore.QRect(660, 45, 130, 90))
        self.labelImage.setObjectName("labelImage")
        
        #=====================================================
        #Param File URL
        monFichierPath = createFolder(self.initDirCaminoParam)
        monFichierPath = monFichierPath.replace("\\","/") + "\\urlcamino.par"
        self.monFichierPath = monFichierPath

        #=====================================================
        #Param File LOGIN
        monFichierPathLoginCourriel = createFolder(self.initDirCaminoParam)
        monFichierPathLoginCourriel = monFichierPathLoginCourriel.replace("\\","/") + "\\logincaminocourriel.par"
        self.monFichierPathLoginCourriel = monFichierPathLoginCourriel

        #=====================================================
        #Image Cursor
        myPathCursorImage = os.path.dirname(__file__)+"/icons/cursor3.jpg";
        myPathCursorImage = myPathCursorImage.replace("\\","/");
        self.cursorImage = QCursor(QPixmap(myPathCursorImage))
        #=====================================================

        #ComboBox Adresse 
        self.labelAdresse = QtWidgets.QLabel(Dialog)
        self.labelAdresse.setGeometry(QtCore.QRect(20,14,100,18))
        self.labelAdresse.setObjectName("labelAdresse")
        self.labelAdresse.setAlignment(Qt.AlignRight)

        self.comboAdresse = QtWidgets.QComboBox(Dialog)
        self.comboAdresse.setGeometry(QtCore.QRect(130,10,660,23))
        self.comboAdresse.setObjectName("comboAdresse")

        #Zone affichage  
        self.resultTextEdit = QtWidgets.QTextEdit(Dialog)
        self.resultTextEdit.setGeometry(QtCore.QRect(5, 45, 650,90))
        self.resultTextEdit.setObjectName("resultTextEdit") 
        self.resultTextEdit.setStyleSheet("QTextEdit {   \
                                background-color: white; \
                                border-style: outset;    \
                                border-width: 2px;       \
                                border-radius: 10px;     \
                                border-color: blue;      \
                                font: bold 11px;         \
                                padding: 6px;            \
                                }")
        
        self.resultTextEdit.setEnabled(False)
        
        #==========================              
        #Zone Onglets
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QtCore.QRect(5, 145, 800,440))
        #--------------------------
        self.tab_widget_Critere = QWidget()
        self.tab_widget_Critere.setObjectName("tab_widget_Critere")
        labelTab5 = QtWidgets.QApplication.translate("camino_onglet_ui", "  Filter  ", None)
        self.tabWidget.addTab(self.tab_widget_Critere,labelTab5)
        #--------------------------
        self.tab_widget_Filter = QWidget()
        self.tab_widget_Filter.setObjectName("tab_widget_Filter")
        labelTab4 = QtWidgets.QApplication.translate("camino_onglet_ui", "   Attributes   ", None)
        self.tabWidget.addTab(self.tab_widget_Filter,labelTab4)
        self.tabWidget.setCurrentIndex(0)
        #--------------------------
        self.tab_widget_Connexion = QWidget()
        self.tab_widget_Connexion.setObjectName("tab_widget_Connexion")
        labelTab6 = QtWidgets.QApplication.translate("camino_onglet_ui", "   connection   ", None)
        self.tabWidget.addTab(self.tab_widget_Connexion,labelTab6)

        #========================== 
        # Premier Onglet
        #====== Zone affichage données avec critères
        self.resulCritere = QtWidgets.QTextEdit(self.tab_widget_Critere)
        self.resulCritere.setGeometry(QtCore.QRect(10, 10, 775, 395))
        self.resulCritere.setObjectName("resulCritere")
        #========================== 
        # deuxième Onglet
        #====== Zone affichage données 
        self.resulFilter = QtWidgets.QTextEdit(self.tab_widget_Filter)
        self.resulFilter.setGeometry(QtCore.QRect(5, 230, 790,390))
        self.resulFilter.setObjectName("resulFilter")
        self.resulFilter.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Filter display", None))
        #------       
        self.resultFilterLayout = QVBoxLayout()
        self.resultFilterLayout.addWidget(self.resulFilter)
        self.tab_widget_Filter.setLayout(self.resultFilterLayout)        
        #========================== 
        # troisième Onglet
        #====== Zone affichage connexion 
        self.resulConnexion = QtWidgets.QTextEdit(self.tab_widget_Connexion)
        self.resulConnexion.setGeometry(QtCore.QRect(10, 10, 775, 395))
        self.resulConnexion.setObjectName("resulFilter")
        #Groupe liseré gauche
        self.groupBoxLeft_1 = QtWidgets.QGroupBox(self.resulConnexion)
        self.groupBoxLeft_1.setGeometry(QtCore.QRect(10,10,755,375))
        self.groupBoxLeft_1.setObjectName("groupBoxLeft_1")

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245,255,0,125))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)
        self.groupBoxLeft_1.setPalette(palette)
        
        #Radio Affichage Etiquettes 
        self.groupBoxRadio = QtWidgets.QGroupBox(self.groupBoxLeft_1)
        self.groupBoxRadio.setGeometry(QtCore.QRect(10,5,140,85))
        self.groupBoxRadio.setObjectName("groupBoxRadio")
        self.groupBoxRadio.setStyleSheet("QGroupBox { color: red; }")
        self.radioOptionMdp3 = QtWidgets.QRadioButton(self.groupBoxRadio)
        self.radioOptionMdp3.setGeometry(QtCore.QRect(10,20,150,23))
        self.radioOptionMdp3.setObjectName("radioOptionMdp3")
        self.radioOptionMdp2 = QtWidgets.QRadioButton(self.groupBoxRadio)
        self.radioOptionMdp2.setGeometry(QtCore.QRect(10,54,150,23))
        self.radioOptionMdp2.setObjectName("radioOptionMdp2")
        self.radioOptionMdp2.setChecked(True)
        #-----------
        #Label et zone COURRIEL   
        self.labelCourriel = QtWidgets.QLabel(self.groupBoxLeft_1)
        self.labelCourriel.setGeometry(QtCore.QRect(120,30,120,18))
        self.labelCourriel.setObjectName("labelCourriel")
        self.labelCourriel.setAlignment(Qt.AlignRight)
        #-----------
        self.textEditCourriel = QtWidgets.QTextEdit(self.groupBoxLeft_1)
        self.textEditCourriel.setGeometry(QtCore.QRect(240,26,505,23))
        self.textEditCourriel.setObjectName("textEditCourriel")

        #Label et zone MDP COURRIEL  
        self.labelMdpCourriel = QtWidgets.QLabel(self.groupBoxLeft_1)
        self.labelMdpCourriel.setGeometry(QtCore.QRect(120,65,120,18))
        self.labelMdpCourriel.setObjectName("labelMdpCourriel")
        self.labelMdpCourriel.setAlignment(Qt.AlignRight)
        #-----------
        self.textEditMdpCourriel = QtWidgets.QTextEdit(self.groupBoxLeft_1)
        self.textEditMdpCourriel.setGeometry(QtCore.QRect(240,61,505,23))
        self.textEditMdpCourriel.setObjectName("textEditMdpCourriel")
        #==========================              
        #Groupe liseré bas
        self.groupBoxDown = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDown.setGeometry(QtCore.QRect(10,590,795,40))
        self.groupBoxDown.setObjectName("groupBoxDown")
        self.groupBoxDown.setStyleSheet("QGroupBox {   \
                                background-color: white; \
                                border-style: outset;    \
                                border-width: 1px;       \
                                border-radius: 10px;     \
                                border-color: black;      \
                                font: bold 12px;         \
                                padding: 6px;            \
                                }")
        #=====================================================
        #Boutons  
        #------       
        self.okhButton = QtWidgets.QPushButton(self.groupBoxDown)
        self.okhButton.setGeometry(QtCore.QRect(500, 10, 100,23))
        self.okhButton.setObjectName("okhButton")
        #------       
        self.helpButton = QtWidgets.QPushButton(self.groupBoxDown)
        self.helpButton.setGeometry(QtCore.QRect(200, 10, 100,23))
        self.helpButton.setObjectName("helpButton")
        self.helpButton.setStyleSheet("QPushButton { color: green; }")
        #------       
        #Filtre bouton multi selection rows 
        self.buttonFilter = QtWidgets.QPushButton(self.tab_widget_Filter)
        self.buttonFilter.setGeometry(QtCore.QRect(200, 378, 100, 23))
        self.buttonFilter.setObjectName("buttonFilter")
        self.buttonFilter.setStyleSheet("QPushButton { color: red; }")
        self.buttonFilter.setVisible(False)
        self.buttonFilter.setEnabled(False)
        #Label nb occurrences
        self.labelOccurrence = QtWidgets.QLabel(self.tab_widget_Filter)
        self.labelOccurrence.setGeometry(QtCore.QRect(450,378,200,18))
        self.labelOccurrence.setObjectName("labelOccurrence")
        self.labelOccurrence.setAlignment(Qt.AlignCenter)    
        self.labelOccurrence.setStyleSheet("QLabel { color: red; }")
        self.labelOccurrence.setVisible(False)
        #------       
        #------ Création de l'IHM Critère
        createIhmCritere(self)   
        #------  
        #Connections  
        self.helpButton.clicked.connect(Dialog.myHelpCamino)
        self.okhButton.clicked.connect(Dialog.reject)
        self.radioOptionMdp2.toggled.connect(Dialog.showHideLogin)
        self.radioOptionMdp3.toggled.connect(Dialog.showHideLogin)
        self.showHideLogin()                                     
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #========================== 
        #Alimentation de la ComboBox Adresse
        self.returnAdresse = self.returnDicoFlux(self.monFichierPath)
        modelComboAdresse = QStandardItemModel()
        for key, value in self.returnAdresse.items() :
            valueCombo = "%s \t--->>  %s" %(str(value[1]), str(value[0]))
            modelComboAdresseCol1 = QStandardItem(str(valueCombo))
            modelComboAdresseCol2 = QStandardItem(str(key))
            modelComboAdresse.appendRow([modelComboAdresseCol1, modelComboAdresseCol2])
        self.comboAdresse.setModel(modelComboAdresse)
        #========================== 
        self.retranslateUi(Dialog)
        returnToken = ""
    #------       
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("camino_onglet_ui", "CAMINO (mining titles) International...", None))
        self.labelCourriel.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "mail address : ", None))
        self.labelMdpCourriel.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Password : ", None))
        self.helpButton.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Help", None))
        self.okhButton.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "Close", None))
        self.buttonFilter.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "multi-line filter", None))
        self.labelAdresse.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "layer address : ", None))
        self.radioOptionMdp2.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "without identifier", None))
        self.radioOptionMdp3.setText(QtWidgets.QApplication.translate("camino_onglet_ui", "With Camino account", None))
        self.groupBoxRadio.setTitle(QtWidgets.QApplication.translate("camino_onglet_ui", " Login ", None))
        self.zMess = QtWidgets.QApplication.translate("camino_onglet_ui", "Here is the return of the Camino API : ", None) +"\n"
        self.zMess1 = QtWidgets.QApplication.translate("camino_onglet_ui", "Username", None)
        self.zMessOrga = QtWidgets.QApplication.translate("camino_onglet_ui", "Organization", None)
        self.zMess2 = QtWidgets.QApplication.translate("camino_onglet_ui", "and Password", None)
        self.zMess3 = QtWidgets.QApplication.translate("camino_onglet_ui", "layer adress", None)
        self.zMess4 = QtWidgets.QApplication.translate("camino_onglet_ui", "name adress", None)
        self.zMess5 = QtWidgets.QApplication.translate("camino_onglet_ui", "provider adress", None)

     #------       
    def returnDicoFlux(self,monFichierPath): return loadFichierParam(self.monFichierPath)
    
    def returnIcon(self, iconAdress) :
        iconSource = iconAdress
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconSource), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    #-----------------------------------
    def showHideCtrl(self,Dialog):
        lScreen, hScreen =  QDesktopWidget().width(), QDesktopWidget().height()
        lDelta = 300 if self.caseFilter.isChecked() else 0
        hDelta =   0 if self.caseFilter.isChecked() else 0
        x, y = (lScreen/2) - (self.lScreenDialog + lDelta)/2, (hScreen/2) - (self.hScreenDialog + hDelta)/2
        self.move(x, y)
        self.resize(self.lScreenDialog + lDelta, self.hScreenDialog + hDelta)
        return
        
    #-----------------------------------
    def showHideLogin(self):
        if self.radioOptionMdp2.isChecked() :
           self.labelCourriel.hide()
           self.textEditCourriel.hide()
           self.labelMdpCourriel.hide()
           self.textEditMdpCourriel.hide()           
        elif self.radioOptionMdp3.isChecked() :
           mIdenCourriel = mGestionLoginCourriel("RESTORE", self.monFichierPathLoginCourriel, '') 
           if self.textEditCourriel.toPlainText() == '' : self.textEditCourriel.setPlainText(mIdenCourriel) 
           self.labelCourriel.show()
           self.textEditCourriel.show()
           self.labelMdpCourriel.show()
           self.textEditMdpCourriel.show()
        return 
        
    #-----------------------------------
    def myHelpCamino(self):
        MonFichierPath = os.path.join(os.path.dirname(__file__) + "/doc/")
        MonFichierPath = MonFichierPath.replace("\\","/")        
        MonFichierReport = os.path.join(MonFichierPath, "camino_doc.pdf")
        execPdf(MonFichierReport)
        return 