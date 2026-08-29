#string -> when we use "xyz" is called string
students_name = "Rajan Singh" 

#int -> stands for integer
students_marks_maths = 77

#float -> has decimal values
student_aggregate = 88.97

#bool -> boolean values
is_Student_Pass_OR_fail = True

#list -> contains homogenous values, mutable(means values can be changed after assigning)
marks_obtained_in_all_subjects = [65, 77, 56, 78, 67]

#set -> helps to deal with common valus and encloses within {}, mutable
subjects_set = {"Maths", "English", "Maths", "Science", "Social Studies", "Sanskrit"}

#tuple -> encloses within (), also immutable(values once assigned cannot be changed)
subjects_tuple = ("Maths", "English", "Maths", "Science", "Social Studies", "Sanskrit")

#dict -> holds a key value pair type data
student = {
    "name": "Rajan",
    "age": 16,
    "city": "Bilaspur",
}

print(students_name)
print(type(students_name))

print(students_marks_maths)
print(type(students_marks_maths))

print(is_Student_Pass_OR_fail)
print(type(is_Student_Pass_OR_fail))

print(marks_obtained_in_all_subjects)
print(type(marks_obtained_in_all_subjects))

print(subjects_set)
print(type(subjects_set))

print(subjects_tuple)
print(type(subjects_tuple))

print(student)
print(type(student))


#####################################################

#type conversions

#string to int 
x = int("100")
print(x)
print(type(x))

#string to float
x = float("45.67")
print(x)
print(type(x))

#int to str
x = str(500)
print(x)
print(type(x))

#tuple to list
x = list((1, 2, 3))
print(x)
print(type(x))

#list to tuple
x = tuple([1, 2, 3])
print(x)
print(type(x))

#list to set
x = set([1, 2, 2, 3])
print(x)
print(type(x))
