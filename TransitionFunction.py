class TransitionFunction(object):

    alphabet = []

    def __init__(self):
        self.transition = {}

    def getTransitionFunction(self):
        licznik = 0
        numberOfOperates = input()
        while licznik < numberOfOperates:
            before = []
            than = []
            licznik2 = 0
            licznik3 = 0
            while licznik2 < 2:
                statesBefore = raw_input()
                before.append(statesBefore)
                licznik2 = licznik2 +1
            while licznik3 < 3:
                statesThan = raw_input()
                than.append(statesThan)
                licznik3 = licznik3 +1
            self.makeTransition(before, than)
            licznik  +=1



    def makeTransition(self, before, than):
        beforeTuple = tuple(before)
        thanTuple = tuple(than)
        self.transition.update({beforeTuple: thanTuple})


    def printTransitionFunction(self):
        print(self.transition)

    def qtTransition(self, stateBefore, charBefore, stateAfter, charAfter, moveTo):
        stateBefore = self.unicodeToString(stateBefore)
        charBefore = self.unicodeToString(charBefore)
        stateAfter = self.unicodeToString(stateAfter)
        charAfter = self.unicodeToString(charAfter)
        if self.checkIfGoodWithAlphabet(charAfter) and self.checkIfGoodWithAlphabet(charBefore):
            beforeTuple = tuple([stateBefore, charBefore])
            afterTuple = tuple([stateAfter, charAfter, moveTo])
            return self.transition.update({beforeTuple: afterTuple})
        else:
            raise BaseException

    def unicodeToString(self, uniString):
        return uniString.encode('ascii', 'ignore')


    def checkIfGoodWithAlphabet(self, char):
        if char in self.alphabet:
            return True
        else:
            return False