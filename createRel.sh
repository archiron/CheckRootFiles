#!/bin/bash

now=$(date +"%Y_%m_%d")
echo $now
echo $CMSSW_VERSION
RELEASE='CMSSW_8_1_0_pre1'
echo $RELEASE

if $CMSSW_VERSION
then
    echo "no CMSSW VERSION"
    /cvmfs/cms.cern.ch/common/scramv1 project CMSSW $RELEASE
    cd $RELEASE/src
    eval `/cvmfs/cms.cern.ch/common/scramv1 runtime -sh`
    echo "CMSSW VERSION : $CMSSW_VERSION"
    python ~/lbin/Projet_CheckRootFiles/main.py
    cd ../..
    pwd
    rm -Rf $RELEASE
else
    echo "CMSSW VERSION : $CMSSW_VERSION"
    python ~/lbin/Projet_CheckRootFiles/main.py
fi
