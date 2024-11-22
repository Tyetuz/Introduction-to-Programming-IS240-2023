class Magazine:
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
    
    def calcSubscription(self):
        return self._pricePerIssue * 12

    def __str__(self):
        return (self._title + "  $" + str(self._pricePerIssue))
    
class Newspaper(Magazine):
    def calcSubscription(self):
        return self._pricePerIssue * 365