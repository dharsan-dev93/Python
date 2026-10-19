# student cut-off calculator.

name = input("Enter your name: ")
maths_marks = int(input("Enter your maths marks: "))
physics_marks = int(input("Enter your physics marks: "))
chemistry_marks = int(input("Enter your chemistry marks: "))
total_marks = maths_marks + physics_marks + chemistry_marks
pm = physics_marks / 2
cm = chemistry_marks / 2
cut_off_marks = maths_marks + pm + cm
print("Student name :",name)
print("Total marks :",total_marks)
print("Cut-off marks :",cut_off_marks)