# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen
# créé mars 2020 version 1.0

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QAction, QMenu , QApplication, QMessageBox, QFileDialog, QTextEdit, QMainWindow, 
                            QTableView, QDockWidget, QVBoxLayout, QTabWidget, QWidget, QAbstractItemView)
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
 
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *

from qgis.core import QgsProject,QgsMapLayer, QgsVectorLayerCache, QgsFeatureRequest
from qgis.gui import (QgsAttributeTableModel, QgsAttributeTableView, QgsLayerTreeViewMenuProvider, QgsAttributeTableFilterModel)
from qgis.utils import iface

from qgis.core import *
from qgis.gui import *
import qgis                              
import os                       
import datetime
import os.path
import time

#==================================================
#Alimentation de la ComboBox Filter
#==================================================
def alimDicComboFilter(self, dicResultId, dicResultAttrib) :
    modelComboFilter = QStandardItemModel()
    for key, value in dicResultAttrib.items() :
        valueCombo = ''
        for mAttribFeat in value :
            valueCombo += "%s >>" %(str(mAttribFeat))
        modelComboFilterCol1 = QStandardItem(str(valueCombo[0:len(valueCombo)-3]))
        modelComboFilterCol2 = QStandardItem(str(key))
        modelComboFilter.appendRow([modelComboFilterCol1, modelComboFilterCol2])
           
    self.resultFilterCombo.setModel(modelComboFilter)

#==================================================
#Alimentation Dico Filter
#==================================================
def alimDicSelect(self,vlayer,dicListId, dicListAttrib) :                            
    dicResultId, dicResultAttrib = {}, {}
    mProvider, mAllValues = vlayer.dataProvider(), vlayer.getFeatures(QgsFeatureRequest())
    mListFieldName = [ mField.name() for mField in mProvider.fields() ]
    nbFeat, countNbFeat  = mProvider.featureCount(), 0
                                                                                                                                            
    #Boucle sur les enrg
    #Création d'un dictionnaire key, value
    for mValue in mAllValues:
        listResultId, listResultAttrib = [], []
        mMonDic = dict(zip(mListFieldName, mValue.attributes()))                        
        for mAttrib in dicListAttrib :
            for key in mMonDic.keys() :
                if key == mAttrib :
                   listResultAttrib.append(mMonDic[key])
        for mId in dicListId :
            for key in mMonDic.keys() :
                if key == mId :
                   listResultId.append(mMonDic[key])
        dicResultId[countNbFeat], dicResultAttrib[countNbFeat]  = listResultId, listResultAttrib
                  
        countNbFeat +=1

    return dicResultId, dicResultAttrib 
        
#==================================================
#Fonction Open Layer
#==================================================
def openLayer(self, mySource,fluxTitre,fluxProvider):
                    
    vlayer = QgsVectorLayer(mySource, fluxTitre, fluxProvider)
    
    if not vlayer.isValid():
       zMessErrorLoadLayerTitre = QtWidgets.QApplication.translate("bibli_camino", "Warning !!", None)                          
       zMessErrorLoadLayerTraduction1 = QtWidgets.QApplication.translate("bibli_camino", "Layer loading :", None)
       zMessErrorLoadLayerTraduction2 = QtWidgets.QApplication.translate("bibli_camino", "Please check your connections.", None)       
       zMessErrorLoadLayer = zMessErrorLoadLayerTraduction1 + " "  + str(fluxTitre) + "\n" + str(mySource) + "\n\n" + zMessErrorLoadLayerTraduction2
       QMessageBox.warning(None, zMessErrorLoadLayerTitre, zMessErrorLoadLayer)
    else :   
       QgsProject.instance().addMapLayer(vlayer)
       mCanvas = iface.mapCanvas()
       mCanvas.setExtent(vlayer.extent())
       openResultFilter(self, mySource, fluxTitre, fluxProvider)   # Onglet 1
       self.tabWidget.setCurrentIndex(0)
    return

#==================================================                                                          
#Fonction Return Index Row
#==================================================
def returnIndexRow():
    mIndexesTable_view = table_view.currentIndex()
    mIndex = mIndexesTable_view.row()
    return mReturnIndexRow
    
#==================================================
#Fonction Open Filter
#==================================================
def openResultFilter(self, mySource, fluxTitre,fluxProvider) :
    self.resulFilter.setText(QtWidgets.QApplication.translate("bibli_camino", "", None))
    self.vlayer = iface.activeLayer()
    self.resultFilterCanvas = QgsMapCanvas()
    self.vector_layer_cache = QgsVectorLayerCache(self.vlayer, 10000)
    self.filter_attribute_table_model = QgsAttributeTableModel(self.vector_layer_cache)
    self.filter_attribute_table_model.loadLayer()
    #--------------
    self.filter_attribute_table_filter_model = QgsAttributeTableFilterModel(self.resultFilterCanvas, self.filter_attribute_table_model)
    #--------------
    self.filter_table_view = QTableView(self.resulFilter)
    self.filter_table_view.setSelectionBehavior(QAbstractItemView.SelectRows) # Mode de selection
    self.filter_table_view.setModel(self.filter_attribute_table_filter_model)
    self.filter_table_view.resize(776, 365)
    #--------------
    self.filter_table_view.show()
    #--------------
    self.filter_table_view.clicked.connect(lambda : displayButtonFilterMulti(self))
    self.filter_table_view.doubleClicked.connect(lambda : loadOpenResultFilter(self, self.filter_table_view, self.filter_attribute_table_model, 
                                                                                    mySource, fluxTitre,fluxProvider))
    self.buttonFilter.setVisible(True)
    return

#==================================================
#Affichage du bouton Filtre des couches filtrées sur simple Click
#==================================================
def displayButtonFilterMulti(self) :
    mListRowsSelected = self.filter_table_view.selectionModel().selectedRows()    
    self.buttonFilter.setEnabled(True) if len(mListRowsSelected) > 1 else self.buttonFilter.setEnabled(False)
    self.labelOccurrence.setText(str(len(mListRowsSelected)) + QtWidgets.QApplication.translate("bibli_camino", " selected objects", None))
    self.labelOccurrence.show() if len(mListRowsSelected) > 1 else self.labelOccurrence.hide()
    return  
                                                   
#==================================================
#Fonction chargement des couches filtrées sur simple Click
#==================================================
def loadOpenResultFilterMulti(self, vlayer,
                                    mySource, fluxTitre, fluxProvider) :
    mNameAttribut = "id"
    posColumId = returnPosColumn(self,vlayer, mNameAttribut)
    mListRowsSelected = [] 
    mListRowsSelected = self.filter_table_view.selectionModel().selectedRows()    
    mListCellRowsSelected = self.filter_table_view.selectedIndexes()
    mListValueFilter = []
    
    for oSelected in mListRowsSelected :
        r, c = oSelected.row(), posColumId
        mListValueFilter.append(str(oSelected.sibling(r, c).data()))

    mRequest = u"id IN ({})".format(','.join("'" + mId + "'" for mId in mListValueFilter)) 
    mMessSelect = QtWidgets.QApplication.translate("bibli_camino", "selections", None)
    fluxTitre = 'Camino ==>  ' + str(len(mListRowsSelected)) + ' ' + mMessSelect
    openLayerFilterSimpleClick(self, mySource,fluxTitre,fluxProvider, mRequest)
           
    return
        
#==================================================
#Retour position colum par rapport au nom
#==================================================
def returnPosColumn(self,vlayer, mNameAttribut) :                            
    mProvider, mPosAttribut = vlayer.dataProvider(), 0
    mFindField = False
    for mField in mProvider.fields():
        if mField.name().upper() == mNameAttribut.upper() :
           mReturnPosColumn = mPosAttribut
           mFindField = True
        else : 
           mPosAttribut += 1
    return mReturnPosColumn if mFindField else 0
    
#==================================================
#Fonction chargement de la couche filtrée sur Double Click
#==================================================
def loadOpenResultFilter(self, filter_table_view, filter_attribute_table_model, 
                               mySource, fluxTitre, fluxProvider) :

    indexAll = filter_table_view.currentIndex()
    #Retourne l'index de la ligne courant sélectionné dans la vue
    mindex = indexAll.row()
    #Retourne le model par défaut
    mModel = QModelIndex()
    #Retourne le model de la table filter par défaut
    mModelAttribut = filter_attribute_table_model
    #le nombre de colonne
    nbColAttribut = mModelAttribut.columnCount(mModel)

    for i in range(nbColAttribut) :
        #Retourne la valeur
        mRowSelect = mModelAttribut.index(mindex,i,mModel)
        mValueFilter = str(mModelAttribut.data(mRowSelect, 0))
        if i == 0 :
           mIdFilter = "id"  
           mRequest = mIdFilter + " = '" + str(mValueFilter)  + "'"
           fluxTitre = 'Camino ==>  ' + str(mValueFilter)
           openLayerFilterDoubleClick(self, mySource,fluxTitre,fluxProvider, mRequest)
           
    return
#==================================================
#Fonction Open Layer Filter DoubleClick
#==================================================
def openLayerFilterDoubleClick(self, mySource,fluxTitre,fluxProvider, mRequest):
    #QApplication.instance().setOverrideCursor(self.cursorImage)
    QApplication.instance().setOverrideCursor(Qt.WaitCursor)                
    vlayer = QgsVectorLayer(mySource, fluxTitre, fluxProvider)
    if not vlayer.isValid():
       QApplication.instance().setOverrideCursor(Qt.ArrowCursor)                
       zMessErrorLoadLayerTitre = QtWidgets.QApplication.translate("bibli_camino", "Warning !!", None)                          
       zMessErrorLoadLayerTraduction1 = QtWidgets.QApplication.translate("bibli_camino", "Layer loading :", None)
       zMessErrorLoadLayerTraduction2 = QtWidgets.QApplication.translate("bibli_camino", "Please check your connections.", None)       
       zMessErrorLoadLayer = zMessErrorLoadLayerTraduction1 + " "  + str(fluxTitre) + "\n" + str(mySource) + "\n\n" + zMessErrorLoadLayerTraduction2
       QMessageBox.warning(None, zMessErrorLoadLayerTitre, zMessErrorLoadLayer)
    else :   
       self.resulFilter.setText(QtWidgets.QApplication.translate("bibli_camino", "", None))
       QgsProject.instance().addMapLayer(vlayer)
       vlayer.setSubsetString(mRequest)
       mCanvas = iface.mapCanvas()
       mCanvas.setExtent(vlayer.extent())
       QApplication.instance().setOverrideCursor(Qt.ArrowCursor)                
    return

#==================================================
#Fonction Open Layer Filter SimpleClick
#==================================================
def openLayerFilterSimpleClick(self, mySource,fluxTitre,fluxProvider, mRequest):
    QApplication.instance().setOverrideCursor(Qt.WaitCursor)                
    vlayer = QgsVectorLayer(mySource, fluxTitre, fluxProvider)
    if not vlayer.isValid():
       QApplication.instance().setOverrideCursor(Qt.ArrowCursor)                
       zMessErrorLoadLayerTitre = QtWidgets.QApplication.translate("bibli_camino", "Warning !!", None)                          
       zMessErrorLoadLayerTraduction1 = QtWidgets.QApplication.translate("bibli_camino", "Layer loading :", None)
       zMessErrorLoadLayerTraduction2 = QtWidgets.QApplication.translate("bibli_camino", "Please check your connections.", None)       
       zMessErrorLoadLayer = zMessErrorLoadLayerTraduction1 + " "  + str(fluxTitre) + "\n" + str(mySource) + "\n\n" + zMessErrorLoadLayerTraduction2
       QMessageBox.warning(None, zMessErrorLoadLayerTitre, zMessErrorLoadLayer)
    else :   
       self.resulFilter.setText(QtWidgets.QApplication.translate("bibli_camino", "", None))
       QgsProject.instance().addMapLayer(vlayer)
       print("je passe")
       vlayer.setSubsetString(mRequest)
       mCanvas = iface.mapCanvas()
       mCanvas.setExtent(vlayer.extent())
       QApplication.instance().setOverrideCursor(Qt.ArrowCursor)                
    return
                
#==================================================
#Lecture du fichier paramètre
#==================================================
def loadFichierParam(monFichierParam):
    fluxAdresse, fluxTitre, fluxProvider = 'https://api.camino.beta.gouv.fr/titres?format=geojson', 'Cadastre miniers api', 'ogr'
    carDebut, carFin = '[', ']'
    listWithValue = [fluxAdresse, fluxTitre, fluxProvider]
    if not FileExiste(monFichierParam) :
       createParam(monFichierParam, listWithValue, carDebut, carFin)

    return loadParam(monFichierParam, carDebut, carFin)
    
#==================================================
def loadParam(monFichierParam, carDebut, carFin):
    #Génération de la liste
    sVar_bonne_ligne = "paramSelect"
    sChaineDebut, sChaineFin, dicoValue, nbKey = carDebut, carFin, {}, 0
    zFileParam = open(monFichierParam, "r",encoding="utf-8")

    for zFileParamLigne in zFileParam :
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

           dicoValue[nbKey] = listWithValue
           nbKey += 1 

    zFileParam.close()
    return dicoValue

#==================================================
#Creation du fichier paramètre
#==================================================
def createParam(monFichierParam,listWithValue, carDebut, carFin) :

    if not FileExiste(monFichierParam) :
       zFileParam = open(monFichierParam, "w",encoding="utf-8")
       zContenu = u"# (c) Didier  LECLERC 2020 CMSIG MTES-MCTRCT/SG/SNUM/UNI/DRC Site de Rouen\n"
       zContenu += u"# créé le " + time.strftime("%d ") + zMyFrenchMonth(float(time.strftime("%m"))) + time.strftime(" %Y - %Hh%Mm%Ss") + "\n"
       zContenu += "\n"
       zContenu += u"paramSelect = " + carDebut

       for ll in listWithValue:
           zContenu += "'" + str(ll) + "',"
       zContenu = zContenu[:len(zContenu)-1] + carFin + "\n"
       zFileParam.write(zContenu)
       zFileParam.close()
    return    
        
#==================================================
#Fichier existe
#==================================================
def FileExiste(FileName):
    try:
       with open(FileName): pass
       ExisteFile = True
    except IOError:
       ExisteFile = False
    return ExisteFile

#==================================================
#Fichier existe
#==================================================
def createFolder(mFolder):
    try:
       os.makedirs(mFolder)
    except OSError:
       pass
    return mFolder
              
#==================================================
def zMyFrenchMonth(zNumberMonth):
    aMyFrenchMonth = {1:"Janvier", 2:"Février", 3:"Mars",4:"Avril",5:"Mai",6:"Juin",7:"Juillet",8:"Août",9:"Septembre",10:"Octobre",11:"Novembre",12:"Décembre"}
    return aMyFrenchMonth[zNumberMonth]
    
#==================================================
def getThemeIcon(theName):
    myPath = CorrigePath(os.path.dirname(__file__));
    myDefPathIcons = myPath + "/icons/"
    myDefPath = myPath.replace("\\","/")+ theName;
    myDefPathIcons = myDefPathIcons.replace("\\","/")+ theName;
    myCurThemePath = QgsApplication.activeThemePath() + "/plugins/" + theName;
    myDefThemePath = QgsApplication.defaultThemePath() + "/plugins/" + theName;
    myQrcPath = "python/plugins/ive/" + theName;
    if QFile.exists(myDefPath): return myDefPath
    elif QFile.exists(myDefPathIcons): return myDefPathIcons
    elif QFile.exists(myCurThemePath): return myCurThemePath
    elif QFile.exists(myDefThemePath): return myDefThemePath
    elif QFile.exists(myQrcPath): return myQrcPath
    else: return theName

#==================================================
def CorrigePath(nPath):
    nPath = str(nPath)
    a = len(nPath)
    subC = "/"
    b = nPath.rfind(subC, 0, a)
    if a != b : return (nPath + "/")
    else: return nPath

def transformeBorneXml(zText) :
    zText = zText.replace("@@",">") 
    zText = zText.replace("@","<")
    return zText
    
#==================================================
#==================================================
def debugMess(type,zTitre,zMess, level=Qgis.Critical):
    #type 1 = MessageBar
    #type 2 = QMessageBox
    if type == 1 :
       qgis.utils.iface.messageBar().pushMessage(zTitre, zMess, level=level)
    else :
       QMessageBox.information(None,zTitre,zMess)
    return  

#==================================================
# FIN
#==================================================
