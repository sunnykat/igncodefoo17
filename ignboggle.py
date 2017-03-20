#Python Number Boggle
#By Michael Rohn for CodeFoo Challenge!
import random

#Establishing an empty array at the highest scope to store our comparison solutions.
solutions = []

def randomNumbers () :
    #Base choice of numbers, can be expanded for larger grids.
    numbers = [0,1,2,3,4,5,6,7,8,9]
    #Array of numbers that will be outputted to our board.
    randomnumbers = []
    #Total count of numbers available so that program can be increased in scope depending on the array of numbers above.
    numcount = len(numbers) - 1

    #Runs a number of times based on the length of the numbers array above.
    for i in range (numcount,0,-1):
        #Selects a randomized number between 0 and the last index in the array of numbers.
        rand = random.randint(0,i)
        #Appends the selected value from the number array to our output array while removing that value from the original array to avoid duplicates.
        randomnumbers.append(numbers.pop(rand))
    #returns our output array to be used in the board constructor.
    return randomnumbers

def drawBoard (randomNums) :
    #Draw a 3x3 grid using random numbers from 0-9 with a nice lil boggle esc border.
    print " -------"
    print "| {} {} {} |".format(randomNums[0], randomNums[1], randomNums[2])
    print "| {} {} {} |".format(randomNums[3], randomNums[4], randomNums[5])
    print "| {} {} {} |".format(randomNums[6], randomNums[7], randomNums[8])
    print " -------"
    return

def compareBoard (randomNums) :
    #Goes through the array of random numbers to compare for solutions with each type of comparison set to run only at certain positions of the grid.
    #In order to expand the grid, you'd also have to expand the comparisions set to each position.
    #Better organization with a switch/case structure would make things a bit more readable. But Python doesn't support those particular
    #types of validation.
    for i in range(0,8,1):
        if i != 2 and i != 5 and i !=8:
            if randomNums[i] + randomNums[i+1] == 9:
                solutions.append("{} + {} = 9".format(randomNums[i],randomNums[i+1]))
        if i != 2 and i < 5:
            if randomNums[i] + randomNums[i+4] == 9:
                solutions.append("{} + {} = 9".format(randomNums[i],randomNums[i+4]))
        if i != 0 and i < 6 and i != 3 :
            if randomNums[i] + randomNums[i+2] == 9:
                solutions.append("{} + {} = 9".format(randomNums[i],randomNums[i+2]))
        if i < 6:
            if randomNums[i] + randomNums[i+3] == 9:
                solutions.append("{} + {} = 9".format(randomNums[i],randomNums[i+3]))
        if i == 2 or i == 5 :
            if (randomNums[i] + randomNums[i-1] + randomNums[i+1]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i-1], randomNums[i+1]))
        if i == 0 or i == 3 or i == 6:
            if (randomNums[i] + randomNums[i+1] + randomNums[i+2]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+1], randomNums[i+2]))
        if i == 3 or i == 6 :
            if (randomNums[i] + randomNums[i-2] + randomNums[i+2]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i-2], randomNums[i+2]))
        if i == 0 or i == 3 :
            if (randomNums[i] + randomNums[i+4] + randomNums[i+5]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+4], randomNums[i+5]))
            if (randomNums[i] + randomNums[i+4] + randomNums[i+2]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+4], randomNums[i+2]))
        if i == 0 :
            if (randomNums[i] + randomNums[i+4] + randomNums[i+8]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+4], randomNums[i+8]))
            if (randomNums[i] + randomNums[i+4] + randomNums[i+6]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+4], randomNums[i+6]))
        if i == 2 :
            if (randomNums[i] + randomNums[i+2] + randomNums[i+4]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+2], randomNums[i+4]))
            if (randomNums[i] + randomNums[i+2] + randomNums[i+6]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+2], randomNums[i+4]))
        if i == 0 or i == 1 or i == 3 or i == 4 :
            if (randomNums[i] + randomNums[i+1] + randomNums[i+3]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+1], randomNums[i+3]))
            if (randomNums[i] + randomNums[i+3] + randomNums[i+4]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+3], randomNums[i+4]))
        if i != 2 and i < 5 :
            if (randomNums[i] + randomNums[i+1] + randomNums[i+4]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+1], randomNums[i+4]))
        if i == 1 or i == 2:
            if (randomNums[i] + randomNums[i+2] + randomNums[i+5]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+2], randomNums[i+5]))
            if (randomNums[i] + randomNums[i+3] + randomNums[i+5]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+3], randomNums[i+5]))
        if i == 1 or i == 2 or i == 4 or i == 5:
            if (randomNums[i] + randomNums[i+2] + randomNums[i+3]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+2], randomNums[i+3]))
        if i == 2 or i == 5 :
            if (randomNums[i] + randomNums[i+2] + randomNums[i+1]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+2], randomNums[i+1]))
        if i == 0 or i == 1 :
            if (randomNums[i] + randomNums[i+3] + randomNums[i+7]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+3], randomNums[i+7]))
        if i < 3:
            if (randomNums[i] + randomNums[i+3] + randomNums[i+6]) == 9:
                solutions.append("{} + {} + {} = 9".format(randomNums[i],randomNums[i+3], randomNums[i+6]))

#Sets a variable to the results of our randomnumber function.
randomNums = randomNumbers()
#--Uncomment below to show the array of randomized numbers.--
# print randomNums
#Runs the function to print our game board with the variable established above used as input.
drawBoard(randomNums)
#Runs our comparison function which appends the solutions found to the global variable solutions.
compareBoard(randomNums)
#Creates a variable with the total number of solutions that were found.
solutionCount = len(solutions)
print "Solutions:"
#If there are no solutions it prints that fact.
if solutionCount == 0:
    print "No solutions found..."
#Otherwise, it will loop through a total number of times exlusively equal to the number of solutions
#And print each solution that was found.
else :
    for i in range(0,solutionCount,1):
        print solutions[i];
