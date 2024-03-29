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
        

chargeCustomersList = []

chargeCustomers = []

       

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

todaysDate = "01/01/2000"


def serveCustomer(typeOfCustomer):
    change = 0
    amount = 0    
    total = 0
    tax = 0
    itemsPurchased = {}
    paymentType =""
                 
    if typeOfCustomer == "COD":
        takeOrder()
        CODpayment() 
        printReceipt()          
        
    def takeOrder():
        fuelType =(input("Fuel Type: ").upper())
        fuelAmt = int(input("Enter fuel amount (litres): "))
        itemsPurchased[fuelType] = fuelAmt #adds it itemsPurchased Dictionary
        
        needLubricant = random.choice(["Y", "N"])
        if needLubricant == "Y":
            lubeType = random.choice(['5W-30', '5W-40', '15W-40', 'SAE-40'])
            lubeAmt = int(input("Enter lubricant amount: "))
            itemsPurchased[lubeType] = lubeAmt
            
        for item in itemsPurchased: #item refers to the dictionary key
            if not inventory[item]["maxCapacity"]:
                total+= inventory[item]["price"]*lubeAmt
            else:
                total += inventory[item]["price"]*fuelAmt
            
        try:
            tax = inventory[lubeType]["price"] * lubeAmt * 0.16
        except Exception:
            tax = 0
            
        total += tax    
    
    def CODpayment():
        paymentType = "Cash tendered"
                   
        amount = float(input("Enter Cash tendered: "))
                
        if amount < total:
            difference = total - amount
            amount = float(input(f"Needs ${difference} more!\n Enter Cash tendered again: "))
                    
    
        
        change = amount - total
    def printReceipt():
        print(f"\n\n\n{todaysDate}\nType of Customer: {typeOfCustomer}\n----")
        print(*(f"{key}: {value}\n" for key, value in itemsPurchased.items()))
        print(f"----\nGCT = ${tax}\ntotal = ${total}\n{paymentType} = ${amount}\nChange = ${change:.2f}\n\n")
    
    
    

itemsPurchased = ['5W-30']


def addChargeCustomer():
    customer = ChargeCustomer()
    
    if not chargeCustomers:
        customer.id = 0
    else:
        customer.id = chargeCustomers[-1].id +1
        
    
    customer.name = input("Enter Customer name: ")
    customer.numOfRep = input("Enter the number of representatives: ")
    
    for i in range(int(customer.numOfRep)):
        customer.plateNum.apppend(input(f"Enter the license pla number for Represetative {i}: "))
    

    opt = random.randint(0,1)
"""
while True:   
    opt = input("Serve Customer: 1\nAdd Charge Customer: 2\nUpdate Charge Customer: 3\nDelete Charge Customer: 4\nMake payment to charge account: 5\nRefuel tank: 6\nGenerate report: 7\nEXIT PROGRAM: 8\n  Selection: ")
    if opt == '1':
        print("COD: 1\nCharge: 2\n  Selection: ")
        if selection == '1':
            serveCustomer("COD")
        elif selction == "2":
                serveCustomer("Charge")
                 
    elif opt == '8':
        break
""" 
serveCustomer()
=======
    opt = random.randint(1,2)
    
        
     


def serveCustomer():
    gct = 0.16
    total = 0
    for i in range(len(itemsPurchased)):
        if inventory[itemsPurchased[i]]["maxCapacity"]==None:
            total+= (inventory[itemsPurchased[i]]["price"]*gct) + inventory[itemsPurchased[i]]["price"]
        else:
            total += inventory[itemsPurchased[i]]["price"]
    
    print(f"total = {total}")
    

   
while True:   
    opt = input("Serve Customer: 1\nAdd Charge Customer: 2\nUpdate Charge Customer: 3\nDelete Charge Customer: 4\nMake payment to charge account: 5\nRefuel tank: 6\nGenerate report: 7\nEXIT PROGRAM: 8\n  Selection: ")
    if opt == 1:
        serveCustomer()
    elif opt == 8:
        break
    

