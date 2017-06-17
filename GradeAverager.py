class GradeAverager:


    def __init__(self):
        print "\nLet's figure out those grades!\nUse the getGrades() method to get started.\n"
        self.grades = []
        self.getGrades()
        self.getGPA()

    def getGrades(self):
        numOfGrades = input("\nHow many grades will there be? ")
        print "\nGreat! Lets get started\n"
        counter = 0
        while(counter < numOfGrades):
            letter = raw_input("Letter grade: ").lower()
            credits = input("Num of credits: ")
            self.grades.append((letter, credits))
            counter += 1
        print "\nYou can now get your GPA with the getGPA() method.\n"

    def clear(self):
        while(len(self.grades) > 0):
            self.grades.pop

    def getGPA(self):
    	total = 0
    	totalCreds = 0
    	for (letter, credit) in self.grades:
    		if letter == 'a':
    			total += credit * 4
    			totalCreds += credit
    		elif letter == 'a-':
    			total += credit * 3.7
    			totalCreds += credit
    		elif letter == 'b+':
    			total += credit * 3.3
    			totalCreds += credit
    		elif letter == 'b':
    			total += credit * 3.0
    			totalCreds += credit
    		elif letter == 'b-':
    			total += credit * 2.7
    			totalCreds += credit
    		elif letter == 'c+':
    			total += credit * 2.3
    			totalCreds += credit
    		elif letter == 'c':
    			total += credit * 2.0
    			totalCreds += credit
    		elif letter == 'c-':
    			total += credit * 1.7
    			totalCreds += credit
    		elif letter == 'd+':
    			total += credit * 1.3
    			totalCreds += credit
    		elif letter == 'd':
    			total += credit * 1.0
    			totalCreds += credit
    		elif letter == 'd-':
    			total += credit * .7
    			totalCreds += credit
    		elif letter == 'e':
    			total += credit * .0
    			totalCreds += credit
    	print "Your total grade score is: " + repr(total)
    	print "Your total number of credits taken is: " + repr(totalCreds)
    	print "Your GPA is: " + repr((total/totalCreds))
