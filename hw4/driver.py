from Employee import Employee
from HourlyEmployee import HourlyEmployee
from FullTimeEmployee import FullTimeEmployee
from Consultant import Consultant
from Vehicle import Vehicle
import pickle
import sys

def main(): 
    run_menu_options()

def run_menu_options():   
    employee_list = read_file_data()
    selection = 1
    
    while selection>=1 and selection<=5:
        print("\n==== Menu ====")
        print("1. To add an Employee")
        print("2. To print the name and address of all the employees")
        print("3. To print the employee name and compensation of all employees")
        print("4. To print the employee name with vehicle information for high mileage vehicles")
        print("5. To exit program")

        try:
            selection = int(input("Your selection: "))
            if selection < 1 or selection > 5:
                raise ValueError
        except ValueError:
            print('You must enter an integer between 1 and 5!')
            print('Try again')
            selection = 1
            continue

        if selection == 1:
            employee_list.append(run_option1())
        elif selection == 2:
            if len(employee_list) == 0: 
                print("No employees in database!")
            else:
                run_option2(employee_list) 
        elif selection == 3:
            if len(employee_list) == 0:
                print("No employees in database!")
            else:    
                run_option3(employee_list)
        elif selection == 4:
            if len(employee_list) == 0:
                print("No employees in database!")
            else:    
                run_option4(employee_list)
        elif selection == 5:
            run_option5(employee_list) 

#load data from .dat file
def read_file_data():  
    my_lst = []
    try:
        el = open('empdata.dat','rb')
    except FileNotFoundError:
        return my_lst
    else : 
        try:
            while(True):
                my_lst.append(pickle.load(el))
        except EOFError:
            el.close()
            return my_lst

#adding employee
def run_option1():
    selection = 0 
    while selection<1 or selection>4:
        try:
            selection = int(input("Type of Emplpyee? (1. Full Time 2. Hourly 3. Consultant) "))
        except ValueError:
            print("Wrong input")
            continue
        
    name,address = get_employee_input()
    make,model,year_of_manufacture,mileage = get_vehicle_input()
    vehicle_object = Vehicle(make,model,year_of_manufacture,mileage)
    
    if selection==1:
        salary = get_fulltime_input()
        employee_object = FullTimeEmployee(name,address,vehicle_object,salary)
    elif selection==2:
        hrwrk,hrrate = get_hourly_input()
        employee_object = HourlyEmployee(name,address,vehicle_object,hrwrk,hrrate)
    elif selection==3:
        prjtype,hrwrk = get_consultant_input()
        employee_object = Consultant(name,address,vehicle_object,prjtype,hrwrk)
        
    return employee_object

#display employee details
def run_option2(my_lst):
    
    for obj in my_lst :
        print(obj)

#display employee name and compensation
def run_option3(my_lst):
    print("\n Employees Name and Compensation of all employees")
    print("===================================================")
    for obj in my_lst:
        print(obj.calculate_compensation())

#display employee name and vehicle data
def run_option4(my_lst):
    print("\n Employees Name and Vehicle data for high mileage vehicles")
    print("=============================================================")
    for obj in my_lst:
        obj.get_for_option4()

#exit the program
def run_option5(my_lst):
    print("You chose to exit the program")
    yes_no = input("Are you sure (Y/N)? ")

    if yes_no.lower() == 'y':
        el = open('empdata.dat', 'wb')
        for obj in my_lst:
            pickle.dump(obj, el)
        el.close()
        sys.exit()
        
def get_employee_input():
    
    employee_name = input("Enter Employee's name : ")
    employee_address = input("Enter Employee's address : ")
    
    return employee_name,employee_address

def get_vehicle_input():
    vehicle_make = input("Enter vehicle's make : ")
    vehicle_model = input("Enter vehicle's model : ")
    
    err_flag = True
    while err_flag:
        try:
            vehicle_year_of_manufacture = int(input("Enter vehicle's year : "))
        except ValueError:
            print('\nEnter a numerical value for year!!')
        else:
            err_flag = False
    
    err_flag = True
    while err_flag :
        try:
            vehicle_mileage = int(input("Enter vehicle's mileage : "))
        except ValueError:
            print('\nEnter an integer value for mileage!!')
        else:
            err_flag = False
    return (vehicle_make,vehicle_model,vehicle_year_of_manufacture,vehicle_mileage)

def get_fulltime_input():
    err_flag = True
    while err_flag:
        try:
            full_time_salary = int(input("Enter salary for full time employee : "))
        except ValueError: 
            print('\nEnter an integer value for salary!!')
        else:
            err_flag = False
    return full_time_salary
    
def get_hourly_input():
    err_flag = True
    while err_flag:
        try:
            hourly_hourly_rate = int(input("Enter rate for Hourly employee : "))
        except ValueError: 
            print('\nEnter an integer value for hourly rate!!')
        else:
            err_flag = False
    
    err_flag = True
    while err_flag:
        try:
            hourly_hours_worked = int(input("Enter hours worked for Hourly employee : "))
        except ValueError: 
            print('\nEnter an integer value for hours worked!!')
        else:
            err_flag = False
    return (hourly_hourly_rate,hourly_hours_worked)

def get_consultant_input():
    err_flag = True
    while err_flag:
        try:
             project_type = int(input("Enter projet type for consultant : "))
        except ValueError: 
            print('\nEnter an integer value for project type!!')
        else:
            err_flag = False
    
    err_flag = True
    while err_flag:
        try:
            hours_worked = int(input("Enter hours worked for consultant : "))
        except ValueError: 
            print('\nEnter an integer value for hours worked!!')
        else:
            err_flag = False
    return (project_type,hours_worked)

main()