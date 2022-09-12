#Declare three variables and save the value of the first two added together to the third variable 
a = 10
b = 5
c = a + b
print(c)
print('-------------------------------------')

#Create a function that adds two numbers 
def sum(num1, num2):
    add_numbers = num1 + num2
    return add_numbers

print(sum(45, 67))
print('-------------------------------------')
#Create three variables with name, occupation and company and add them together using string concatenation.
name = "Steven"
occupation = "student"
company = "Codeclan"

print("My name is " + name + " I am a " + occupation + " at " + company)

print('-------------------------------------')
#Create a 2d list of cars to store data, make model etc.
cars = [["Ford", "Fiesta", "red", 3], ["Audi", "A4", "silver", 4], ["Toyota", "Rav4", "black", 5]]
#Add another set of car data to the end of the list
cars.append(["Renault", "Clio", "white", 3])
#Find the colour of the car at position 3 in the list
print("The colour of the " + cars[2][0] + " is " + cars[2][2])