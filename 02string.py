message = " Welcome To Python Programming Class "


#to clear up spaces
print(message.strip())

#Convert everything to lowercase
print(message.lower())

#Convert everything to uppercase
print(message.upper())

#Convert to title case
print(message.title())

#Replace "Python" with "Advanced Python"
print(message.replace('Python', 'Advanced Python'))

#Check whether the string starts with "Welcome"
print(message.strip().startswith("Welcome"))

#Check whether it ends with "Class"
print(message.strip().endswith("Class"))

#Check no of counts of 'o'
print(message.count('o'))

#Find the position of "Programming"
print(message.find('Programming'))

#Split the sentence into words
print(message.split())