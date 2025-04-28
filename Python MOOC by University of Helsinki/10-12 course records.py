'''Please write an interactive application for keeping track of your studies. 
The internal structure is up to you, but this would be a good opportunity to 
practice creating a similar structure as in the PhoneBook example above.
'''

# Write your solution here:
class Course:
    def __init__(self, name, credit):
        self.__name = name
        self.__credit = credit
        self.__best = 0

    @property
    def name(self):
        return self.__name

    @property
    def credit(self):
        return self.__credit
    
    def best(self):
        return self.__best

    def update(self, grade):
        if grade > self.__best:
            self.__best = grade

    def __str__(self):
        return f"{self.__name} ({self.__credit} cr) grade {self.__best}"


class Record:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name, credit, grade):
        if name not in self.__courses:
            self.__courses[name] = Course(name, credit)
        
        self.__courses[name].update(grade)

    def getData(self, name):
        if name in self.__courses:
            return self.__courses[name]

    def getStats(self):
        taken = len(self.__courses)
        credits, grades = 0, 0
        stats = [0] * 5

        for subj in self.__courses.values():
            credits += subj.credit
            grades += subj.best()
            stats[subj.best() - 1] += 1

        return taken, credits, grades, stats


class TrackerApp:
    def __init__(self):
        self.__tracker = Record()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def insert(self):
        name = input("name: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        self.__tracker.add_course(name, credit, grade)

    def search(self):
        name = input("name: ")
        data = self.__tracker.getData(name)
        print(data if data else "no entry for this course")

    def report(self):
        taken, credits, grades, stats = self.__tracker.getStats()
        print(f"{taken} completed courses, a total of {credits} credits")
        print(f"mean {grades / taken :.1f}" if taken else "mean 0")
        print("grade distribution")
        for i in range(len(stats) - 1, -1, -1):
            print(f"{i + 1}: {'x' * stats[i]}")

    def execute(self):
        self.help()
        actions = {"1": self.insert, "2": self.search, "3": self.report}
        while True:
            command = input("\ncommand: ")
            if command == "0":
                break
            if command in actions:
                actions[command]()


application = TrackerApp()
application.execute()
