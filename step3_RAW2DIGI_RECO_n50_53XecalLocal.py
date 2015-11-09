# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --data --conditions auto:run1_data -s RAW2DIGI,RECO --scenario HeavyIons --datatier GEN-SIM-RECO --eventcontent RECODEBUG -n 10 --repacked --filein file:/mnt/hadoop/cms/store/user/richard/HIHighPt/HIHighPt-HIRun2011-RAW-photon20and30_v2/56d3f34efbd38c742eee00f066b12bcb/HIHighPt-HIRun2011-RAW-photon20_100_1_6Oj.root --fileout file:step3_RAW2DIGI_RECO_75X.root --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50) #10
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/mnt/hadoop/cms/store/user/richard/HIHighPt/HIHighPt-HIRun2011-RAW-photon20and30_v2/56d3f34efbd38c742eee00f066b12bcb/HIHighPt-HIRun2011-RAW-photon20_100_1_6Oj.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:50'), #10
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECODEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:step3_RAW2DIGI_RECO_75X_n50_53XecalLocal.root'),
    outputCommands = process.RECODEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstructionHeavyIons)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECODEBUGoutput_step = cms.EndPath(process.RECODEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECODEBUGoutput_step)

from Configuration.Applications.ConfigBuilder import MassReplaceInputTag
MassReplaceInputTag(process)


