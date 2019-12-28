from Employee import Employee
class FullTimeEmployee(Employee):
    def __init__(self,name,address,vehicle,salary):
        super().__init__(name,address,vehicle)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        self.__salary = salary
    
    def calculate_compensation(self):
        compensation = 0
        if(self.__salary<=45000):
            compensation = self.__salary-(self.__salary*0.18)
        elif(self.__salary<82000):
            compensation = self.__salary-(45000*0.18) - ((self.__salary-45000)*0.28)
        
        return "{0}'s is ${1:.2f}".format(self.get_name(),compensation)

    def __str__(self):
        print("\nDetails of Full Time Employees are:")
        children = super().__str__()
        children += "\nSalary: " + str(format(self.__salary,'.2f'))
        return children