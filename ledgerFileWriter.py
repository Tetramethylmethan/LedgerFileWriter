from datetime import datetime


filepath = ""

def setFilePath(path):
    filepath = path

def writeToJournal(partyA="",partyB ="",description="",amount=""):
    with open(filepath, "a") as file:
        file.write()
        file.close()

def __getCurrDate__():
    return datetime.today().strftime('%Y/%m/%d')

#futureproofing  - basicly dead code
def createAmountString(amount=0, currency=""):
    if currency not in ['€']:
        return 0
    else:
        return str(amount)+currency

    

class Transaction:
    def __init__(self):
        self.data ={
            "date":"",
            "secDate":"",
            "Status":"",
            "code":"",
            "description":"",
            "note":"",
            "comment":"",
            "postingA":{
                "status":"",
                "name":"",
                "currency":"",
                "amount":"",
                "comment":"",
            },
            "postingB":{
                "status":"",
                "name":"",
                "currency":"",
                "amount":"",
                "comment":""
            }
        }
    def easyTransact(self,description="",accountNameA="",accountNameB="",amountA=0,currency="€",date = __getCurrDate__(),amountB=None):
        if amountB == None:
            amountB = -amountA
        amountA = str(amountA)
        amountB = str(amountB)
        self.data["date"] = date
        self.data["description"] =description
        self.data["postingA"]["name"] = accountNameA
        self.data["postingA"]["currency"] =currency
        self.data["postingA"]["amount"] = amountA
        self.data["postingB"]["name"] = accountNameB
        self.data["postingB"]["currency"] =currency
        self.data["postingB"]["amount"] =amountB
    
    def generateSmallString(self):
        stringA= self.data["date"] + " " +self.data["description"] + "\n"
        stringB="    "+self.data["postingA"]["name"] + "    "+ self.data["postingA"]["currency"]+self.data["postingA"]["amount"]+ "\n"
        stringC="    "+self.data["postingB"]["name"] + "    "+ self.data["postingB"]["currency"]+self.data["postingB"]["amount"]+ "\n \n"
        return stringA+stringB+stringC