'''Asks a user to input their age,
    then converts that into the number
    of seconds they have lived.
    '''

def age_in_seconds():
    '''
    variables:  age - takes user input
                seconds - conversion of age into seconds
    '''

    age = input('How old are you: ')
    seconds = int(age) * 365 * 24 * 60 * 60
    num = calc_leap_years(int(age))
    leap_years = num # the number of leap years from birth to current year
    extra_seconds = leap_years * 24 * 60 * 60
    seconds += extra_seconds
    print(f'Your age in seconds is: {seconds}')

def calc_leap_years(num):
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

# calculates the year the user was born
    num_year = current_year - num

# calculates the number of leap years that have passed
# since the users birth, and appends them into the
# leap_year list
    while num_year < current_year:
        if num_year % 4 == 0:
            leap_year.append(num_year)
        num_year += 1

# just returns the number of leap years
    return len(leap_year)

age_in_seconds()
