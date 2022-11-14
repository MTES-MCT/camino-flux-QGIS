# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen
# créé mars 2020 version 1.0

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QAction, QMenu , QApplication, QMessageBox, QFileDialog, QTextEdit, QMainWindow, 
                            QTableView, QDockWidget, QVBoxLayout, QTabWidget, QWidget, QAbstractItemView)
 
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *

from . import bibli_camino
from .bibli_camino import *

#==================================================
# Gestion de l'IHM pour les critères
#==================================================
    
def createIhmCritere(self) :
    #=====================================================
    #Groupe Domaines
    self.groupBoxDom = QtWidgets.QGroupBox(self.tab_widget_Critere)
    self.groupBoxDom.setGeometry(QtCore.QRect(15,15,220,260))
    self.groupBoxDom.setObjectName("groupBoxDom") 
    mMess = QtWidgets.QApplication.translate("bibli_ihm_camino", "  Domains  ", None)
    self.groupBoxDom.setTitle(mMess)
    self.groupBoxDom.setStyleSheet("QGroupBox { color: red; }")
    #------   
    self.groupBoxDomTous = QtWidgets.QGroupBox(self.tab_widget_Critere)
    self.groupBoxDomTous.setGeometry(QtCore.QRect(15,280,220,30))
    self.groupBoxDomTous.setObjectName("groupBoxDomTous") 
    self.groupBoxDomTous.setStyleSheet("QGroupBox { border : 1px solid #E4E4E4}")
    #------
    self.caseDomMINERAUX, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxDom), QtWidgets.QApplication.translate("bibli_ihm_camino", "Minerals and Metals", None)
    genereObjets(self, self.caseDomMINERAUX, "caseDomMINERAUX", 10,20,250,18, mLibelleCase, "metier/domm.png", False, 0, 0)     
    #------       
    self.caseDomGRANULATS, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxDom), QtWidgets.QApplication.translate("bibli_ihm_camino", "Marine Aggregates", None)
    genereObjets(self, self.caseDomGRANULATS, "caseDomGRANULATS", 10,50,250,18, mLibelleCase, "metier/domw.png", False, 0, 0)     
    #------   
    self.caseDomCARRIERES, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxDom), QtWidgets.QApplication.translate("bibli_ihm_camino", "Careers", None)
    genereObjets(self, self.caseDomCARRIERES, "caseDomCARRIERES", 10,80,250,18, mLibelleCase, "metier/domc.png", False, 0, 0)     
    #------                                                                                   
    self.caseDomHYDRO, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxDom), QtWidgets.QApplication.translate("bibli_ihm_camino", "Liquid or gaseous hydrocarbons", None)
    genereObjets(self, self.caseDomHYDRO, "caseDomHYDRO", 10,110,250,18, mLibelleCase, "metier/domh.png", False, 0, 0)     
    #------   
    self.caseDomCOMBU, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxDom), QtWidgets.QApplication.translate("bibli_ihm_camino", "Fossil fuels", None)
    genereObjets(self, self.caseDomCOMBU, "caseDomCOMBU", 10,140,250,18, mLibelleCase, "metier/domf.png", False, 0, 0)     
    #------       
    self.caseDomRADIOACTIFS, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxDom), QtWidgets.QApplication.translate("bibli_ihm_camino", "Radioactive element", None)
    genereObjets(self, self.caseDomRADIOACTIFS, "caseDomRADIOACTIFS", 10,170,250,18, mLibelleCase, "metier/domr.png", False, 0, 0)     
    #------   
    self.caseDomGEOTHERMIE, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxDom), QtWidgets.QApplication.translate("bibli_ihm_camino", "Geothermal energy", None)
    genereObjets(self, self.caseDomGEOTHERMIE, "caseDomGEOTHERMIE", 10,200,250,18, mLibelleCase, "metier/domg.png", False, 0, 0)     
    #------       
    self.caseDomSTOCKAGES, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxDom), QtWidgets.QApplication.translate("bibli_ihm_camino", "Underground storage", None)
    genereObjets(self, self.caseDomSTOCKAGES, "caseDomSTOCKAGES", 10,230,250,18, mLibelleCase, "metier/doms.png", False, 0, 0)     
    #------   
    self.caseDomTOUS, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxDomTous), QtWidgets.QApplication.translate("bibli_ihm_camino", "All", None)
    genereObjets(self, self.caseDomTOUS, "caseDomTOUS", 10,5,250,18, mLibelleCase, "metier/tous.png", False, 0, 0)     
    #==============
    #Connections
    # Liste
    mListCaseDom = [self.caseDomMINERAUX, self.caseDomGRANULATS,   self.caseDomCARRIERES,  self.caseDomHYDRO,
                   self.caseDomCOMBU,    self.caseDomRADIOACTIFS, self.caseDomGEOTHERMIE, self.caseDomSTOCKAGES,  
                   self.caseDomTOUS
    ]
    # Id
    mListCaseDomCode = ["m", "w", "c", "h", "f", "r", "g", "s", "t"]
    mDicCaseDom = dict(zip(mListCaseDom, mListCaseDomCode))
    # connec
    genereConnexion(mListCaseDom)
    #=====================================================
    #Groupe Types
    self.groupBoxType = QtWidgets.QGroupBox(self.tab_widget_Critere)
    self.groupBoxType.setGeometry(QtCore.QRect(245,15,245,260))
    self.groupBoxType.setObjectName("groupBoxType") 
    mMess = QtWidgets.QApplication.translate("bibli_ihm_camino", "  Types  ", None)
    self.groupBoxType.setTitle(mMess)
    self.groupBoxType.setStyleSheet("QGroupBox { color: red; }")
    #------ 
    self.groupBoxTypeTous = QtWidgets.QGroupBox(self.tab_widget_Critere)
    self.groupBoxTypeTous.setGeometry(QtCore.QRect(245,280,245,30))
    self.groupBoxTypeTous.setObjectName("groupBoxTypeTous") 
    self.groupBoxTypeTous.setStyleSheet("QGroupBox { border : 1px solid #E4E4E4}")
    #------       
    self.caseTypePROSPECTIONS, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxType), QtWidgets.QApplication.translate("bibli_ihm_camino", "Authorization for pre-prospecting", None)
    genereObjets(self, self.caseTypePROSPECTIONS, "caseTypePROSPECTIONS", 10,20,250,18, mLibelleCase, "metier/typeautpro.png",
                False, 0, 0)     
    #------   
    self.caseTypeRECHERCHE, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxType), QtWidgets.QApplication.translate("bibli_ihm_camino", "Research authorization", None)
    genereObjets(self, self.caseTypeRECHERCHE, "caseTypeRECHERCHE", 10,50,250,18, mLibelleCase, "metier/typeautrec.png", False, 0, 0)     
    #------       
    self.caseTypePERMISRECHERCHE, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxType), QtWidgets.QApplication.translate("bibli_ihm_camino", "Exclusive license to search", None)
    genereObjets(self, self.caseTypePERMISRECHERCHE, "caseTypePERMISRECHERCHE", 10,80,250,18, mLibelleCase, "metier/typeperexclurec.png",
                False, 0, 0)     
    #------   
    self.caseTypeEXPLOITATION, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxType), QtWidgets.QApplication.translate("bibli_ihm_camino", "Authorization to operate", None)
    genereObjets(self, self.caseTypeEXPLOITATION, "caseTypeEXPLOITATION", 10,110,250,18, mLibelleCase, "metier/typeautexp.png", False, 0, 0)     
    #------       
    self.caseTypePERMISCARRIERES, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxType), QtWidgets.QApplication.translate("bibli_ihm_camino", "Exclusive Career Permit", None)
    genereObjets(self, self.caseTypePERMISCARRIERES, "caseTypePERMISCARRIERES", 10,140,250,18, mLibelleCase, "metier/typeperexclucar.png",
                False, 0, 0)     
    #------   
    self.caseTypePERMISEXPLOITATION, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxType), QtWidgets.QApplication.translate("bibli_ihm_camino", "Business Permit", None)
    genereObjets(self, self.caseTypePERMISEXPLOITATION, "caseTypePERMISEXPLOITATION", 10,170,250,18, mLibelleCase, "metier/typeperexploi.png", False, 0, 0)     
    #------       
    self.caseTypeCONCESSION, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxType), QtWidgets.QApplication.translate("bibli_ihm_camino", "Concession", None)
    genereObjets(self, self.caseTypeCONCESSION, "caseTypeCONCESSION", 10,200,250,18, mLibelleCase, "metier/typeconces.png", False, 0, 0)     
    #------   
    self.caseTypeTOUS, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxTypeTous), QtWidgets.QApplication.translate("bibli_ihm_camino", "All", None)
    genereObjets(self, self.caseTypeTOUS, "caseTypeTOUS", 10,5,250,18, mLibelleCase, "metier/tous.png", False, 0, 0)     
    #==============
    #Connections
    # Liste
    mListCaseType = [self.caseTypePROSPECTIONS,     self.caseTypeRECHERCHE,          self.caseTypePERMISRECHERCHE,  self.caseTypeEXPLOITATION,
                     self.caseTypePERMISCARRIERES,  self.caseTypePERMISEXPLOITATION, self.caseTypeCONCESSION,  
                     self.caseTypeTOUS
    ]
    # Id
    mListCaseTypeCode = ["ap", "ar", "pr", "ax", "pc", "px", "cx", "t"]
    mDicCaseType = dict(zip(mListCaseType, mListCaseTypeCode))
    # connec    
    genereConnexion(mListCaseType)
    #=====================================================
    # image traduction selon la langue choisie   
    overrideLocale = QSettings().value("locale/overrideFlag", False)
    localeFullName = QLocale.system().name() if not overrideLocale else QSettings().value("locale/userLocale", "")
    mLangue = localeFullName[0:2]
    # image traduction selon la langue choisie   
    #Groupe Statuts
    self.groupBoxStatuts = QtWidgets.QGroupBox(self.tab_widget_Critere)
    self.groupBoxStatuts.setGeometry(QtCore.QRect(500,15,280,170))
    self.groupBoxStatuts.setObjectName("groupBoxStatuts") 
    mMess = QtWidgets.QApplication.translate("bibli_ihm_camino", "  Statutes  ", None)
    self.groupBoxStatuts.setTitle(mMess)
    self.groupBoxStatuts.setStyleSheet("QGroupBox { color: red; }")
    #------ 
    self.groupBoxStatutsTous = QtWidgets.QGroupBox(self.tab_widget_Critere)
    self.groupBoxStatutsTous.setGeometry(QtCore.QRect(500,190,280,30))
    self.groupBoxStatutsTous.setObjectName("groupBoxStatutsTous") 
    self.groupBoxStatutsTous.setStyleSheet("QGroupBox { border : 1px solid #E4E4E4}")
    #------       
    self.caseStatusDEMANDEINIT, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxStatuts), QtWidgets.QApplication.translate("bibli_ihm_camino", "", None)                       
    genereObjets(self, self.caseStatusDEMANDEINIT, "caseStatusDEMANDEINIT", 10,20,250,18, mLibelleCase, "metier/statutdmi_" + mLangue + ".png", False, 120, 40)     
    #------   
    self.caseStatusDEMANDECLA, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxStatuts), QtWidgets.QApplication.translate("bibli_ihm_camino", "", None)
    genereObjets(self, self.caseStatusDEMANDECLA, "caseStatusDEMANDECLA", 10,50,250,18, mLibelleCase, "metier/statutdmc_" + mLangue + ".png", False, 120, 40)     
    #------   
    self.caseStatusVALIDE, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxStatuts), QtWidgets.QApplication.translate("bibli_ihm_camino", "", None)
    genereObjets(self, self.caseStatusVALIDE, "caseStatusVALIDE", 10,80,250,18, mLibelleCase, "metier/statutval_" + mLangue + ".png", False, 120, 40)     
    #------   
    self.caseStatusMODIF, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxStatuts), QtWidgets.QApplication.translate("bibli_ihm_camino", "", None)
    genereObjets(self, self.caseStatusMODIF, "caseStatusMODIF", 10,110,250,18, mLibelleCase, "metier/statutmod_" + mLangue + ".png", False, 200, 40)     
    #------   
    self.caseStatusECHU, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxStatuts), QtWidgets.QApplication.translate("bibli_ihm_camino", "", None) 
    genereObjets(self, self.caseStatusECHU, "caseStatusECHU", 10,140,250,18, mLibelleCase, "metier/statutec_" + mLangue + ".png", False, 120, 40)     
    #------   
    self.caseStatusTOUS, mLibelleCase = QtWidgets.QCheckBox(self.groupBoxStatutsTous), QtWidgets.QApplication.translate("bibli_ihm_camino", "All", None)
    genereObjets(self, self.caseStatusTOUS, "caseStatusTOUS", 10,5,250,18, mLibelleCase, "metier/tous.png", False, 0, 0)     
    #==============
    # Liste
    mListCaseStatus = [self.caseStatusDEMANDEINIT, self.caseStatusDEMANDECLA, self.caseStatusVALIDE, self.caseStatusMODIF,self.caseStatusECHU,  
                       self.caseStatusTOUS
    ]
    # Id
    mListCaseStatusCode = ["dmi", "dmc", "val", "mod", "ech", "t"]
    mDicCaseStatus = dict(zip(mListCaseStatus, mListCaseStatusCode))
    # connec      
    genereConnexion(mListCaseStatus)
    #=====================================================
    #Groupe Zones libres
    self.groupBoxZonelibre = QtWidgets.QGroupBox(self.tab_widget_Critere)
    self.groupBoxZonelibre.setGeometry(QtCore.QRect(500,225,280,175))
    self.groupBoxZonelibre.setObjectName("groupBoxZonelibre") 
    mMess = QtWidgets.QApplication.translate("bibli_ihm_camino", "  Titles and permissions  ", None)
    self.groupBoxZonelibre.setTitle(mMess)
    self.groupBoxZonelibre.setStyleSheet("QGroupBox { color: red; }")
    #------           
    self.labelZonelibreNOM = QtWidgets.QLabel(self.groupBoxZonelibre)
    self.labelZonelibreNOM.setGeometry(QtCore.QRect(10,20,70,18))
    self.labelZonelibreNOM.setObjectName("labelZonelibreNOM")
    self.labelZonelibreNOM.setAlignment(Qt.AlignRight)
    self.labelZonelibreNOM.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", "Names : ", None))
    self.textZonelibreNOM = QtWidgets.QLineEdit(self.groupBoxZonelibre)
    self.textZonelibreNOM.setGeometry(QtCore.QRect(90,20,180,23))
    self.textZonelibreNOM.setObjectName("textZonelibreNOM")        
    #------           
    self.labelZonelibreENTREPRISE = QtWidgets.QLabel(self.groupBoxZonelibre)
    self.labelZonelibreENTREPRISE.setGeometry(QtCore.QRect(10,50,70,18))
    self.labelZonelibreENTREPRISE.setObjectName("labelZonelibreENTREPRISE")
    self.labelZonelibreENTREPRISE.setAlignment(Qt.AlignRight)
    self.labelZonelibreENTREPRISE.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", "Companies : ", None))
    self.textZonelibreENTREPRISE = QtWidgets.QLineEdit(self.groupBoxZonelibre)
    self.textZonelibreENTREPRISE.setGeometry(QtCore.QRect(90,50,180,23))
    self.textZonelibreENTREPRISE.setObjectName("textZonelibreENTREPRISE")          
    #------           
    self.labelZonelibreSUBSTANCES = QtWidgets.QLabel(self.groupBoxZonelibre)
    self.labelZonelibreSUBSTANCES.setGeometry(QtCore.QRect(10,80,70,18))
    self.labelZonelibreSUBSTANCES.setObjectName("labelZonelibreSUBSTANCES")
    self.labelZonelibreSUBSTANCES.setAlignment(Qt.AlignRight)
    self.labelZonelibreSUBSTANCES.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", "Substances : ", None))
    self.textZonelibreSUBSTANCES = QtWidgets.QLineEdit(self.groupBoxZonelibre)
    self.textZonelibreSUBSTANCES.setGeometry(QtCore.QRect(90,80,180,23))
    self.textZonelibreSUBSTANCES.setObjectName("textZonelibreSUBSTANCES")   
    #------           
    self.labelZonelibreREFERENCES = QtWidgets.QLabel(self.groupBoxZonelibre)
    self.labelZonelibreREFERENCES.setGeometry(QtCore.QRect(10,110,70,18))
    self.labelZonelibreREFERENCES.setObjectName("labelZonelibreREFERENCES")
    self.labelZonelibreREFERENCES.setAlignment(Qt.AlignRight)
    self.labelZonelibreREFERENCES.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", "References : ", None))
    self.textZonelibreREFERENCES = QtWidgets.QLineEdit(self.groupBoxZonelibre)
    self.textZonelibreREFERENCES.setGeometry(QtCore.QRect(90,110,180,23))
    self.textZonelibreREFERENCES.setObjectName("textZonelibreREFERENCES")   
    #------           
    self.labelZonelibreTERRITOIRES = QtWidgets.QLabel(self.groupBoxZonelibre)
    self.labelZonelibreTERRITOIRES.setGeometry(QtCore.QRect(10,140,70,18))
    self.labelZonelibreTERRITOIRES.setObjectName("labelZonelibreTERRITOIRES")
    self.labelZonelibreTERRITOIRES.setAlignment(Qt.AlignRight)
    self.labelZonelibreTERRITOIRES.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", "Territories : ", None))
    self.textZonelibreTERRITOIRES = QtWidgets.QLineEdit(self.groupBoxZonelibre)                    
    self.textZonelibreTERRITOIRES.setGeometry(QtCore.QRect(90,140,180,23))
    self.textZonelibreTERRITOIRES.setObjectName("textZonelibreTERRITOIRES") 
    #==============
    #Liste Zones libres
    # Liste
    mListZoneLibre = [self.textZonelibreNOM, self.textZonelibreENTREPRISE, self.textZonelibreSUBSTANCES, self.textZonelibreREFERENCES,self.textZonelibreTERRITOIRES] 
    # Id
    mmListZoneLibreCode = ["noms", "entreprises", "substances", "references", "territoires"]
    mDicCaseZoneLibre = dict(zip(mListZoneLibre, mmListZoneLibreCode))     
    #=====================================================
    #Groupe gestion filtre avec boutons
    self.groupBoxFiltre = QtWidgets.QGroupBox(self.tab_widget_Critere)
    self.groupBoxFiltre.setGeometry(QtCore.QRect(15,320,475,80))
    self.groupBoxFiltre.setObjectName("groupBoxFiltre")
    
    _hgroupBoxFiltre = self.groupBoxFiltre.height() 
    _lgroupBoxFiltre = self.groupBoxFiltre.width()
    _ecartButton = 10
    _sizeWidthButton = (_lgroupBoxFiltre - (6 * _ecartButton)) / 5  
    _yButton = 15  
    _sizeHeigthButton = 23  
    #boutons territoires 
    self.buttonTout = QtWidgets.QPushButton(self.groupBoxFiltre)
    self.buttonTout.setGeometry(QtCore.QRect((1 * _ecartButton) + (0 * _sizeWidthButton), _yButton, _sizeWidthButton, _sizeHeigthButton))
    self.buttonTout.setObjectName("buttonTout")
    self.buttonTout.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", self.ToutLibelle, None))
    self.buttonTout.setVisible(True)
    self.buttonTout.setStyleSheet("QPushButton { border-style: outset; border-width: 1px; border-radius: 10px; border-color: #958B62; font: bold 10px; padding: 3px; }")    
    self.buttonTout.clicked.connect(lambda : genereFiltreUrlTerritoires(self, self.buttonTout, [mDicCaseDom, mDicCaseType, mDicCaseStatus, mDicCaseZoneLibre]))
    #-
    self.buttonMetropole = QtWidgets.QPushButton(self.groupBoxFiltre)
    self.buttonMetropole.setGeometry(QtCore.QRect((2 * _ecartButton) + (1 * _sizeWidthButton), _yButton, _sizeWidthButton, _sizeHeigthButton))
    self.buttonMetropole.setObjectName("buttonMetropole")
    self.buttonMetropole.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", self.MetropoleLibelle, None))
    self.buttonMetropole.setVisible(True)
    self.buttonMetropole.setStyleSheet("QPushButton { border-style: outset; border-width: 1px; border-radius: 10px; border-color: #958B62; font: bold 10px; padding: 3px; }")    
    self.buttonMetropole.clicked.connect(lambda : genereFiltreUrlTerritoires(self, self.buttonMetropole, [mDicCaseDom, mDicCaseType, mDicCaseStatus, mDicCaseZoneLibre]))
    #-
    self.buttonGuyane = QtWidgets.QPushButton(self.groupBoxFiltre)
    self.buttonGuyane.setGeometry(QtCore.QRect((3 * _ecartButton) + (2 * _sizeWidthButton) , _yButton, _sizeWidthButton, _sizeHeigthButton))
    self.buttonGuyane.setObjectName("buttonGuyane")
    self.buttonGuyane.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", self.GuyaneLibelle, None))
    self.buttonGuyane.setVisible(True)
    self.buttonGuyane.setStyleSheet("QPushButton { border-style: outset; border-width: 1px; border-radius: 10px; border-color: #958B62; font: bold 10px; padding: 3px; }")    
    self.buttonGuyane.clicked.connect(lambda : genereFiltreUrlTerritoires(self, self.buttonGuyane, [mDicCaseDom, mDicCaseType, mDicCaseStatus, mDicCaseZoneLibre]))
    #-
    self.buttonOceanIndien = QtWidgets.QPushButton(self.groupBoxFiltre)
    self.buttonOceanIndien.setGeometry(QtCore.QRect((4 * _ecartButton) + (3 * _sizeWidthButton) , _yButton, _sizeWidthButton, _sizeHeigthButton))
    self.buttonOceanIndien.setObjectName("buttonOceanIndien")
    self.buttonOceanIndien.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", self.OceanIndienLibelle, None))
    self.buttonOceanIndien.setVisible(True)
    self.buttonOceanIndien.setStyleSheet("QPushButton { border-style: outset; border-width: 1px; border-radius: 10px; border-color: #958B62; font: bold 10px; padding: 3px; }")    
    self.buttonOceanIndien.clicked.connect(lambda : genereFiltreUrlTerritoires(self, self.buttonOceanIndien, [mDicCaseDom, mDicCaseType, mDicCaseStatus, mDicCaseZoneLibre]))
    #-
    self.buttonAntilles = QtWidgets.QPushButton(self.groupBoxFiltre)
    self.buttonAntilles.setGeometry(QtCore.QRect((5 * _ecartButton) + (4 * _sizeWidthButton) , _yButton, _sizeWidthButton, _sizeHeigthButton))
    self.buttonAntilles.setObjectName("buttonAntilles")
    self.buttonAntilles.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", self.AntillesLibelle, None))
    self.buttonAntilles.setVisible(True)
    self.buttonAntilles.setStyleSheet("QPushButton { border-style: outset; border-width: 1px; border-radius: 10px; border-color: #958B62; font: bold 10px; padding: 3px; }")    
    self.buttonAntilles.clicked.connect(lambda : genereFiltreUrlTerritoires(self, self.buttonAntilles, [mDicCaseDom, mDicCaseType, mDicCaseStatus, mDicCaseZoneLibre]))
    #-
    #boutons territoires 
                                          
    #Filtre bouton filtre criteres 
    self.buttonFilterCritere = QtWidgets.QPushButton(self.groupBoxFiltre)
    self.buttonFilterCritere.setGeometry(QtCore.QRect(305,  _hgroupBoxFiltre - 34, 150, 33))
    self.buttonFilterCritere.setObjectName("buttonFilterCritere")
    self.buttonFilterCritere.setStyleSheet("QPushButton { color: red; }")
    #self.buttonFilterCritere.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", "layer loading", None))
    _buttonFilterCritereText  =        QtWidgets.QApplication.translate("bibli_ihm_camino", "layer loading", None)
    _buttonFilterCritereText += "\n" + QtWidgets.QApplication.translate("bibli_ihm_camino", "from the list of layers", None)
    self.buttonFilterCritere.setText(_buttonFilterCritereText)
    self.buttonFilterCritere.setVisible(True)
    self.buttonFilterCritere.setStyleSheet("QPushButton {\
                                color: red;              \
                                border-style: outset;    \
                                border-width: 2px;       \
                                border-radius: 10px;     \
                                border-color: blue;      \
                                font: bold 9px;         \
                                padding: 3px;            \
                                }")    
    #------   
    #Filtre bouton Sauvegarde filtre
    self.buttonFilterSave = QtWidgets.QPushButton(self.groupBoxFiltre)
    self.buttonFilterSave.setGeometry(QtCore.QRect(165, _hgroupBoxFiltre - 30, 120, 23))
    self.buttonFilterSave.setObjectName("buttonFilterSave")
    self.buttonFilterSave.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", "save the filter", None))
    self.buttonFilterSave.setVisible(True)
    #------       
    #Filtre bouton charger filtre
    self.buttonFilterLoad = QtWidgets.QPushButton(self.groupBoxFiltre)
    self.buttonFilterLoad.setGeometry(QtCore.QRect(25,  _hgroupBoxFiltre - 30, 120, 23))
    self.buttonFilterLoad.setObjectName("buttonFilterLoad")
    self.buttonFilterLoad.setText(QtWidgets.QApplication.translate("bibli_ihm_camino", "filter loading", None))
    self.buttonFilterLoad.setVisible(True)
    #------  
    #Connections boutons filtre
    self.buttonFilterCritere.clicked.connect(lambda : genereFiltreUrl(self, [mDicCaseDom, mDicCaseType, mDicCaseStatus, mDicCaseZoneLibre]))
    self.buttonFilterSave.clicked.connect(lambda : saveRequestCritere(self, [mDicCaseDom, mDicCaseType, mDicCaseStatus, mDicCaseZoneLibre]))
    self.buttonFilterLoad.clicked.connect(lambda : restoreRequestCritere(self, [mDicCaseDom, mDicCaseType, mDicCaseStatus,mDicCaseZoneLibre], 
                                                                                mListCaseDom, mListCaseType, mListCaseStatus, mListZoneLibre))
    self.mDicCaseDom, self.mDicCaseType, self.mDicCaseStatus, self.mDicCaseZoneLibre = mDicCaseDom, mDicCaseType, mDicCaseStatus, mDicCaseZoneLibre
    self.mListCaseDom, self.mListCaseType, self.mListCaseStatus, self.mListZoneLibre =  mListCaseDom, mListCaseType, mListCaseStatus, mListZoneLibre
    #------ Bouton multi filtre  
    self.buttonFilter.clicked.connect(lambda : loadOpenResultFilterMulti(self, self.vlayer,
                                                                                    self.mySource, self.fluxTitre, self.fluxProvider))
           
    return


#============================================ 
def restoreRequestCritere(self,mListDico, mListCaseDom, mListCaseType, mListCaseStatus, mListZoneLibre, mOption=None) : 
    carDebut, carFin = '[', ']'
    #------------
    urlDom, urlType, urlStatus                                       = "domainesIds", "typesIds", "statutsIds"
    urlCaseDico = [urlDom, urlType, urlStatus]
    urlNom, urlEntreprise, urlSubstance, urlReference, urlTerritoire = "noms", "entreprises", "substances", "references", "territoires"
    urlZoneLibreDico = [urlNom, urlEntreprise, urlSubstance, urlReference, urlTerritoire]
    if mOption == None :
       mFileOpen = mOpenFileName(self)[0]
    else :
       mFileOpen = self.initDirCaminoParam + "\\CAM_DEFAUT.camino"
       if not FileExiste(mFileOpen) : mFileOpen = '' 
    if mFileOpen != '' :
       #------------
       critDomDico, critTypeDico, critStatusDico, critZoneLibreDico = returnRequestCritere(mFileOpen, urlCaseDico, urlZoneLibreDico, carDebut, carFin)
       #------------
       if (len(critDomDico) + len(critTypeDico) + len(critStatusDico) + len(critZoneLibreDico)) == 0 :
          QMessageBox.warning(None,QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning", None),
                                 QtWidgets.QApplication.translate("bibli_ihm_camino", "No criteria entered.", None))
       else :
          for iCaseDico in range(len(urlCaseDico)) :
              #Pour les CheckBox 
              #J'efface                                                                                 
              for mKey, mValue in mListDico[iCaseDico].items():
                  mKey.setChecked(False)
              for mCrit in [critDomDico, critTypeDico, critStatusDico][iCaseDico] :
                  for mKey, mValue in mListDico[iCaseDico].items():
                      if (mCrit == mValue) : mKey.setChecked(True)
          #pour les Tous
          showHideCtrlCase("case",mListCaseDom)
          showHideCtrlCase("case",mListCaseType)
          showHideCtrlCase("case",mListCaseStatus)
          #Pour les QlineEdit (Zones Libres)                                                                              
          for iZoneLibreDico in range(len(urlZoneLibreDico)) :
              mListZoneLibre[iZoneLibreDico].setText('')
              mListZoneLibre[iZoneLibreDico].setText(critZoneLibreDico[iZoneLibreDico])

    return
#==================================================
def returnRequestCritere(mFileOpen, urlCaseDico, urlZoneLibreDico, carDebut, carFin):
    #Génération des listes
    sChaineDebut, sChaineFin = carDebut, carFin
    critDomDico, critTypeDico, critStatusDico, critZoneLibreDico = [], [], [],[]
     
    with open(mFileOpen, "r",encoding="utf-8") as mFileParam :
       #Pour les CheckBox
       for zFileParamLigne in mFileParam :
           for iCaseDico in range(len(urlCaseDico)) :
               sVar_bonne_ligne = urlCaseDico[iCaseDico]
               if sVar_bonne_ligne in zFileParamLigne :
                  listWithValue = []
                  #---------------
                  posInf = 0
                  while posInf < len(zFileParamLigne) :
                      if zFileParamLigne[posInf:posInf + 1] == sChaineDebut :
                         break
                      posInf += 1
                  #---------------
                  posSup = posInf + 1
                  while posSup < len(zFileParamLigne) :
                      if zFileParamLigne[posSup:posSup + 1] == sChaineFin : 
                         break
                      posSup += 1
                  slistWithValue = zFileParamLigne[posInf + 1:posSup]
                  #---------------
                  for sUnique in slistWithValue.split(",") :
                      sMyCle    = sUnique[sUnique.index("'") + 1 :].strip()
                      sMyValue  = sMyCle[0:sMyCle.index("'")].strip()
                      listWithValue.append(sMyValue)
                  #---------------
                  if iCaseDico == 0 :
                     critDomDico = listWithValue
                  elif iCaseDico == 1 :
                     critTypeDico = listWithValue
                  elif iCaseDico == 2 :
                     critStatusDico = listWithValue
                  
    with open(mFileOpen, "r",encoding="utf-8") as mFileParam :
       #Pour les QlineEdit (Zones Libres)
       for zFileParamLigne in mFileParam :
           for iZoneLibreDico in range(len(urlZoneLibreDico)) :
               sVar_bonne_ligne = urlZoneLibreDico[iZoneLibreDico]
               if sVar_bonne_ligne in zFileParamLigne :
                  listWithValue = []
                  #---------------
                  posInf = 0
                  while posInf < len(zFileParamLigne) :
                      if zFileParamLigne[posInf:posInf + 1] == sChaineDebut :
                         break
                      posInf += 1
                  #---------------
                  posSup = posInf + 1
                  while posSup < len(zFileParamLigne) :
                      if zFileParamLigne[posSup:posSup + 1] == sChaineFin : 
                         break
                      posSup += 1 
                  slistWithValue = zFileParamLigne[posInf + 1:posSup]
                  #---------------
                  sMyCle    = slistWithValue[slistWithValue.index("'") + 1 :].strip()
                  sMyValue  = sMyCle[0:sMyCle.index("'")].strip()
                  critZoneLibreDico.append(sMyValue)
 
    return critDomDico, critTypeDico, critStatusDico, critZoneLibreDico      

#============================================ 
def saveRequestCritere(self, mListDico, mOption=None) : 
    carDebut, carFin = '[', ']'
    if mOption == None :
       mFileSaveInit = "CAM_" + time.strftime("%Y%m%d_%Hh%Mm%S") + ".camino"
    else :
       mFileSaveInit = self.initDirCaminoParam + "\\CAM_DEFAUT.camino"
    #------------
    returListDom, returnListType, returnListStatus, returnListZoneLibre = returnValueCritere(mListDico)
    listCaseDico = [returListDom, returnListType, returnListStatus]
    urlDom, urlType, urlStatus                                       = "domainesIds", "typesIds", "statutsIds"
    urlCaseDico = [urlDom, urlType, urlStatus]
    urlNom, urlEntreprise, urlSubstance, urlReference, urlTerritoire = "noms", "entreprises", "substances", "references", "territoires"
    urlZoneLibreDico = [urlNom, urlEntreprise, urlSubstance, urlReference, urlTerritoire]
    if mOption == None :
       mFileSave = mSaveFileName(self, mFileSaveInit)[0]
    else :
       mFileSave = mFileSaveInit
    
    if mFileSave != '' :
       if (len(returListDom) + len(returnListType) + len(returnListStatus) + len(returnListZoneLibre)) == 0 :
          QMessageBox.warning(None,QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning", None),
                                 QtWidgets.QApplication.translate("bibli_ihm_camino", "No criteria entered.", None))
       else :
          zFileParam = open(mFileSave, "w",encoding="utf-8")
          zContenu = u"# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen\n"
          zContenu += u"# créé le " + time.strftime("%d ") + zMyFrenchMonth(float(time.strftime("%m"))) + time.strftime(" %Y - %Hh%Mm%Ss") + "\n"
          if mOption != None :
             zContenu += u"# Sauvegarde du filtre à la fermeture de la boite de dialogue CAMINO\n"
          zContenu += "\n"
          #Pour les CheckBox
          for iCaseDico in range(len(urlCaseDico)) :
              zContenu += urlCaseDico[iCaseDico] + " = " + carDebut
              if len(listCaseDico[iCaseDico]) == 0 :
                 zContenu += "'',"
              else :
                 for ll in listCaseDico[iCaseDico]:
                     zContenu += "'" + str(ll) + "',"
              zContenu = zContenu[:len(zContenu)-1] + carFin + "\n"
          #Pour les QlineEdit (Zones Libres)
          for iZoneLibreDico in range(len(urlZoneLibreDico)) :
              zContenu += urlZoneLibreDico[iZoneLibreDico] + " = " + carDebut
              zContenu += "'" + str(returnListZoneLibre[iZoneLibreDico]) + "',"
              zContenu = zContenu[:len(zContenu)-1] + carFin + "\n"
          zFileParam.write(zContenu)
          zFileParam.close()
    return
    
#============================================ 
def mOpenFileName(self):
    #Ouverture de la boite de dialogue Fichiers
    InitDir = createFolder(self.initDirCaminoParam + "\\requete")
    TypeList = QtWidgets.QApplication.translate("bibli_ihm_camino", "Camino Request", None) + " (*.camino)"
    fileName = QFileDialog.getOpenFileName(None,QtWidgets.QApplication.translate("bibli_ihm_camino", "Camino Files :", None),InitDir,TypeList)
    return fileName
   
#============================================ 
def mSaveFileName(self, mFileSaveInit):
    #Sauvegarde de la boite de dialogue Fichiers
    InitDir = createFolder(self.initDirCaminoParam + "\\requete\\") + mFileSaveInit 
    TypeList = QtWidgets.QApplication.translate("bibli_ihm_camino", "Camino Request", None) + " (*.camino)"
    fileName = QFileDialog.getSaveFileName(None,QtWidgets.QApplication.translate("bibli_ihm_camino", "Camino Files :", None),InitDir,TypeList)
    return fileName
    
#============================================ 
def genereFiltreUrlTerritoires(self, mButton, mListDico) : 
    returListDom, returnListType, returnListStatus, returnListZoneLibre = returnValueCritere(mListDico)
    listCaseDico = [returListDom, returnListType, returnListStatus]

    if (len(returListDom) + len(returnListType) + len(returnListStatus) + len(returnListZoneLibre)) == 0 :
        QMessageBox.warning(None,QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning", None),
                                 QtWidgets.QApplication.translate("bibli_ihm_camino", "No criteria entered.", None))
    else :
       urlDom, urlType, urlStatus                                       = "domainesIds", "typesIds", "statutsIds"
       urlCaseDico = [urlDom, urlType, urlStatus]
       # Pour infos Mapping     Corresponds aux attributs
       # "noms", "entreprises",     "substances", "references", "territoires"
       # "nom",  "titulaires_noms", "substances", "references", "régions"
       urlNom, urlEntreprise, urlSubstance, urlReference, urlTerritoire = "noms", "entreprises", "substances", "references", "territoires"
       urlZoneLibreDico = [urlNom, urlEntreprise, urlSubstance, urlReference, urlTerritoire]
       urlCaseOk, mFirst, mOpe = "", True, ""
       #Pour les CheckBox
       for iCaseDico in range(len(urlCaseDico)) :
           if len(listCaseDico[iCaseDico]) != 0 :
              urlCaseDico[iCaseDico] += "={}".format(','.join(mIds for mIds in listCaseDico[iCaseDico])) 
              urlCaseOk =  urlCaseOk + mOpe + urlCaseDico[iCaseDico]
              if mFirst : mFirst, mOpe = False, "&"
       #Pour les QlineEdit (Zones Libres)
       for iZoneLibreDico in range(len(urlZoneLibreDico)) :
           if returnListZoneLibre[iZoneLibreDico] != '' :
              urlZoneLibreDico[iZoneLibreDico] += "=" + returnListZoneLibre[iZoneLibreDico].replace(" ","%20")
              urlCaseOk =  urlCaseOk + mOpe + urlZoneLibreDico[iZoneLibreDico]
              if mFirst : mFirst, mOpe = False, "&"
    #=============
    idenCourriel = self.textEditCourriel.toPlainText()
    mdpCourriel  = self.textEditMdpCourriel.toPlainText()     
    mContinue = False
    
    if self.radioOptionMdp3.isChecked() :
       if (idenCourriel == "" or mdpCourriel == "") :
          myTokenTitre = QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning !!", None)
          myToken = QtWidgets.QApplication.translate("bibli_ihm_camino", "Please enter your mail address and password please.", None)
          QMessageBox.warning(None, myTokenTitre,myToken)
       else :
          mGestionLoginCourriel("SAVE", self.monFichierPathLoginCourriel, idenCourriel) 
          mContinue = True
    else :
       mContinue = True

    if mContinue :
       #Charge le flux camino teste si la couche t valide et après le résultat
       #Gestion des territoires                                                              
       _urlDefaut = self.UrlcaminoDefaut
       if mButton.objectName()   == "buttonTout" :
          mySource  = _urlDefaut   
          fluxTitre = self.ToutLibelle
       elif mButton.objectName() == "buttonMetropole" :
          mySource  = _urlDefaut + "&perimetre=" + "&perimetre=".join(self.MetropoleCoord)   
          fluxTitre = self.MetropoleLibelle
       elif mButton.objectName() == "buttonGuyane" : 
          mySource  = _urlDefaut + "&perimetre=" + "&perimetre=".join(self.GuyaneCoord)   
          fluxTitre = self.GuyaneLibelle
       elif mButton.objectName() == "buttonOceanIndien" : 
          mySource  = _urlDefaut + "&perimetre=" + "&perimetre=".join(self.OceanIndienCoord)   
          fluxTitre = self.OceanIndienLibelle
       elif mButton.objectName() == "buttonAntilles" : 
          mySource  = _urlDefaut + "&perimetre=" + "&perimetre=".join(self.AntillesCoord)   
          fluxTitre = self.AntillesLibelle
       fluxProvider = 'ogr' 
       #============
       #Gestion de l'adresse et du login
       mFindCaminoAdresse, mCodeUrl, mSepMdp, mSepAdresse = "https://", "%40", ":", "@"  
       mPos = mySource.find(mFindCaminoAdresse)
       if mPos == -1 :
          urlMySourceLogin = mySource
       else :
          if self.radioOptionMdp3.isChecked() :
             idenCourriel = idenCourriel.replace(mSepAdresse, mCodeUrl)
             urlMySourceLogin = mySource[0:len(mFindCaminoAdresse)] + idenCourriel + mSepMdp + mdpCourriel + mSepAdresse + mySource[len(mFindCaminoAdresse):]
             mySource = urlMySourceLogin
       #============
       QApplication.instance().setOverrideCursor(Qt.WaitCursor)
       vlayer = QgsVectorLayer(mySource, fluxTitre, fluxProvider) 

       if not vlayer.isValid():
          QApplication.instance().setOverrideCursor(Qt.ArrowCursor)
          zMessErrorLoadLayerTitre = QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning !!", None)                          
          zMessErrorLoadLayerTraduction1 = QtWidgets.QApplication.translate("bibli_ihm_camino", "Layer loading :", None)
          zMessErrorLoadLayerTraduction2 = QtWidgets.QApplication.translate("bibli_ihm_camino", "Please check your connections.", None)       
          #zMessErrorLoadLayer = zMessErrorLoadLayerTraduction1 + " "  + str(fluxTitre) + "\n" + str(mySource) + "\n\n" + zMessErrorLoadLayerTraduction2
          #suppression de la source cas ou il y a le mot de passe 
          zMessErrorLoadLayer = zMessErrorLoadLayerTraduction1 + " "  + str(fluxTitre) + "\n\n" + zMessErrorLoadLayerTraduction2
          QMessageBox.warning(None, zMessErrorLoadLayerTitre, zMessErrorLoadLayer)
       else :
          if urlCaseOk != "" :  #Gestion du pt ? 
             if mySource.find("?") == -1 :
                mySource += "?" + urlCaseOk
             else :
                mySource += "&" + urlCaseOk
             #Gestion du nom de la couche si mdp ou pas
             fluxTitre = QtWidgets.QApplication.translate("bibli_ihm_camino", "Camino => Filter with criteria", None)
           
          vlayer = QgsVectorLayer(mySource, fluxTitre, fluxProvider)
          if not vlayer.isValid():
             QApplication.instance().setOverrideCursor(Qt.ArrowCursor)
             zMessErrorLoadLayerTitre = QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning !!", None)                          
             zMessErrorLoadLayerTraduction1 = QtWidgets.QApplication.translate("bibli_ihm_camino", "Layer loading :", None)
             zMessErrorLoadLayerTraduction2 = QtWidgets.QApplication.translate("bibli_ihm_camino", "No results.", None)       
             zMessErrorLoadLayer = zMessErrorLoadLayerTraduction1 + " "  + str(fluxTitre) + "\n" + str(mySource) + "\n\n" + zMessErrorLoadLayerTraduction2
             QMessageBox.warning(None, zMessErrorLoadLayerTitre, zMessErrorLoadLayer)
          else :
             #------     
             fluxAdresse = mySource
             #------     
             self.resultTextEdit.clear()
             zMess = self.zMess
             zMess += self.zMess3 + " : \t" + str(fluxAdresse) + "\n"
             zMess += self.zMess4 + " : \t" + str(fluxTitre) + "\n"
             zMess += self.zMess5 + " : \t" + str(fluxProvider)
             self.resultTextEdit.setText(zMess)       
             #------  
             self.mySource,self.fluxTitre,self.fluxProvider = mySource,fluxTitre,fluxProvider
             QApplication.instance().setOverrideCursor(Qt.WaitCursor)
             openLayer(self, self.mySource,self.fluxTitre,self.fluxProvider)               
             QApplication.instance().setOverrideCursor(Qt.ArrowCursor)
             
    #=============
    return

#============================================ 
def genereFiltreUrl(self, mListDico) : 
    returListDom, returnListType, returnListStatus, returnListZoneLibre = returnValueCritere(mListDico)
    listCaseDico = [returListDom, returnListType, returnListStatus]

    if (len(returListDom) + len(returnListType) + len(returnListStatus) + len(returnListZoneLibre)) == 0 :
        QMessageBox.warning(None,QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning", None),
                                 QtWidgets.QApplication.translate("bibli_ihm_camino", "No criteria entered.", None))
    else :
       urlDom, urlType, urlStatus                                       = "domainesIds", "typesIds", "statutsIds"
       urlCaseDico = [urlDom, urlType, urlStatus]
       # Pour infos Mapping     Corresponds aux attributs
       # "noms", "entreprises",     "substances", "references", "territoires"
       # "nom",  "titulaires_noms", "substances", "references", "régions"
       urlNom, urlEntreprise, urlSubstance, urlReference, urlTerritoire = "noms", "entreprises", "substances", "references", "territoires"
       urlZoneLibreDico = [urlNom, urlEntreprise, urlSubstance, urlReference, urlTerritoire]
       urlCaseOk, mFirst, mOpe = "", True, ""
       #Pour les CheckBox
       for iCaseDico in range(len(urlCaseDico)) :
           if len(listCaseDico[iCaseDico]) != 0 :
              urlCaseDico[iCaseDico] += "={}".format(','.join(mIds for mIds in listCaseDico[iCaseDico])) 
              urlCaseOk =  urlCaseOk + mOpe + urlCaseDico[iCaseDico]
              if mFirst : mFirst, mOpe = False, "&"
       #Pour les QlineEdit (Zones Libres)
       for iZoneLibreDico in range(len(urlZoneLibreDico)) :
           if returnListZoneLibre[iZoneLibreDico] != '' :
              urlZoneLibreDico[iZoneLibreDico] += "=" + returnListZoneLibre[iZoneLibreDico].replace(" ","%20")
              urlCaseOk =  urlCaseOk + mOpe + urlZoneLibreDico[iZoneLibreDico]
              if mFirst : mFirst, mOpe = False, "&"
    #=============
    idenCourriel = self.textEditCourriel.toPlainText()
    mdpCourriel  = self.textEditMdpCourriel.toPlainText()     
    mContinue = False
    
    if self.radioOptionMdp3.isChecked() :
       if (idenCourriel == "" or mdpCourriel == "") :
          myTokenTitre = QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning !!", None)
          myToken = QtWidgets.QApplication.translate("bibli_ihm_camino", "Please enter your mail address and password please.", None)
          QMessageBox.warning(None, myTokenTitre,myToken)
       else :
          mGestionLoginCourriel("SAVE", self.monFichierPathLoginCourriel, idenCourriel) 
          mContinue = True
    else :
       mContinue = True
       
    if mContinue :
       #Charge le flux camino teste si la couche t valide et après le résultat
       mySource = self.returnAdresse[self.comboAdresse.currentIndex()][0]
       fluxTitre    = self.returnAdresse[self.comboAdresse.currentIndex()][1]
       fluxProvider = self.returnAdresse[self.comboAdresse.currentIndex()][2]
       fluxProvider = 'ogr' 
       #============
       #Gestion de l'adresse et du login
       mFindCaminoAdresse, mCodeUrl, mSepMdp, mSepAdresse = "https://", "%40", ":", "@"  
       mPos = mySource.find(mFindCaminoAdresse)
       if mPos == -1 :
          urlMySourceLogin = mySource
       else :
          if self.radioOptionMdp3.isChecked() :
             idenCourriel = idenCourriel.replace(mSepAdresse, mCodeUrl)
             urlMySourceLogin = mySource[0:len(mFindCaminoAdresse)] + idenCourriel + mSepMdp + mdpCourriel + mSepAdresse + mySource[len(mFindCaminoAdresse):]
             mySource = urlMySourceLogin
       #============
       QApplication.instance().setOverrideCursor(Qt.WaitCursor)
       vlayer = QgsVectorLayer(mySource, fluxTitre, fluxProvider) 

       if not vlayer.isValid():
          QApplication.instance().setOverrideCursor(Qt.ArrowCursor)
          zMessErrorLoadLayerTitre = QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning !!", None)                          
          zMessErrorLoadLayerTraduction1 = QtWidgets.QApplication.translate("bibli_ihm_camino", "Layer loading :", None)
          zMessErrorLoadLayerTraduction2 = QtWidgets.QApplication.translate("bibli_ihm_camino", "Please check your connections.", None)       
          #zMessErrorLoadLayer = zMessErrorLoadLayerTraduction1 + " "  + str(fluxTitre) + "\n" + str(mySource) + "\n\n" + zMessErrorLoadLayerTraduction2
          #suppression de la source cas ou il y a le mot de passe 
          zMessErrorLoadLayer = zMessErrorLoadLayerTraduction1 + " "  + str(fluxTitre) + "\n\n" + zMessErrorLoadLayerTraduction2
          QMessageBox.warning(None, zMessErrorLoadLayerTitre, zMessErrorLoadLayer)
       else :
          if urlCaseOk != "" :  #Gestion du pt ? 
             if mySource.find("?") == -1 :
                mySource += "?" + urlCaseOk
             else :
                mySource += "&" + urlCaseOk
             #Gestion du nom de la couche si mdp ou pas
             fluxTitre = QtWidgets.QApplication.translate("bibli_ihm_camino", "Camino => Filter with criteria", None)
           
          vlayer = QgsVectorLayer(mySource, fluxTitre, fluxProvider)
          if not vlayer.isValid():
             QApplication.instance().setOverrideCursor(Qt.ArrowCursor)
             zMessErrorLoadLayerTitre = QtWidgets.QApplication.translate("bibli_ihm_camino", "Warning !!", None)                          
             zMessErrorLoadLayerTraduction1 = QtWidgets.QApplication.translate("bibli_ihm_camino", "Layer loading :", None)
             zMessErrorLoadLayerTraduction2 = QtWidgets.QApplication.translate("bibli_ihm_camino", "No results.", None)       
             zMessErrorLoadLayer = zMessErrorLoadLayerTraduction1 + " "  + str(fluxTitre) + "\n" + str(mySource) + "\n\n" + zMessErrorLoadLayerTraduction2
             QMessageBox.warning(None, zMessErrorLoadLayerTitre, zMessErrorLoadLayer)
          else :
             #------     
             fluxAdresse = mySource
             #------     
             self.resultTextEdit.clear()
             zMess = self.zMess
             zMess += self.zMess3 + " : \t" + str(fluxAdresse) + "\n"
             zMess += self.zMess4 + " : \t" + str(fluxTitre) + "\n"
             zMess += self.zMess5 + " : \t" + str(fluxProvider)
             self.resultTextEdit.setText(zMess)       
             #------  
             self.mySource,self.fluxTitre,self.fluxProvider = mySource,fluxTitre,fluxProvider
             QApplication.instance().setOverrideCursor(Qt.WaitCursor)
             openLayer(self, self.mySource,self.fluxTitre,self.fluxProvider)               
             QApplication.instance().setOverrideCursor(Qt.ArrowCursor)
             
    #=============
    return

#============================================ 
def returnValueCritere(mListDico) :
    mReturListDom, mReturnListType, mReturnListStatus, mReturnListZoneLibre = [], [], [], []
    mReturnListDico = [mReturListDom, mReturnListType, mReturnListStatus, mReturnListZoneLibre]
    
    for iParamDico in range(len(mListDico)) :
        #Pour les CheckBox
        if iParamDico < (len(mListDico) - 1) :  
           for mKey, mValue in mListDico[iParamDico].items() :
               if mValue != "t" :   # exclure les "Tous"
                  if mKey.isChecked() : mReturnListDico[iParamDico].append(mValue)
        #Pour les QlineEdit (Zones Libres)
        else :
           for mKey, mValue in mListDico[iParamDico].items() :
               mReturnListDico[iParamDico].append(mKey.text() if (mKey.text() != '') else '')
                                      
    return mReturListDom, mReturnListType, mReturnListStatus, mReturnListZoneLibre
    
#============================================        
def genereConnexion(mListCaseParam) :
    for i in range(len(mListCaseParam)):
        if i < (len(mListCaseParam) - 1) :
           mListCaseParam[i].clicked.connect(lambda : showHideCtrlCase("case", mListCaseParam))
        else :
           mListCaseParam[i].clicked.connect(lambda : showHideCtrlCase("tous", mListCaseParam))
    return 
    
#============================================        
def genereObjets(self, mNameObjet, mName, mX, mY, mL, mH, mLibelle, mIcon, mEtat, mIconX, mIconY) :
    mNameObjet.setGeometry(QtCore.QRect(mX, mY, mL, mH))
    mNameObjet.setObjectName(mName)
    mNameObjet.setText(mLibelle)
    mNameObjet.setIcon(self.returnIcon(bibli_camino.getThemeIcon(mIcon)))
    if mIconX != 0 :
       mNameObjet.setIconSize(QSize(mIconX,mIconY))
    mNameObjet.setChecked(mEtat)
    return  

      
#============================================        
def showHideCtrlCase(mType, mListCase) :
    iDisplay = 0                  
    for i in mListCase :
        if i.isChecked() : iDisplay += 1
    if mListCase[len(mListCase)-1].isChecked() : iDisplay -= 1
    #------           
    if mType == "case" :
      mFlag = (False if (iDisplay < (len(mListCase)-1)) else True)
      mListCase[len(mListCase)-1].setChecked(mFlag)
    #------           
    elif mType == "tous" :
      mFlag = (True if mListCase[len(mListCase)-1].isChecked() else False)
      for i in range(len(mListCase) - 1) :
          if i < len(mListCase) - 1 : mListCase[i].setChecked(mFlag)
    return  

#==================================================
#Execute Pdf 
#==================================================
def execPdf(nameciblePdf):
    
    paramGlob = nameciblePdf            
    os.startfile(paramGlob)

    return       
#============================================  
      
#============================================ 
def mGestionLoginCourriel(mType, mFile, mIden) :

    if mType == "SAVE" :
       carDebut, carFin = '[', ']'
       zFileParam = open(mFile, "w",encoding="utf-8")
       zContenu = u"# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen\n"
       zContenu += u"# créé le " + time.strftime("%d ") + zMyFrenchMonth(float(time.strftime("%m"))) + time.strftime(" %Y - %Hh%Mm%Ss") + "\n"
       zContenu += "\n"
       zContenu += "IDEN = " + carDebut + mIden + carFin + "\n"
       zFileParam.write(zContenu)
       zFileParam.close()
       return
    elif mType == "RESTORE" :
       if FileExiste(mFile) :
          carDebut, carFin, mIden, mOrga, mListeLogin = '[', ']', '', '', ["IDEN"]
          with open(mFile, "r",encoding="utf-8") as mFileParam :
               for zFileParamLigne in mFileParam :
                   for i in range(len(mListeLogin)) :
                       sVar_bonne_ligne = mListeLogin[i]

                       if sVar_bonne_ligne in zFileParamLigne :
                          slistWithValue = ""
                          #---------------
                          posInf = 0
                          while posInf < len(zFileParamLigne) :
                                if zFileParamLigne[posInf:posInf + 1] == carDebut :
                                   break
                                posInf += 1
                          #---------------
                          posSup = posInf + 1
                          while posSup < len(zFileParamLigne) :
                                if zFileParamLigne[posSup:posSup + 1] == carFin : 
                                   break
                                posSup += 1
                          slistWithValue = zFileParamLigne[posInf + 1:posSup]
                          #---------------
                          if sVar_bonne_ligne == "IDEN" :
                             mIden = slistWithValue
       return mIden
#==================================================
def returnVersion() : return "version 1.7.0"
#============================================ 
         