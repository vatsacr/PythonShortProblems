from Employee import Employee
class HourlyEmployee(Employee):
    def __init__(self,name,address,vehicle,hoursWorked,hourlyRate):
        super().__init__(name,address,vehicle)
        self.__hoursWorked = hoursWorked
        self.__hourlyRate = hourlyRate

    def get_hourlyRate(self):
        return self.__hourlyRate

    def set_hourlyRate(self,hourlyRate):
        self.__hourlyRate = hourlyRate

    def get_hoursWorked(self):
        return self.__hoursWorked

    def set_hoursWorked(self,hoursWorked):
        self.__hoursWorked = hoursWorked
    
    def calculate_compensation(self):
        compensation = 0
        if(self.__hoursWorked>40):
            compensation = (self.__hoursWorked*self.__hourlyRate)+((self.__hoursWorked-40)*self.__hourlyRate*1.8)
        else:
            compensation = self.__hoursWorked*self.__hourlyRate

            return "{0}'s is ${1:.2f}".format(self.get_name(),compensation)

    def __str__(self):
        print("\nDetails of Hourly Employee are:")
        children = super().__str__()
        children += "\nHour Rate: " + str(self.__hourlyRate) + "\nHour Worked: " + str(self.__hoursWorked)
        return children