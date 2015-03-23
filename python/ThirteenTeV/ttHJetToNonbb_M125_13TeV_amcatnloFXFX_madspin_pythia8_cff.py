import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *
generator = cms.EDFilter("Pythia8HadronizerFilter",
maxEventsToPrint = cms.untracked.int32(1),
pythiaPylistVerbosity = cms.untracked.int32(1),
filterEfficiency = cms.untracked.double(1.0),
pythiaHepMCVerbosity = cms.untracked.bool(False),
comEnergy = cms.double(13000.),
PythiaParameters = cms.PSet(
pythia8CommonSettingsBlock,
pythia8CUEP8M1SettingsBlock,
pythia8aMCatNLOSettingsBlock,
  processParameters = cms.vstring(
  'JetMatching:setMad = off',
  'JetMatching:scheme = 1',
  'JetMatching:merge = on',
  'JetMatching:jetAlgorithm = 2',
  'JetMatching:etaJetMax = 999.',
  'JetMatching:coneRadius = 1.',
  'JetMatching:slowJetPower = 1',
  'JetMatching:qCut = 40.', #this is the actual merging scale
  'JetMatching:doFxFx = on',
  'JetMatching:qCutME = 20.',#this must match the ptj cut in the lhe generation step
  'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
  'JetMatching:nJetMax = 1', #number of partons in born matrix element for highest multiplicity
  'SLHA:useDecayTable = off',  # Use pythia8s own decay mode instead of decays defined in LH accord
  '25:m0 = 125.0',
  '25:onMode = on', 	# Allow all higgs decays 
  '25:offIfAny = 5 5',    # Switch decays of b quarks off
  'Higgs:clipWings = off',  # Do not clip higgs width
  'HiggsSM:NLOWidths = on' # On by default, mentioned for documentation
  ),
parameterSets = cms.vstring('pythia8CommonSettings',
'pythia8CUEP8M1Settings',
'pythia8aMCatNLOSettings',
'processParameters',
)
)
)
