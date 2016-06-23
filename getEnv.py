#! /usr/bin/env python
#-*-coding: utf-8 -*-

import os,sys
import urllib2

class env:
    def __init__(self): 
        # os.getenv is equivalent, and can also give a default value instead of `None`
        print os.getenv('CMSSW_BASE', "RIEN")
#        self.CMSSWBASE = os.environ['CMSSW_BASE'] # donne le repertoire de travail
#        self.CMSSWBASECMSSWRELEASEBASE = os.environ['CMSSW_RELEASE_BASE'] # donne la release et l'architecture
#        self.CMSSWBASECMSSWVERSION = os.environ['CMSSW_VERSION'] # donne la release (CMSSW_7_1_0 par exemple)
        self.CMSSWBASE = os.getenv('CMSSW_BASE', "CMSSW_BASE")
        self.CMSSWBASECMSSWRELEASEBASE = os.getenv('CMSSW_RELEASE_BASE', "CMSSW_RELEASE_BASE")
        self.CMSSWBASECMSSWVERSION = os.getenv('CMSSW_VERSION', "CMSSW_VERSION")

    def getCMSSWBASE(self):
#        CMSSWBASE = os.environ['CMSSW_BASE']
        CMSSWBASE = os.getenv('CMSSW_BASE', "CMSSW_BASE")
        return CMSSWBASE
		
    def getCMSSWBASECMSSWRELEASEBASE(self):
        return self.CMSSWBASECMSSWRELEASEBASE
		
    def getCMSSWBASECMSSWVERSION(self):
        return self.CMSSWBASECMSSWVERSION
		
    def cmsAll(self):
        cmsAll="<strong>CMSSW_BASE</strong> : " + self.getCMSSWBASE()
        cmsAll+="<br /><strong>CMSSW_RELEASE_BASE</strong> : " + self.getCMSSWBASECMSSWRELEASEBASE()
        cmsAll+="<br /><strong>CMSSW_VERSION</strong> : " + self.getCMSSWBASECMSSWVERSION()
        return cmsAll

    def eosText(self):
        eosText="/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"
        eosText+=' ls /eos/cms/store/relval/' 
        return eosText

    def eosFind(self):
        eosFind="http://cms-project-relval.web.cern.ch/cms-project-relval/relval_stats/"
        return eosFind

    def liste_datasets(self):
        liste_datasets = ['RelValSingleElectronPt10_UP15', 'RelValSingleElectronPt1000_UP15', 'RelValSingleElectronPt35_UP15', 'RelValQCD_Pt_80_120_13', 'RelValTTbar_13', 'RelValZEE_13']
        return liste_datasets

    def liste_datasets_miniAOD(self):
        return self.liste_datasets()

    def liste_datasets_fast(self):
        liste_fast = ['RelValTTbar_13', 'RelValZEE_13']
        return liste_fast

    def liste_datasets_pu(self):
        return self.liste_fast()

    def liste_type(self):
        liste_type = ['GEN-SIM-RECO', 'MINIAODSIM', 'GEN-SIM-DIGI-RECO']
        return liste_type

    def liste_tab(self):
        list_tab = ['liste_datasets', 'liste_datasets_miniAOD', 'liste_datasets_fast']
        return list_tab
        
    def dictionnaire(self):
        dictionnaire = {}
        dictionnaire["liste_datasets"] = ['RelValSingleElectronPt10_UP15', 'RelValSingleElectronPt1000_UP15', 'RelValSingleElectronPt35_UP15', 'RelValQCD_Pt_80_120_13', 'RelValTTbar_13', 'RelValZEE_13']
        dictionnaire["liste_datasets_miniAOD"] = ['RelValSingleElectronPt10_UP15', 'RelValSingleElectronPt1000_UP15', 'RelValSingleElectronPt35_UP15', 'RelValQCD_Pt_80_120_13', 'RelValTTbar_13', 'RelValZEE_13']
        dictionnaire["liste_datasets_fast"] = ['RelValTTbar_13', 'RelValZEE_13']
        return dictionnaire
        