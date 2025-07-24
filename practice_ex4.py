##This program request a user for their score and print out
##their final grade letters.

score = float(input("Enter your score: "))
if score >= 90:
    print('Your grade is A')
elif score >= 80:
    print('Your grade is B')
elif score >= 70:
    print('Your grade is C')
else:
    print('Your grade is F')