# tuple is a immutable data type enclosed within ()

technologies = ("Python", "Java", "Python", "C++", "JavaScript", "Python")

# Print the tuple
print("Technologies: ",technologies)

# Print its type
print(type(technologies))

# Print the first item
print("First item: ",technologies[0])

#print last item
print("Last itemt: ",technologies[-1])

#slicing the tuple
print(technologies[1:3])
print(technologies[1:5:2])

#counting occurence of "Python"
print(technologies.count("Python"))

#Index of C++
print(technologies.index("C++"))

#Length of tuple
print(len(technologies))

new_technologies_list = list(technologies)
print(new_technologies_list)
print(type(new_technologies_list))

#Adding "Go" after onverting into a list
new_technologies_list.append("Go")
print("After adding new item: ",new_technologies_list)

#Converting back into a tuple
new_technologies_tuple = tuple(new_technologies_list)

print("After converting:", new_technologies_tuple)

#Tuples are immutable because once we set the value to a tuple we can't change it afterwards


