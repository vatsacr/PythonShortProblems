
number_one = int(input("Input the first number : "))
number_two = int(input("Input the second number : "))
number_three = int(input("Input the third number : "))
if number_one > number_two:
    if number_one < number_three:
        median = number_one
    elif number_two > number_three:
        median = number_two
    else:
        median = number_three
else:
    if number_one > number_three:
        median = number_one
    elif number_two < number_three:
        median = number_two
    else:
        median = number_three
print("Median of above three numbers - ", median)