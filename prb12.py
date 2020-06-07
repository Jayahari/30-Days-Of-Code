class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)



class Student(Person):
    def __init__(self, firstName, lastName ,idNum , scores):
        Person.__init__(self, firstName, lastName,idNum)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        iSum = 0
        for i in range (0,len(scores)) :
            iSum = iSum + scores [i]
        iSum = iSum / len(scores)

        if iSum < 40 :
            return 'T'
        elif iSum >=40 and iSum <55 :
            return 'D'
        elif iSum >=55 and iSum <70 :
            return 'P'
        elif iSum >=70 and iSum <80 :
            return 'A'
        elif iSum >=80 and iSum <90 :
            return 'E'
        elif iSum >=90 and iSum <=100 :
            return 'O'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())