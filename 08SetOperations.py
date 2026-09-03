python_students = {"Rahul", "Aman", "Priya", "Karan", "Neha"}

java_students = {"Priya", "Karan", "Rohit", "Simran"}

#printing both the sets

print(f"Python students: {python_students}\nJava students: {java_students}:\n")

print(python_students | java_students) #students learning python or java (or operation, union, |)

print(python_students & java_students) #common students studying both (and operation, intersection, &)

print(f"Students learning python: {python_students - java_students}")# students learning only python

print(f"Students learning java: {java_students - python_students}")# students learning only java



print((python_students | java_students) - (python_students & java_students)) #students belonging to exactly one group

# #All students
#      -
# Common students
#      =
# Students in exactly one group

# OR
print(python_students ^ java_students) # for printing students belonging to exactly one group


# Add a new student
python_students.add("Vikas")
print("After adding Vikas to Python_students:", python_students)

# Remove a student
python_students.remove("Vikas")
print("After removing Vikas from Python_students:", python_students)


# Demonstrating set methods

print("Union:", python_students.union(java_students))

print("Intersection:", python_students.intersection(java_students))

print("Only Python:", python_students.difference(java_students))

print("Exactly one group:",
      python_students.symmetric_difference(java_students))

# Demonstrating discard()
python_students.discard("Vikas")
print("After discard:", python_students)

# remove()   → removes item, but errors if item doesn't exist
# discard()  → removes item if present, otherwise does nothing