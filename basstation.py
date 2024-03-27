
class ChargeCustomer:
    def  __init__(self, id, name, numOfRep, pref, plateNum=[]):
        self.id = id
        self.name = name
        self.numOfRep = numOfRep
        self.pref = pref
        self.plateNum = plateNum
    
    def display(self):
        print(f"ID: {self.id}\nName: {self.name}\nNumber of Representatives: {self.numOfRep}\nPreference: {self.pref}\nLicense Plate Numbers: {self.plateNum}")
       

inventory = {"E10-87":{"maxCapacity":75708.23,
                       "price":184.90},
        
            "E10-90":{"maxCapacity":113562.35,
                      "price":193.60},
            
            "diesel":{"maxCapacity":94635.29,
                      "price":182.},
            
            "5W-30":{"maxCapacity":None,
                     "price":2900.00},
            
            "5W-40":{"maxCapacity":None,
                     "price":3500.00},
            
            "15W-40":{"maxCapacity":None,
                      "price":3600.00},
            
            "SAE-40":{"maxCapacity":None,
                      "price":2100.00}
            }

date = "01/01/2000"