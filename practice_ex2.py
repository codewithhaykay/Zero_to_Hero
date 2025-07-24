## This program request a user for a number and determines
#whether the number is positive, negative or zero
requested_number = int(input("Enter a number: "))
if requested_number > 0:
    print(f'{requested_number} is positive')
elif requested_number < 0:
    print(f'{requested_number} is negative')
    
else:
    print(f'{requested_number} is zero')