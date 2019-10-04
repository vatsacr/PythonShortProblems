number_one = int(input('Enter the first two digit number'))
number_two = int(input('Enter the second two digit number'))
number_three = int(input('Enter the third two digit number'))

if(number_one==number_two==number_three):
    print('Three times the sum of {0},{1} and {2} is {3}'.format(number_one,number_two,number_three,3*(number_one+number_two+number_three)))
else:
    print('Four times the sum of {0},{1} and {2} is {3}'.format(number_one,number_two,number_three,4*(number_one+number_two+number_three)))
