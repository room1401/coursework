'''
In this exercise you will write a program for printing out grade statistics 
for a university course. The program asks the user for results from different 
students on the course. These include exam points and numbers of exercises 
completed. The program then prints out statistics based on the results. Exam 
points are integers between 0 and 20. The number of exercises completed is an 
integer between 0 and 100. The program keeps asking for input until the user 
types in an empty line. You may assume all lines contain valid input, which 
means that there are two integers on each line, or the line is empty.

When the user types in an empty line, the program prints out statistics. The 
exercises completed are converted into exercise points, so that completing at 
least 10% of the exercises grants one point, 20% grants two points, and so 
forth. Completing all 100 exercises grants 10 exercise points. The number of 
exercise points granted is an integer value, rounded down.

There is also an exam cutoff threshold. If a student received less than 10 
points from the exam, they automatically fail the course, regardless of their 
total number of points. Floating point numbers should be printed out with one 
decimal precision.
'''

# Write your solution here
import bisect as bs

def getData(res=[]):
    while True:
        entry = [int(x) for x in input("Points:").split()]
        if not entry:
            break
        res.append(entry)

    return res

def grading(exam, score):
    if exam < 10:
        return 0

    return bs.bisect([15, 18, 21, 24, 28], score)

def getStat(data: list):
    grades = [0] * 6
    size, total = len(data), 0
    while data:
        exam, work = data.pop()
        score = exam + work // 10
        grades[grading(exam, score)] += 1
        total += score

    return size, total, grades

def showStat(data: list):
    size, total, grades = getStat(data)
    avg = total / size
    prate = (1 - grades[0] / size) * 100
    
    print("Statistics:")
    print(f"Points average: {avg:.1f}")
    print(f"Pass percentage: {prate:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        star = "*" * grades[i]
        print(f"  {i}: {star}")

def main():
    data = getData()
    showStat(data)

main()
