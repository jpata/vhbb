import FWCore.ParameterSet.Config as cms

hltMonBTagIPClient = cms.EDFilter('HLTMonBTagClient',
    monitorName             = cms.string('HLT/HLTMonBJet'),
    pathName                = cms.string('HLT_BTagIP_Jet50U'),
    storeROOT               = cms.untracked.bool(False),
    updateLuminosityBlock   = cms.untracked.bool(True),
    updateRun               = cms.untracked.bool(False),
    updateJob               = cms.untracked.bool(False),
    outputFile              = cms.untracked.string('HLTMonBTag.root')
)
