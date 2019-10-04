def print_squares(numbers):
    for number in range(1,numbers+1):
        squared = number*number
        print('The square of {0} is {1}'.format(number,squared))
def main():
    number_of_integers = int(input('Enter a positive integer'))
    if(number_of_integers<0):
        print('You entered an invalid value. Exiting the program!')
    else:
        print_squares(number_of_integers)

main()