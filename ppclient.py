#PAST PAPER TRACKER - CLIENT
#PPCLIENT

import ppclasses, pickle, webbrowser, math

f = open("ppdata.meme", "rb")
modules = pickle.load(f)
#### dumped in as [C3, C4, S2, M2, FP2] ###
f.close()

"""
C3 = modules[0]
C4 = modules[1]
S2 = modules[2]
M2 = modules[3]
FP2= modules[4]
"""

#FUNCTION TO FIND PAPER
def findPaper(module, paperName):
    """paperName in form jun07/jan11"""
    season = paperName[:3]
    year = paperName[3:]

    targetPaper = None

    for paper in module.papers:
        if paper.season==season and paper.year==year:
            targetPaper = paper
            break

    return targetPaper

def openPaper(moduleName, paperName):
    """paperName in form jun07/jan11"""

    season = paperName[:3]
    year = paperName[3:]
    fullSeasons = {"jan": "January", "jun": "June"}

    #standard URL = http://pmt.physicsandmathstutor.com/download/Maths/A-level/C4/Papers-OCR/January%202008%20MS%20-%20C4%20OCR.pdf
    #QUESTION PAPER - QP
    webbrowser.open(r"http://pmt.physicsandmathstutor.com/download/Maths/A-level/"+moduleName+"/Papers-OCR/"+fullSeasons[season]+"%2020"+year+"%20QP%20-%20"+moduleName+"%20OCR.pdf")
    #MARK SCHEME - MS
    webbrowser.open(r"http://pmt.physicsandmathstutor.com/download/Maths/A-level/"+moduleName+"/Papers-OCR/"+fullSeasons[season]+"%2020"+year+"%20MS%20-%20"+moduleName+"%20OCR.pdf")

    #90 MIN TIMER
    webbrowser.open(r"https://www.google.co.uk/search?q=timer+90+minutes&oq=TIMER&aqs=chrome.1.69i57j69i59j0l4.1560j0j7&sourceid=chrome&ie=UTF-8")

def fill(string, n, filler=" "):
    if len(string) >= n:
        return string
    else:
        return string+(n-len(string))*filler

#GLOBAL VARIABLES - used in MATRIX
allPapers  = ['        ', 'spc04   ', 'jun05   ', 'jan06   ', 'jun06   ', 'jan07   ', 'jun07   ', 'jan08   ', 'jun08   ', 'jan09   ', 'jun09   ', 'jan10   ', 'jun10   ', 'jan11   ', 'jun11   ', 'jan12   ', 'jun12   ', 'jan13   ', 'jun13   ', 'jun14   ', 'jun15   ', 'jun16   ']
allModules = ["        ", "   C3   ", "   C4   ", "   S2   ", "   M2   ", "   FP2  "]

f = open("greeting.txt", "r")
greeting = f.readlines()
f.close()

for line in greeting:
    print(line[:79])
print()

mainMenuOption = ""
while mainMenuOption.upper() != "X":
    print("""               8888888888 Y88b   d88P     888     888 8888888b.
               888         Y88b d88P      888     888 888   Y88b
               888          Y88o88P       888     888 888    888
               8888888       Y888P        888     888 888   d88P
               888            888         888     888 8888888P"
               888            888         888     888 888
               888            888         Y88b. .d88P 888
               8888888888     888          "Y88888P"  888

WHAT YA WANNA DO?

    0. View full PAST PAPER MATRIX
    1. View a SPECIFIC SUBJECT PAPER LIST
    2. Add a SPECIFIC RESULT
    3. Add all results for ONE MODULE
    4. View STATS

    X. EXIT
""")
    mainMenuOption = ""
    while mainMenuOption.upper() not in ("0","1","2","3","4","X"):
        mainMenuOption = input("> ")

    if mainMenuOption == "0":
        #MATRIX MADE OF 6x22 GRID WITH 8x1 UNITS (x,y)
        #i.e. each x unit is 8 characters long and each y unit is 1 line

        #f = open("G:/My Drive/Maths Past Papers.txt","w")

        print("SCORE DISPLAY TYPE: m/p (press enter for default=p)")
        score = input("> ").lower()
        if score == "":
            score = "p"

            totalPapersCompleted = 0

        for y in range(22):    # Y = PAPERS
            for x in range(6): # X = MODULES

                if y==2 and x==5:  #get around issue of fp2 having no jun05
                    if score == "p":
                        print("   xxx  ", end="")
                        #f.write("   xxx  ")
                    else:
                        print("   xx   ", end="")

                elif y== 0:
                    print(allModules[x], end="")
                    #f.write(allModules[x])
                elif x==0:
                    print(allPapers[y], end="")
                    #f.write(allPapers[y])

                else:
                    results = findPaper(modules[x-1],allPapers[y][:5]).results

                    if score == "p":
                        if results == []:
                            print("   ---  ", end="")
                            #f.write("   ---  ")
                        else:
                            result = str(int(round((max(results)*100)/72, 0))).zfill(3)
                            print("   %s  " % (result), end="")
                            #f.write("   %s  " % (result))
                            totalPapersCompleted += 1
                    else:
                        if results == []:
                            print("   --   ", end="")
                        else:
                            print("   %s   " % (str(max(results))).zfill(2), end="")
                            totalPapersCompleted += 1
            print()
            #f.write("\n")

        print("          ",end="")
        #f.write("          ")

        for i, module in enumerate(modules):
            papersCompleted = 0
            for paper in module.papers:
                if len(paper.results)!=0:
                    papersCompleted += 1
            if i != 4:
                print("%s/21   " % (str(papersCompleted).zfill(2)), end="")
            else:
                print("%s/20   " % (str(papersCompleted).zfill(2)), end="")
            #f.write("%s/21   " % (str(papersCompleted).zfill(2)))

        print(" Papers completed: ", totalPapersCompleted, "/104")
        #f.write("\n\nPapers completed: %s/104\n" % (totalPapersCompleted))

        '''
        footnote = open("footnote.txt","r")
        footnoteText = footnote.readlines()
        footnote.close()

        for line in footnoteText:
            f.write(line)

        f.close()
        '''

        rawInput = None
        while rawInput != "":
            print("OPEN PAPER IN BROWSER (eg 's2 jun07'/'fp2 jan11') (LEAVE BLANK TO GO BACK)")
            rawInput = input()
            if rawInput != "":
                moduleName, paperName = rawInput.split()
                openPaper(moduleName.upper(), paperName)

    elif mainMenuOption in ("1", "2", "3"):

        #SELECT MODULE (NEEDED FOR 1, 2 & 3)
        moduleOption = None
        while moduleOption != "":
            print("MODULE  0-C3  1-C4  2-S2  3-M2  4-FP2  (LEAVE BLANK TO GO BACK)")
            moduleOption = None
            while moduleOption not in  ("0","1","2","3","4",""):
                moduleOption = input("> ")

            if moduleOption != "":

                module = modules[int(moduleOption)]

                if mainMenuOption == "1":
                    print("""Type in any display options (separate by space):
                        c/s - Chronological/Sorted order
                        m/p - raw Marks/Percentage
                        (press enter for c m)""")
                    rawInput = input("> ").lower()
                    if rawInput == "":
                        rawInput = "c m"
                    order, score = rawInput.split()
                    module.displayResults(order, score)
                    print()

                    paperEntry = None
                    while paperEntry != "":
                        paper = None
                        print("OPEN PAPER IN BROWSER (eg jun07/jan11) (LEAVE BLANK TO GO BACK)")
                        while paper == None and paperEntry!="":
                            paperEntry = input("> ").lower()
                            paper = findPaper(module, paperEntry)

                        if paperEntry != "" and paper != None:
                            openPaper(module.name, paperEntry)
                    print()

                elif mainMenuOption == "2":
                    paperEntry = None
                    while paperEntry != "":
                        paper = None
                        print("PAPER (eg jun07/jan11)  (LEAVE BLANK TO GO BACK)")
                        while paper == None and paperEntry!="":
                            paperEntry = input("> ").lower()
                            paper = findPaper(module, paperEntry)

                        if paperEntry != "" and paper != None:
                            print("RAW MARK (/72)")
                            newMark = None
                            while newMark not in range(0,73):
                                newMark = int(input("> "))

                            paper.updateResults(newMark)

                            #update the .meme file
                            with open("ppdata.meme", "wb") as f:
                                pickle.dump(modules, f)

                            print("RESULT ADDED.\n")

                else:
                    print("RAW MARK (/72) (LEAVE BLANK TO SKIP PAPER) (TYPE end TO BREAK LOOP)")
                    for paperName in [x[:5] for x in allPapers[1:]]:
                        newMark = input("%s> " % (paperName))
                        if newMark.upper() == "END":
                            break
                        elif newMark != "":
                            paper = findPaper(module, paperName)
                            paper.updateResults(int(newMark))
                            with open("ppdata.meme", "wb") as f:
                                pickle.dump(modules, f)

    elif mainMenuOption == "4":
        #Show: Average score, no completed (total) both for individual modules and overall
        completedPerModule = [0,0,0,0,0]
        meanPerModule = [0,0,0,0,0]
        seventyTwoPerModule = [0,0,0,0,0]

        squareSumPerModule = [0,0,0,0,0]
        variancePerModule = [0,0,0,0,0]
        unbiasedVariancePerModule = [0,0,0,0,0]

        totalCompleted = 0
        totalScore = 0

        for i, module in enumerate(modules):
            scoreSum = 0
            for paper in module.papers:
                if len(paper.results) != 0:
                    for result in paper.results:
                        if result>7:
                            completedPerModule[i] += 1
                            scoreSum += result
                            squareSumPerModule[i] += result**2

                            meanPerModule[i] = (scoreSum*(100/72))/completedPerModule[i]

                        if result == 72:
                            seventyTwoPerModule[i] += 1

            totalScore += scoreSum

            variancePerModule[i] = (squareSumPerModule[i]/completedPerModule[i])-((meanPerModule[i]*(72/100))**2)
            unbiasedVariancePerModule[i] = variancePerModule[i]*(completedPerModule[i]/(completedPerModule[i]-1))

        totalCompleted = sum(completedPerModule)
        totalMeanPercentage = (totalScore*(100/72))/totalCompleted

        totalVariance = (sum(squareSumPerModule)/totalCompleted)-((totalScore/totalCompleted)**2)
        totalUnbiasedVariance = totalVariance*(totalCompleted/(totalCompleted-1))

        print("---- TOTAL ----")
        print("Papers Completed: ", totalCompleted)
        print("Mean Percentage = ", "%.1f" % (totalMeanPercentage))
        print("Number of 72s: ", sum(seventyTwoPerModule))
        print("\nMean Score = ", "%.3f" % (totalScore/totalCompleted))
        print("Standard Deviation = %s (biased)    %s (unbiased)" % ("%.3f" % (math.sqrt(totalVariance)), "%.3f" % (math.sqrt(totalUnbiasedVariance))))

        print("\n---- PER MODULE ---")
        for i, module in enumerate(modules):
            print("%s -- Papers Completed: %s   MeanPercentage: %s   No 72: %s" % (fill(module.name, 3), completedPerModule[i], "%.1f" % (meanPerModule[i]), seventyTwoPerModule[i]))
            print("    -- Standard Deviation(biased): %s  Standard Deviation(unbiased): %s\n" % ("%.3f" % (math.sqrt(variancePerModule[i])), "%.3f" % (math.sqrt(unbiasedVariancePerModule[i]))))
        input()



    if mainMenuOption.upper() == "X":
        input(""" .d8888b.         d8888 88888888888  .d8888b.  888    888
d88P  Y88b       d88888     888     d88P  Y88b 888    888
888    888      d88P888     888     888    888 888    888
888            d88P 888     888     888        8888888888
888           d88P  888     888     888        888    888
888    888   d88P   888     888     888    888 888    888
Y88b  d88P  d8888888888     888     Y88b  d88P 888    888
 "Y8888P"  d88P     888     888      "Y8888P"  888    888



Y88b   d88P  .d88888b.  888     888      .d88888b.  888b    888
 Y88b d88P  d88P" "Y88b 888     888     d88P" "Y88b 8888b   888
  Y88o88P   888     888 888     888     888     888 88888b  888
   Y888P    888     888 888     888     888     888 888Y88b 888
    888     888     888 888     888     888     888 888 Y88b888
    888     888     888 888     888     888     888 888  Y88888
    888     Y88b. .d88P Y88b. .d88P     Y88b. .d88P 888   Y8888
    888      "Y88888P"   "Y88888P"       "Y88888P"  888    Y888


88888888888 888    888 8888888888
    888     888    888 888
    888     888    888 888
    888     8888888888 8888888
    888     888    888 888
    888     888    888 888
    888     888    888 888
    888     888    888 8888888888



8888888888 888      8888888 8888888b.  8888888b. 8888888 8888888b. Y88b   d88P
888        888        888   888   Y88b 888   Y88b  888   888  "Y88b Y88b d88P
888        888        888   888    888 888    888  888   888    888  Y88o88P
8888888    888        888   888   d88P 888   d88P  888   888    888   Y888P
888        888        888   8888888P"  8888888P"   888   888    888    888
888        888        888   888        888         888   888    888    888
888        888        888   888        888         888   888  .d88P    888
888        88888888 8888888 888        888       8888888 8888888P"     888



8888888888 888      8888888 8888888b.
888        888        888   888   Y88b
888        888        888   888    888
8888888    888        888   888   d88P
888        888        888   8888888P"
888        888        888   888
888        888        888   888
888        88888888 8888888 888   """)

#"What"
#"love that"
#- Georgia Cope 2K17
