user_input = input('Enter a string: ')
last_characters = user_input[-3:]
if len(user_input)>2:
    if(last_characters == 'ing'):
        print(user_input + 'ly')
    else:
        print(user_input + 'ing')
else:
    print(user_input)