'''
    This program calculates how many leap years
    there have been since the user was born.

    The current_year is hard coded to 2018,
    but eventually I would like it to be taken
    from the current date.
'''

current_year = 2018

# leap_year is set to an empty list
leap_year = []

age = int(input('Enter your age: '))

# calculates the year the user was born
num_year = current_year - age 

# calculates the number of leap years that have passed
# since the users birth, and appends them into the
# leap_year list
while num_year < current_year:
    if num_year % 4 == 0:
        leap_year.append(num_year)
    num_year += 1

# just prints out all of the leap years
print(leap_year)
print(len(leap_year))
