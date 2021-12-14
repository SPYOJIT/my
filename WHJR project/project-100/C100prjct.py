class ATM(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo
 
    def CashWithdrawn(self,object):
        print("Cash Withdrawn",object)

    def BalanceEnquiry(self,object):
        print("Balance is ",object)

yojit=ATM("11008899","5234")
print(yojit.cardNo)
print(yojit.pinNo)
yojit.CashWithdrawn(500)
yojit.BalanceEnquiry(500)
