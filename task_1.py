import gooeypie as gp
import task_1_grades

# Calculate function

def calculate(event):
    task_1_grades.calculate_grade(home, int(user_inp.text), course_types.selected)

# home screen
home = gp.GooeyPieApp("Marks & Grades")
home.set_size(250,200)

# Create widgets
mark_lbl = gp.Label(home, 'Mark:')
course_lbl = gp.Label(home, 'Course Type:')
user_inp = gp.Input(home)
course_types = gp.Radiogroup(home, ["Pass/fail", "Graded"])
calculate_btn = gp.Button(home, 'Calculate', calculate)

# Set grid to 3 rows by 2 columns
home.set_grid(3,2) 

# Add the labels to the window
home.add(mark_lbl, 1,1, align ='right', justify='right')
home.add(course_lbl, 2,1, align ='right',justify='right')
home.add(user_inp,1,2, align ='left')
home.add(course_types,2,2, align ='left')
home.add(calculate_btn,3,2, align ='left')

# Add the other widgets to the window
home.run()