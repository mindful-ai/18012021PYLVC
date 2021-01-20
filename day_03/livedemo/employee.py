class Employee:

    nemployees = 0

    # Data : 
    def __init__(self, name, age, company):
        self.name     = name
        self.age      = age
        self.company  = company
        self.salary   = 0
        self.tax      = 0

    # Functions: 
    def setname(self, value):
        self.name = value
    
    def setage(self, value):
        self.age = value 

    def setcompany(self, value):
        self.company = value
    
    def setsalary(self, value):
        self.salary = value
        self.calctax()
    
    def gettax(self):
        return self.tax

    def getsalary(self):
        return self.salary

    def printinfo(self):
        print("\n")
        print(self.name, "|", self.age,"|", self.company)
        print("-"*40)
        print("SALARY : ", self.salary)
        print("TAX    :", self.gettax())
        print("NET    :", self.salary - self.tax)
        print("\n")

    def calctax(self):
        self.tax = 0.1 * self.salary


# -----------------------------------------------------

if __name__ == "__main__":

    # ------------------------------------------- EXP1

    e = Employee("Kiran", 35, "Oracle")
    e.printinfo()

    e.setsalary(1000000)
    e.printinfo()

    # -------------------------------------------- EXP2

    x = [ ("Anil", 35, "Oracle", 1000000),
          ("Sunil", 36, "Oracle", 1050000),
          ("Raj", 37, "Oracle", 1150000)
        ]

    eobjs = []
    for emp in x:
        obj = Employee(emp[0], emp[1], emp[2])
        obj.setsalary(emp[3])
        eobjs.append(obj)

    for obj in eobjs:
        obj.printinfo()

    
    # calculate 15% hikes
    
    for obj in eobjs:
        currsal = obj.getsalary()
        newsalary = 1.15 * currsal 
        obj.setsalary(newsalary)
    

    for obj in eobjs:
        obj.printinfo()      

    # -------------------------------------------- EXP3

    y = [ ("Anil", 35, "Oracle", 1000000, 99),
          ("Sunil", 36, "Oracle", 1050000, 76),
          ("Raj", 37, "Oracle", 1150000, 65),
          ("Dev", 37, "Oracle", 1150000, 45)
        ]    

    '''
    hike policy
    performance > 90  20%
    performance between 75 and 90 15%
    performance between 50 and 75 10%
    performance below 50 0%
    '''