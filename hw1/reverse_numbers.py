user_numbers = int(input('Please enter a positive four digit number'))
def is_four_digit(numbers):
    digits=0
    while(numbers>0):
        numbers//=10
        digits+=1
    return digits==4
def reverse_number(numbers):
    if(is_four_digit(numbers)):
        reverse = 0
        while (numbers > 0):
            reverse *= 10
            reverse += numbers % 10
            numbers //= 10
        return reverse
if(user_numbers>0 and is_four_digit(user_numbers)):
    print('{0} in reverse is {1}'.format(user_numbers,reverse_number(user_numbers)))
else:
    print('You entered an invalid value.\nExiting the program!')