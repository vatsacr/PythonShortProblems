class Employee:
    def __init__(self,name,address,vehicle):
        self.__name = name
        self.__address = address
        self.__vehicle = vehicle
    
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name
    
    def get_address(self):
        return self.__address

    def set_address(self,address):
        self.__address = address

    def get_vehicle(self):
        return self.__vehicle
    
    def set_vehicle(self,vehicle):
        self.__vehicle = vehicle
    
    def get_for_option4(self):
        
        if self.__vehicle.get_mileage()>78000:
            print("Employee name is : {0} {1}".format(self.get_name(),self.get_vehicle()))
        
    def __str__(self):
        allData = "Employee Name: " + self.__name + "; Employee Address: " + self.__address
        allData +=  "\n" + self.__vehicle.__str__()
        return allData

