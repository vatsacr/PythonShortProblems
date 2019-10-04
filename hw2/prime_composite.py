user_input = int(input('Enter a positive number'))
if user_input > 1:   
   for i in range(2, user_input//2): 
       if (user_input % i) == 0: 
           print('{0} is a composite number'.format(user_input)) 
           break
   else: 
       print('{0} is a prime number'.format(user_input)) 
else: 
   print('{0} is a neither a prime or a composite number'.format(user_input))