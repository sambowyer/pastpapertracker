#PAST PAPER TRACKER - GENERATOR
#PPGEN

import ppclasses, pickle

#C3 (21), C4 (21), S2 (21), M2 (21), FP2(20 - no jun05)
papers = ["spc04", "jun05"]
seasons = ["jan","jun"]

for i in range(6,14):
    papers.append("%s%s" % (seasons[i%2], str(i).zfill(2)))
    papers.append("%s%s" % (seasons[(i+1)%2], str(i).zfill(2)))
for i in range(14,17):
    papers.append("jun%s" % (i))

#Paper Creation
modulePapers = []
C3Papers = []
C4Papers = []
S2Papers = []
M2Papers = []
FP2Papers= []
modulePapers = [C3Papers, C4Papers, S2Papers, M2Papers] #add in fp2 later

for modulePaperList in modulePapers:
    for paper in papers:
        modulePaperList.append(ppclasses.Paper(paper[:3], paper[3:]))

papers.remove("jun05")#as fp2 doesnt have this paper
for paper in papers:
    FP2Papers.append(ppclasses.Paper(paper[:3], paper[3:]))

modulePapers.append(FP2Papers)

#Module Creation
C3 = ppclasses.Module("C3",modulePapers[0])
C4 = ppclasses.Module("C4",modulePapers[1])
S2 = ppclasses.Module("S2",modulePapers[2])
M2 = ppclasses.Module("M2",modulePapers[3])
FP2= ppclasses.Module("FP2",modulePapers[4])

modules = [C3, C4, S2, M2, FP2]
"""
for module in modules:
    module.displayResults()
"""

with open("ppdata.meme", "wb") as f:
    pickle.dump(modules, f)

#"What"
#"love that"
#- Georgia Cope 2k18
