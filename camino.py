# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen
# créé mars 2020 version 1.0


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QAction, QMenu , QApplication, QMessageBox
from PyQt5.QtGui import QIcon

from qgis.core import *
from qgis.gui import *

import os
from . import doAbout
from . import docamino_onglet_ui
from . import bibli_camino
from .bibli_camino import *

class MainPlugin(object):
  def __init__(self, iface):
     self.name = "CAMINO (camino)"
     self.iface = iface
    
     # Generation de la traduction selon la langue choisie   
     overrideLocale = QSettings().value("locale/overrideFlag", False)
     localeFullName = QLocale.system().name() if not overrideLocale else QSettings().value("locale/userLocale", "")
     self.localePath = os.path.dirname(__file__) + "/i18n/camino_" + localeFullName[0:2] + ".qm"
     if QFileInfo(self.localePath).exists():
        self.translator = QTranslator()
        self.translator.load(self.localePath)
        QCoreApplication.installTranslator(self.translator)
     # Generation de la traduction selon la langue choisie   

  def initGui(self):
     #Construction du menu
     self.menu=QMenu("CAMINO (mining titles) International")
     self.menu.setTitle(QtWidgets.QApplication.translate("camino_main", "CAMINO (mining titles) International"))

     menuIcon = bibli_camino.getThemeIcon("camino2.png")
     self.camino2 = QAction(QIcon(menuIcon),"CAMINO (mining titles) International...",self.iface.mainWindow())
     self.camino2.setText(QtWidgets.QApplication.translate("camino_main", "CAMINO (mining titles) International..."))
     self.camino2.triggered.connect(self.clickIHMcamino2)
     
     menuIcon = bibli_camino.getThemeIcon("about.png")
     self.about = QAction(QIcon(menuIcon), "About ...", self.iface.mainWindow())
     self.about.setText(QtWidgets.QApplication.translate("camino_main", "About ..."))
     self.about.triggered.connect(self.clickAbout)
    
     #Construction du menu
     self.menu.addAction(self.camino2)
     self.menu.addSeparator()
     self.menu.addAction(self.about)

     #=========================
     #Ajouter une barre d'outils'
     menuBar = self.iface.mainWindow().menuBar()    
     zMenu = menuBar
     for child in menuBar.children():
         if child.objectName()== "mPluginMenu" :
            zMenu = child
            break
     zMenu.addMenu(self.menu)
     #-- Ajout du menu

     self.toolBarName = QtWidgets.QApplication.translate("camino_main", "My tool bar CAMINO (mining titles)")
     self.toolbar = self.iface.addToolBar(self.toolBarName)
     # Pour faire une action
     self.toolbar.addAction(self.camino2)
     self.toolbar.addSeparator()
     self.toolbar.addAction(self.about)
     #=========================
    
     #Méthode au déchargement de l'extension
     def unload(self): pass   
     
  def clickAbout(self):
      d = doAbout.Dialog()
      d.exec_()

  def clickIHMcamino2(self):
      d = docamino_onglet_ui.Dialog()
      d.exec_()

  def unload(self):
      pass   




  