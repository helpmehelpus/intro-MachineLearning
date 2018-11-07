names = input('Enter names separated by commas: ').title().split(',')
assignments = input('Enter assignment counts separated by commas: ').split(',')
current_grades = input('Enter grades separated by commas: ').split(',')

for name, assignment, current_grade in zip(names, assignments, current_grades):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n".format(name, assignment, current_grade, int(current_grade) + 2*int(assignment))
    print(message)