
employee_file = open('employees.txt', 'r')

my_employees = []

for employee in employee_file:
    my_employees.append(employee)
    my_employees = employee.split(' - ')
    
    



print(my_employees)

employee_file.close()