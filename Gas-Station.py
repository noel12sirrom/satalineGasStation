import random
class ChargeCustomer:
    def  __init__(self, id, name, numOfRep, pref, plateNum=[]):
        self.id = id
        self.name = name
        self.numOfRep = numOfRep
        self.pref = pref
        self.plateNum = plateNum
    
    def display(self):
        print(f"ID: {self.id}\nName: {self.name}\nNumber of Representatives: {self.numOfRep}\nPreference: {self.pref}\nLicense Plate Numbers: {self.plateNum}")
#test variables 
testChargeCust = ChargeCustomer(1,"gas Pro", 2, None, ["brd232", "ej232"])
chargeCustomersList = [testChargeCust]
todaysDate = "01/01/2000"
itemsPurchased = ['5W-30']       

inventory = {'87':{"maxCapacity":75708.23,
                    "price":184.90},
        
            '90':{"maxCapacity":113562.35,
                      "price":193.60},

            "D":{"maxCapacity":94635.29,
                 "price":182.30},
            "diesel":{"maxCapacity":94635.29,
                      "price":182.30},
            
            "5W-30":{"maxCapacity":None,
                     "price":2900.00},
            
            "5W-40":{"maxCapacity":None,
                     "price":3500.00},

            "15W-40":{"maxCapacity":None,
                      "price":3600.00},
            
            "SAE-40":{"maxCapacity":None,
                      "price":2100.00}
            }


def serveCustomer(typeOfCustomer):
    currentCustomer = None
    change = 0
    amount = 0    
    total = 0
    tax = 0
    fuelAmt = 0
    itemsPurchased = {}
    paymentType =""
        
    def validate():
        givenId = int(input("\nEnter ID: "))
        for customer in chargeCustomersList:
            if customer.id == givenId:
                nonlocal currentCustomer
                currentCustomer  = customer
                break
        else:
            print("Charge Account Not found.")
            return False
            
        print(customer.name) 
    
        #print out license plate under the under the ID
        print("See List below for plates eligible for fuel")
        for index, plate in enumerate(currentCustomer.plateNum, start=1):
            print(f"{index}. {plate}")
        while True:
            opt = input("Eligible Plates (Y/N): ").upper()
            if opt == 'Y' :
                return True
            elif opt  == 'N':
                return False
            print("Invalid Entry. Please Enter Y or N.")  
        
    def takeOrder():
        nonlocal total, fuelAmt, tax
        fuelType =(input("\nFuel Type: ").upper())
        fuelAmt = int(input("Enter fuel amount (litres): "))
        itemsPurchased[fuelType] = fuelAmt #adds it itemsPurchased Dictionary
        
        needLubricant = random.choice(["Y", "N"])
        if needLubricant == "Y":
            lubeType = random.choice(['5W-30', '5W-40', '15W-40', 'SAE-40'])
            lubeAmt = int(input("Enter lubricant amount: "))
            #adds lubricant type and amount ot list
            itemsPurchased[lubeType] = lubeAmt
            
        for item in itemsPurchased: #item refers to the dictionary key
            if not inventory[item]["maxCapacity"]:
                total += inventory[item]["price"]*lubeAmt
            else:
                total += inventory[item]["price"]*fuelAmt
            
        try:
            tax = inventory[lubeType]["price"] * lubeAmt * 0.16
        except Exception:
            tax = 0
            
        total += tax    
    
    def CODpayment():
        nonlocal paymentType, change, amount
        while True:
            opt = input("Payment type [(1)Cash/(2)Card]: ")
            if opt == "1":
                paymentType = "Cash tendered" 
                if fuelAmt < 2:
                    while True:
                        opt = input("The minimum purchase is two litres for cash payments. By more gas? (Y/N): ").upper()
                        if opt == "Y":
                            takeOrder()
                            CODpayment()
                        elif opt ==  "N":
                            break
                        
                amount = float(input("Enter Cash tendered: "))
                break
            elif  opt == "2":
                paymentType = "Card"
                amount = total
                #validate if card amount greater than $1000
                if amount < 1000:
                    while True:
                        opt = input("The minimum amount is $1000 for card transactions.. Would u like to retake order and add more items? (Y/N): ").upper()
                        if opt == "Y":
                            takeOrder()
                            CODpayment()
                        elif opt ==  "N":
                            break
                break
            
            print( "Please enter a valid option")
        
        if amount < total:
            difference = total - amount
            amount = float(input(f"Needs ${difference:.2f} more!\n Enter Cash tendered again: "))
                    
        change = amount - total
        
    def printReceipt():
        print(f"\n\n{todaysDate}\nType of Customer: {typeOfCustomer}\n----")
        print(*(f"{key}: {value}\n" for key, value in itemsPurchased.items()))
        print(f"----\nGCT = ${tax}\ntotal = ${total}\n{paymentType} = ${amount}\nChange = ${change:.2f}\n\n")
    
    
    if typeOfCustomer == "charge":
        if validate():
            takeOrder()
            printReceipt() 
    elif typeOfCustomer == "COD":
        takeOrder() 
        CODpayment() 
        printReceipt()      

def addChargeCustomer():
    customer = ChargeCustomer()
    
    if not chargeCustomersList:
        customer.id = 0
    else:
        customer.id = chargeCustomersList[-1].id +1
        
    
    customer.name = input("Enter Customer name: ")
    customer.numOfRep = input("Enter the number of representatives: ")
    
    for i in range(int(customer.numOfRep)):
        customer.plateNum.apppend(input(f"Enter the license pla number for Represetative {i}: "))
    

    opt = random.randint(0,1)

while True:   
    opt = input("\nServe Customer: 1\nAdd Charge Customer: 2\nUpdate Charge Customer: 3\nDelete Charge Customer: 4\nMake payment to charge account: 5\nRefuel tank: 6\nGenerate report: 7\nEXIT PROGRAM: 8\n  Selection: ")
    if opt == '1':
        opt = input("Customer Type [(1) COD,(2)Charge ]: ")
        if opt == '1':
            serveCustomer("COD")
        elif opt == '2':
            serveCustomer("charge")
                 
    elif opt == '8':
        break
 

    
    

