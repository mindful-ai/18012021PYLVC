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


class extEmployee(Employee):
    pass

class extEmployee2(Employee):
    
    def __init__(self, name, age, company, phone, addr):
        super().__init__(name, age, company)
        self.phone = phone
        self.addr  = addr
    
    def setphone(self, value):
        self.phone = value

    def setaddr(self, value):
        self.addr = value

    
    def printinfo(self):
        print("-"*40)
        super().printinfo()
        print("-"*40)
        print(self.addr)
        print("PHONE : ", self.phone)
        print("-"*40)
    

# -----------------------------------------------------

if __name__ == "__main__":

    # -------------------------------------------- EXP - Backward Compatibility

    x = [ ("Anil", 35, "Oracle", 1000000),
          ("Sunil", 36, "Oracle", 1050000),
          ("Raj", 37, "Oracle", 1150000)
        ]

    eobjs = []
    for emp in x:
        obj = extEmployee2(emp[0], emp[1], emp[2], '', '')
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

    # -------------------------------------------- EXP 5

    e = extEmployee2("Ram", 35, "Oracle", "+91876545476", "J P Nagar, Bangalore")
    e.printinfo()
    e.setsalary(1500000)
    e.printinfo()


    # -------------------------------------------- EXP 6

    e1 = extEmployee2("Ram", 35, "Oracle", "+91876545476", "J P Nagar, Bangalore")
    e1.setsalary(1500000)

    e2 = Employee("Raj", 35, "Oracle")
    e2.setsalary(1550000)

    e = e2
    e.printinfo()

