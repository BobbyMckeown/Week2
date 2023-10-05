# task 1
UserName = input("Please enter your name: ")
print("Hello " + UserName + "nice to meet you ")

# task 2
celsuis = (int(input("Please enter temp in celsius ")))
ConvertToFahrenheit = (celsuis * 9 / 5) + 32
print('Fahrenheit;', ConvertToFahrenheit, 'Celsius;', celsuis)

# task 3
TotalStudents = (int(input("Enter the total number of students: ")))
LabGroupSize = (int(input("Type the amount of people you want in a group: ")))
AmountOfGroups = TotalStudents // LabGroupSize
RemainingStudents = TotalStudents % LabGroupSize
print("There will be ", AmountOfGroups, "groups \n There will be ", RemainingStudents, " in the reminding group")


#task 4
AmountOfStudents = int(input("How many total students: "))
AmountOfSweats = int(input("how many sweats is there: "))
AmountForEachStudent = AmountOfSweats // AmountOfStudents
LeftOver = AmountOfSweats % AmountOfStudents
print("Each students will get ", AmountForEachStudent ,"\n There will also have ",LeftOver," left over")