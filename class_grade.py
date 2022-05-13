"""PlAIN ENGLISH
start
create a list to store 5 numbers (float)
capture user's input 5 times for their grades
each time we capture the user's input, we append the number to the list
sort the list ascending, then splice the itmes starting at index 2
once we have three highest numbers in the list, we sum them up and divide by 3
output a message to the user 
end
"""

"""PSUDOCODE
create list

capture input 
append number to the list 

capture input 
append to the list 

capture input 
append to the list 

capture input 
append to the list 

capture input 
append to the list 

sort the list then splice out the two lowest numbers
print message to the user 
"""

grades=[]

grade=input("Enter the 1st grade: ")
grades.append(float(grade))

grade=input("Enter the 2nd grade: ")
grades.append(float(grade))

grade=input("Enter the 3rd grade: ")
grades.append(float(grade))

grade=input("Enter the 4th grade: ")
grades.append(float(grade))

grade=input("Enter the 5th grade: ")
grades.append(float(grade))

grades.sort()

grades=grades[2:]

grades=sum(grades)

result=grades/3

print("Average Grade {0:.2f}%".format(result))