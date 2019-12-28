import sys #Note that we import the sys module to take care of abnormal termination of the program

def close_files(file_lst):
    file_lst[0].close()
    file_lst[1].close()

#Any Division by Zero or ValueError generated here will be passed on to the calling function 
# ---the main() function where they will be handled.
#Note that since the main() function does not have a catch-all except block, any other exceptions will not be handled.
def process_data(file_lst):
    f = file_lst[0]
    f2 = file_lst[1]
    for line in f:
        n_lst = line.split(',')
        n1 = int(n_lst[0])
        n2 = int(n_lst[1])
        quo = n1/n2
        my_quo = '{0:3.2f}'.format(quo)
        f2.write(str(n1)+','+str(n2)+','+ str(my_quo) +'\n')
        
#Open files.  The FileNotFoundError is handled where it is generated
def open_files():
    try:
        f = open('input.txt', 'r')
        f2 = open('output.txt', 'w') 
        return ([f, f2])
    except FileNotFoundError: 
        print('File Does Not Exist\nPrinting from open_files() function') 
        sys.exit()
        
def process_data1(fl):
    process_data(fl)
    
#Define the main function.  We have broken down the tasks into open file, process and close files.
# The ZeroDivisionError and ValueError are generated in the process_data() function 
# but will be handled in the main() function
def main():
    file_lst = open_files()
    try:
        process_data1(file_lst)
        close_files(file_lst)
    except ZeroDivisionError:
        print('Division by zero is not allowed!!\nPrinting from main function')
    except ValueError:
        print('You need to enter a numeric value\nPrinting from main function')

main()