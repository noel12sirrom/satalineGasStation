import random
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd =  "GasStation",
    database = "GasStation"
)
cursor = db.cursor()

class ChargeCustomer:
    def  __init__(self, id, name, numOfRep, pref, plateNum=[]):
        self.id = id
        self.name = name
        self.numOfRep = int(numOfRep)
        self.pref = pref
        self.plateNum = plateNum
    
    def display(self):
        print(f"\nID: {self.id}\nName: {self.name}\nNumber of Representatives: {self.numOfRep}\nPreference: {self.pref}\nLicense Plate Numbers: {self.plateNum}")

# variables 
testChargeCust = ChargeCustomer(1,"gas Pro", 2, None, ["brd232", "ej232"])
chargeCustomersList = [testChargeCust]
minDeposit = 10000
maxLitres = 3785.41
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
    preference = ""
    
    #validates if the Charge customer exists in the system and if the proper liscence plates are presented
    def validate():
        nonlocal preference
        givenId = int(input("\nEnter ID: "))
        try:
            cursor.execute("SELECT customer_id FROM chargecustomer")
            results = cursor.fetchall()
            for x in results:
                if x[0] == givenId:  # Access the first column of the result row
                    cursor.execute(f"SELECT customer_name FROM chargecustomer WHERE customer_id = {givenId}")
                    result = cursor.fetchone()
                    print(result[0])
                       
                    cursor.execute(f"SELECT preference FROM chargecustomer WHERE customer_id = {givenId}")
                    result = cursor.fetchone()
                    preference = result[0]    
                    break
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            db.rollback() # isnt needed but can stay in case of soem wild unrelated error
            return False
             
    
        #print out license plate under the under the ID
        print("See List below for plates eligible for fuel")
        cursor.execute(f"SELECT License_plate FROM representatives WHERE customer_id = {givenId}")
        result = cursor.fetchall()
        for row in result:
            print(row)
        while True:
            opt = input("Eligible Plates (Y/N): ").upper()
            if opt == 'Y' :
                return True
            elif opt  == 'N':
                return False
            print("Invalid Entry. Please Enter Y or N.")  
    
    #takes the order of lubricants and fuel and calculates the total with gct
    def takeOrder():
        nonlocal total, fuelAmt, tax, preference
        
        fuelType = input("\nFuel Type: ").upper()
        
        while fuelType not in inventory:
            print("Invalid entry.")
            fuelType = input("\nFuel Type: ").upper()
            
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
                        opt = input("The minimum purchase is two litres for cash payments. Buy more gas? (Y/N): ").upper()
                        if opt == "Y":
                            takeOrder()
                            return CODpayment()  # Terminate and return recursively
                        elif opt ==  "N":
                            break  # Exit the inner loop
                amount = float(input("Enter Cash tendered: "))
                break  # Exit the outer loop
            elif opt == "2":
                paymentType = "Card"
                amount = total
                # Validate if card amount greater than $1000
                if amount < 1000:
                    while True:
                        opt = input("The minimum amount is $1000 for card transactions. Would you like to retake the order and add more items? (Y/N): ").upper()
                        if opt == "Y":
                            takeOrder()
                            return CODpayment()  # Terminate and return recursively
                        elif opt ==  "N":
                            break  # Exit the inner loop
                break  # Exit the outer loop
            else:
                print("Please enter a valid option")
        
        # Check if the amount is less than the total and prompt for additional payment if necessary
        if amount < total:
            difference = total - amount
            amount = float(input(f"Needs ${difference:.2f} more! Enter Cash tendered again: "))
        
        change = amount - total
      
    """def chargePayment():"""
      #get this dine after add customer  
        
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
    
    mainMenu()      

def addChargeCustomer():
    while True:
        if not chargeCustomersList:
            id = 0
        else:
            id = chargeCustomersList[-1].id +1
        
        name = input("Enter Customer name: ")
        
        #validates  that numOfRep is between 1 and  5 inclusive
        while True:
            num = int(input("Enter the number of representatives: "))
            if num > 0 and num <= 5:
                numOfRep = num 
                break
            print("Cannot enter more than 5 representatives or less than one")
        
        #validates if all license plat numbrs given are unique
        plateNum = []
        for i in range(numOfRep):
            while True:
                plate = input(f"Enter the license plate number for Represetative {i+1}: ")
                if plate not in plateNum:
                    plateNum.append(plate)
                    break 
                print("Plate number already entered!") 
                
        #preference is randomly generated
        pref = random.choice(["Deposit", "Maximum Litres"])
        
        customer = ChargeCustomer(id, name, numOfRep, pref, plateNum)
        
        customer.display()
        
        opt = input("\n\nSave [1]\nRemake [2]\nClick any other character to omit: ")
        if opt == "1":
            try:
                cursor.execute("INSERT INTO chargecustomer ( customer_name, number_of_representatives, preference) VALUES (%s, %s, %s)",
                            ( name, numOfRep, pref))
                db.commit() 
                # Get the auto-generated customer_id for the newly inserted customer
                customer_id = cursor.lastrowid
                for plate in plateNum:
                    cursor.execute("INSERT INTO representatives (customer_id, License_plate) VALUES (%s, %s)", (customer_id, plate))
                    db.commit()
                print("\n\nCustomer added successfully")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                db.rollback()
            break
        elif opt == "2":
            continue
    mainMenu()

def deleteChargeCustomer():
    password = "admin"
    givenPassword = input("Enter password: ")
    if givenPassword != password:
        print("incorrect Passowrd")
        mainMenu()
    
    givenId = input("Enter Customer ID Number: ")
    
    try:
        cursor.execute("DELETE from chargecustomer WHERE customer_id=%s", (givenId,))
        db.commit()  
        print("\nRecord deleted successfully")
    except mysql.connector.Error as err:
        print(f"\nError: {err}")
        db.rollback()
         
    mainMenu()

def updateInventory():
    print("\nfeature hasnt been added")
    mainMenu()

def mainMenu():   
    opt = input("\nServe Customer: 1\nAdd Charge Customer: 2\nUpdate Charge Customer: 3\nDelete Charge Customer: 4\nMake payment to charge account: 5\nRefuel tank: 6\nGenerate report: 7\nUpdate inventory: 8\nEXIT PROGRAM: 'ANY OTHER CHARACTER'\n  Selection: ")
    if opt == '1':
        opt = input("Customer Type [COD (1) ,Charge (2)]: ")
        if opt == '1':
            serveCustomer("COD")
        elif opt == '2':
            serveCustomer("charge")
    if opt == "2":
        addChargeCustomer()
    if opt =="4":
        deleteChargeCustomer()
                 
        
mainMenu()