students = [

["Rahul", 21, "Python"],

["Priya", 22, "Data Science"],

["Aman", 20, "Machine Learning"]

]

print("Nested list is: ", students)
print(students[0][0]) #to print Rahul's name, as it contains a list again, which is itself inside a list hence we give the index of inside list to print specific requirements, students[0] -> will print ["Rahul", 21, "Python"], and to print Rahul we will provide the index position of Rahul which is [0], hence students[0][0]


print(students[1][1]) #to print priyas age 
print(students[2][2]) #to print Aman's course

print(students[1]) #complete record of priya

students[0][2] = "AI"
print(students[0][2])

students.append(["Kartik", 23, "AI/ML"])
print(students) # to add manually a new record of student


