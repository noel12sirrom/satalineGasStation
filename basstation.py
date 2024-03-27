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
        
chargeCustomers = []
       

inventory = {"E10-87":{"maxCapacity":75708.23,
                       "price":184.90},
        
            "E10-90":{"maxCapacity":113562.35,
                      "price":193.60},
            
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
    