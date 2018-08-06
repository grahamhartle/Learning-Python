''' This program uses 'f' strings. You may need to change
    it for your version of Python'''

'''
    Create a Student class with the attributes
    name
    major
    gpa
    '''

class Students:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    '''
    Create the function on_honour_roll
    Checks the students gpa and if it
    is equal or greater than 3.5 returns
    true
    '''

    def on_honour_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

student1 = Students('Bob', 'Accounting', 3.1)
student2 = Students('Kath', 'Business', 3.5)

# create list os students
students = [student1, student2]

# check if students are on the honour roll
# and print out appropriate message
for student in students:
    if student.on_honour_roll() == False:
        print(f'{student.name} you need to get your grades up!')
    else:
        print(f'{student.name} keep up the good work!')