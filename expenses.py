import os

class Expenses(object):
    def __init__(self):
        relativePath = os.path.dirname(__file__)
        self.path = os.path.join(relativePath,'.expenses')
        if not(os.path.isfile(self.path)):
            self.expenses=open(self.path,'w+')
            self.expenses.close()

    def calculateExpenses(self):
        self.expenses=open(self.path)
        final = 0.0
        for item in self.expenses:
            final = final + float(item)

        return final

    def editExpenses(self):
        os.system("vim " + self.path)
