#string -> when we use "xyz" is called string
students_name = "Rajan Singh" 
students_course = "Computer Science"


#int -> stands for integer
students_marks_maths = 77
student_age = 16
student_roll_number = 25


#float -> has decimal values
student_aggregate = 88.97
student_height = 5.6


#bool -> boolean values
is_Student_Pass_OR_fail = True
is_Student_Present = True


#list -> ordered, mutable(means values can be changed after assigning), duplicates are allowed
marks_obtained_in_all_subjects = [65, 77, 56, 78, 67]
student_hobbies = ["Reading", "Coding", "Gaming"]


#set -> stores unique values, unordered, mutable
subjects_set = {"Maths", "English", "Maths", "Science", "Social Studies", "Sanskrit"}
student_languages = {"English", "Hindi", "Sanskrit"}


#tuple -> encloses within (), also immutable(values once assigned cannot be changed)
subjects_tuple = ("Maths", "English", "Maths", "Science", "Social Studies", "Sanskrit")
student_grades = ("A", "B", "A", "A", "B")


#dict -> holds a key value pair type data
student = {
    "name": "Rajan",
    "age": 16,
    "city": "Bilaspur",
}


print(students_name)
print(type(students_name))

print(students_course)
print(type(students_course))


print(students_marks_maths)
print(type(students_marks_maths))

print(student_age)
print(type(student_age))

print(student_roll_number)
print(type(student_roll_number))


print(student_aggregate)
print(type(student_aggregate))

print(student_height)
print(type(student_height))


print(is_Student_Pass_OR_fail)
print(type(is_Student_Pass_OR_fail))

print(is_Student_Present)
print(type(is_Student_Present))


print(marks_obtained_in_all_subjects)
print(type(marks_obtained_in_all_subjects))

print(student_hobbies)
print(type(student_hobbies))


print(subjects_set)
print(type(subjects_set))

print(student_languages)
print(type(student_languages))


print(subjects_tuple)
print(type(subjects_tuple))

print(student_grades)
print(type(student_grades))


print(student)
print(type(student))



#####################################################


#type conversions


#string to int 
x = int("100")
print(x)
print(type(x))
# "100" is converted from string to integer 100


#string to float
x = float("45.67")
print(x)
print(type(x))
# "45.67" is converted from string to float 45.67


#int to str
x = str(500)
print(x)
print(type(x))
# 500 is converted from integer to string "500"


#int to bool
x = bool(1)
print(x)
print(type(x))
# 1 is converted from integer to True


#tuple to list
x = list((1, 2, 3))
print(x)
print(type(x))
# (1, 2, 3) is converted from tuple to list [1, 2, 3]


#list to tuple
x = tuple([1, 2, 3])
print(x)
print(type(x))
# [1, 2, 3] is converted from list to tuple (1, 2, 3)


#list to set
x = set([1, 2, 2, 3])
print(x)
print(type(x))
# [1, 2, 2, 3] is converted from list to set {1, 2, 3}
# duplicate value 2 is removed
