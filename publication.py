#Publication

class Publication:
    def __init__(self, title="", pricePerIssue=0):
        self._title = title
        self._pricePerIssue = pricePerIssue

    def setTitle(self, title):
        self._title = title

    def setPricePerIssue(self, pricePerIssue):
            self._pricePerIssue = pricePerIssue

    def getTitle(self):
        return self._title

    def getPricePerIssue(self):
        return self._pricePerIssue

    def __str__(self):
        return (self._title + "  $" + str(self._pricePerIssue))
        
class Magazine(Publication):
    def __init__(self, title="", pricePerIssue=0, numIssues=0):
        super().__init__(title, pricePerIssue)
        self._numIssues = numIssues
    def calcSubscription(self):
        return self._pricePerIssue * self._numIssues
    
class Newspaper(Publication):
    def __init__(self, title="", pricePerIssue=0, daily=True):
        super().__init__(title, pricePerIssue)
        self._daily = daily
    def calcSubscription(self):
        if self._daily:
            return self._pricePerIssue * 365
        else:
            return self._pricePerIssue * 52
    
    
    

