from Employee import Employee
class Consultant(Employee):
    def __init__(self,name,address,vehicle,hoursWorked,projectType):
        super().__init__(name,address,vehicle)
        self.__hoursWorked = hoursWorked
        self.__projectType = projectType

    def get_hoursWorked(self):
        return self.__hoursWorked

    def set_hoursWorked(self,hoursWorked):
        self.__hoursWorked = hoursWorked

    def get_projectType(self):
        return self.__projectType

    def set_projectType(self,projectType):
        self.__projectType = projectType

    def calculate_compensation(self):
        compensation = 0
        if(self.__projectType == 1):
            compensation = self.__hoursWorked*55
        elif(self.__projectType ==2):
            compensation = self.__hoursWorked*70
        else:
            compensation = self.__hoursWorked*85

        return "{0}'s is {1:.2f}".format(self.get_name(),compensation)

    def __str__(self):
        print("\nDetails of Consultant are:")
        children = super().__str__()
        children += "\nProject Type: " + str(self.__projectType) + "\nHour Worked: " + str(self.__hoursWorked)
        return children