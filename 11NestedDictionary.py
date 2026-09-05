employee = {
    "name": "Amit",
    "department": "Engineering",

    "skills": {
        "language": "Python",
        "database": "PostgreSQL",
        "cloud": "AWS"
    },

    "salary": 80000
}

# Print employee name
print(employee["name"])

# Print department
print(employee["department"])

# Print complete skills dictionary
print(employee["skills"])

# Print programming language
print(employee["skills"]["language"])

# Print database
print(employee["skills"]["database"])

# Print cloud technology
print(employee["skills"]["cloud"])

# Change Python to Python + JavaScript
employee["skills"]["language"] = "Python + JavaScript"

# Change salary
employee["salary"] = 90000

# Add experience
employee["experience"] = 3

# Add another skill under skills dictionary
employee["skills"]["framework"] = "Django"

print(employee)


#How nested dictionaries are accessed ?
#First we have our dictionary named "employee" which has some items under it and within its item there is also another dictionary named "skills" now to access skills content, first we will access the skill, through employee

# By -> employee["skills"], once we have accessed the skillss now we will access inside skill through nesting
 
# which will look like 

#employee["skills"]["database"] 
#to access whats the database the person have skilled

# Go to employee → find "skills" → inside it find "database".
