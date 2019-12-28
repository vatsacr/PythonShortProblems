class Vehicle:
    def __init__(self,make,model,year_of_manufacture,mileage):
        self.__make=make
        self.__model=model
        self.__year_of_manufacture=year_of_manufacture
        self.__mileage=mileage
    
    def get_make(self):
        return self.__make
    
    def set_make(self,make):
        self.__make = make

    def get_model(self):
        return self.__model
    
    def set_model(self,model):
        self.__model = model
    
    def get_year_of_manufacture(self):
        return self.__year_of_manufacture
    
    def set_year_of_manufacture(self,year_of_manufacture):
        self.__year_of_manufacture = year_of_manufacture
    
    def get_mileage(self):
        return self.__mileage

    def set_mileage(self,mileage):
        self.__mileage = mileage
    
    def __str__(self):
        return "Make: " + self.__make + "; Model: " + self.__model + "; Year: " + str(self.__year_of_manufacture) + "; Mileage: " + str(self.__mileage)
