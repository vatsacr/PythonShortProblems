totalNumbers = int(input('Enter a positive integer: '))
total=0
if(totalNumbers>0):
    for number in range(totalNumbers+1):
        total=total+number
        
    print('The sum of {1} positive numbers is {0}'.format(total,totalNumbers))
else:
    print('You entered an invalid value. Exiting the program!')