#! /usr/bin/env python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore

import os,sys,subprocess

from getEnv import env
from fonctions import cmd_fetch, list_search, explode_item
		
#############################################################################
class CheckWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('CheckRootFiles publish v0.0.2')

        self.cmsenv = env()
        self.texte = self.cmsenv.cmsAll()
        self.coll_list = []
        self.working_dir_base = os.getcwd()
						
		# creation of texEdit for the release to check
        self.QGBox1 = QGroupBox("release")
        self.QGBox1.setMaximumHeight(80)
        self.QGBox1.setMinimumHeight(80)
        self.QGBox1.setMaximumWidth(450)
        self.QGBox1.setMinimumWidth(450)
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setText(self.cmsenv.getCMSSWBASECMSSWVERSION()) # default
        self.lineedit1.setMinimumWidth(150)
        self.label1 = QLabel("release", self)
        self.label1.setMaximumWidth(80)
        self.label1.setMinimumWidth(80)
            # Création du bouton Check
        self.bouton1 = QPushButton(self.trUtf8("Check !"),self)
        self.bouton1.setFont(QFont("Comic Sans MS", 10,QFont.Bold,True))
        self.bouton1.setIcon(QIcon("../images/smile.png"))
        self.connect(self.bouton1, SIGNAL("clicked()"), self.Check_1) 

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.lineedit1)
        hbox1.addWidget(self.bouton1)
        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox1)
        vbox1.addStretch(1)
        self.QGBox1.setLayout(vbox1)

        #Layout intermédiaire 1 : création et peuplement de la release
        self.layoutH_release = QHBoxLayout()
        self.layoutH_release.addStretch(1)
        self.layoutH_release.addWidget(self.QGBox1)

		# creation of texEdit for the release to check
        self.QGBox2 = QGroupBox("Results")
        self.QGBox21 = QGroupBox("eos ls")
        self.QGBox22 = QGroupBox("https")
        self.QGBox21.setMaximumHeight(200)
        self.QGBox21.setMinimumHeight(200)
        self.QGBox21.setMaximumWidth(450)
        self.QGBox21.setMinimumWidth(450)
        self.QGBox22.setMaximumHeight(200)
        self.QGBox22.setMinimumHeight(200)
        self.QGBox22.setMaximumWidth(450)
        self.QGBox22.setMinimumWidth(450)
        # creation du TextEdit secondaire
        self.texte_eosls = QTextEdit()
        # creation du TextEdit liens
        self.texte_https = QTextEdit()
        self.hbox2 = QHBoxLayout()
        self.hbox21 = QHBoxLayout()
        self.hbox21.addWidget(self.texte_eosls)
        self.hbox22 = QHBoxLayout()
        self.hbox22.addWidget(self.texte_https)
        self.QGBox21.setLayout(self.hbox21)
        self.QGBox22.setLayout(self.hbox22)
        self.hbox2.addWidget(self.QGBox21)
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(self.QGBox22)
        self.QGBox2.setLayout(self.hbox2)

        #Layout intermédiaire 2 : textedit
        self.layoutH_View = QHBoxLayout()
        self.layoutH_View.addStretch(1)
        self.layoutH_View.addWidget(self.QGBox2)

        # Création du bouton quitter, ayant pour parent la "fenetre"
        self.boutonQ = QPushButton(self.trUtf8("Quitter ?"),self)
        self.boutonQ.setFont(QFont("Comic Sans MS", 14,QFont.Bold,True))
        self.boutonQ.setIcon(QIcon("../images/smile.png"))
        self.connect(self.boutonQ, SIGNAL("clicked()"), qApp, SLOT("quit()"))
        
        #Layout intermédiaire : boutons
        self.layoutH_boutons = QHBoxLayout()
        self.layoutH_boutons.addStretch(1)
        self.layoutH_boutons.addWidget(self.boutonQ)

		# creation du label resumé
        self.labelResume = QLabel(self.trUtf8(self.texte), self)
            # creation du grpe Folders paths
        self.QGBoxFinal = QGroupBox("Folders paths")
        vbox8 = QVBoxLayout()
        vbox8.addWidget(self.labelResume)
        self.QGBoxFinal.setLayout(vbox8)

        #Layout intermédiaire : ComboBox + labelcombo
        self.layoutV_combobox = QVBoxLayout()
        self.layoutV_combobox.addWidget(self.QGBoxFinal)
        
        # creation des onglets
        self.onglets = QTabWidget()
        self.generalTab = QWidget()
        self.generalTab.setMinimumHeight(170)
        self.onglets.insertTab(0, self.generalTab, "General")
            #Set Layout for Tabs Pages
        self.generalTab.setLayout(self.layoutV_combobox)   

        #Layout principal : création et peuplement
        self.layout_general = QVBoxLayout()
        self.layout_general.addLayout(self.layoutH_release)
        self.layout_general.addLayout(self.layoutH_View)
        self.layout_general.addWidget(self.onglets)
        self.layout_general.addLayout(self.layoutH_boutons)
        self.setLayout(self.layout_general)       

        print "fin"

    def Check_1(self):
        print "Check button clicked !"
        print "Computation for " + self.lineedit1.text()
#        QtCore.QCoreApplication.processEvents()

