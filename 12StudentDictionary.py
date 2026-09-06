# Student Profile Using Dictionary
student = {

"name": "Rahul",

"age": 22,

"course": "Python",

"city": "Bangalore",

"marks": 88

}

# Print the complete dictionary

print("Student information: ", student)

#Print the student's name

print(student["name"])

#Print their course

print(student["course"])

# print all keys

print(student.keys()

#to print all key-value pairs

print("All key value pairs: ", student.items())

#To change the marks to 
student["marks"] = 92
print(student["marks"])


#to add student email

student["email"] =  "student@gmail.com"

#to add student email
student["phone"] =  6789998212

#to remove city
student.pop("city")

#Use get() method to receive name

print(student.get("name"))


#To copy the dictionary

student_copy = student.copy()

print(student_copy)

# Returns all the keys

print(student_copy.keys())


# Returns all the values

print(student_copy.values())

# Returns all key-value pairs
print(student_copy.items())

# Retrieves the value of a key

print(student_copy.get("name"))

print(student_copy.get("email")) #here the doesn't exist so it prints, none


# Used to add or modify key-value pairs
student_copy.update({"marks": 92})

# to add new key
student_copy.update({"email": "rahul@gmail.com"})

