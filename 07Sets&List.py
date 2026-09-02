numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60] 

print("List is: ", numbers) # to print the given list

new_numbers = set(numbers)
print(new_numbers) #converting list to set

#after printing the new type conversion our list to set, common numbers present in list appears to be gone and we only get them once

new_list = list(new_numbers)
print(new_list) #converting set to list

print(len(numbers)) #size of original list named "numbers", also prints the number of original elements

print(len(new_list)) #Prints the number of unique elements

student_names = [
    "Aman", "Chitransh", "Rajat", "Shree", "Kartik", "Aman"
]


#Another example using duplicate student names
print("New student names: ", student_names)

new_student_set = set(student_names)
print(new_student_set)

new_list_students = list(new_student_set)
print(new_list_students)

print(len(student_names)) #original student names(have common name)

print(len(new_list_students)) #removes common name after converting into a set

