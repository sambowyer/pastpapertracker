#PAST PAPER TRACKER - CLASSES
#PPCLASSES

class Paper():
    def __init__(self,season, year):
        self.season = season
        self.year = year
        self.results = []

    def updateResults(self, newMark):
        self.results.append(newMark)


class Module():
    def __init__(self, name, papers):
        self.name = name
        self.papers = papers

    def displayResults(self, order, score):
        #options
        #order: c-chronological s-sorted (max-->min)
        #score: m-marks         p-percentage

        print("\n%s results:" % (self.name))
        for paper in self.papers:
            blank="--"

            results = paper.results
            if order != "c":
                #sort results from max to min
                results = sorted(results, reverse=True)
            if score != "m":
                #convert from raw marks to percentage
                results = [str(int(round((x*100)/72, 0))).zfill(3) for x in results]
                blank ="---" #results take 3 char not 2
            else:
                results = [str(x).zfill(2) for x in results]

            print(paper.season+paper.year+":", end=" ")
            if len(results) != 0:
                for result in results:
                    print(result, end=" ")
            else:
                print(blank, end=" ")
            print()

#"What"
#"love that"
#- Georgia Cope 2k18
