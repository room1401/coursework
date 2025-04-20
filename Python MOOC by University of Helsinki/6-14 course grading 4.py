# write your solution here
import bisect as bs

# setup print format
def format(c1, c2, c3, c4, c5, c6):
    return f"{c1:30}{c2:<10}{c3:<10}{c4:<10}{c5:<10}{c6:<10}\n"

info = input("Student information: ")
work = input("Exercises completed: ")
exam = input("Exam points: ")
subj = input("Course information: ")
db = dict()

# create db
with open(info) as file:
    next(file)
    line = file.readline().rstrip()
    while line:
        id, first, last = line.split(";")
        db[id] = {"name": first + " " + last}
        line = file.readline().rstrip()

# get exercise points
with open(work) as file:
    next(file)
    line = file.readline().rstrip()
    while line:
        dummy = line.split(";")
        db[dummy[0]]["work"] = sum(int(x) for x in dummy[1:])
        line = file.readline().rstrip()

# get exam points
with open(exam) as file:
    next(file)
    line = file.readline().rstrip()
    while line:
        dummy = line.split(";")
        db[dummy[0]]["exam"] = sum(int(x) for x in dummy[1:])
        line = file.readline().rstrip()

# get course details
c_info = []
with open(subj) as file:
    for line in file:
        dummy = [x.strip() for x in line.split(":")]
        c_info.append(dummy[1])

# output result as text and csv
with open("results.txt", "w") as res_t, \
    open("results.csv", "w") as res_c:

    title = f"{c_info[0]}, {c_info[1]} credits"
    label = format('name', 'exec_nbr', 'exec_pts.', 'exm_pts.', 'tot_pts.', 'grade')
    
    res_t.write(title + "\n")
    res_t.write("=" * len(title) + "\n")
    res_t.write(label)
    
    # get grade and print
    grading = [15, 18, 21, 24, 28]
    for id, ppl in db.items():
        wpt = ppl["work"] // 4
        score = wpt + ppl["exam"]
        grade = bs.bisect(grading, score)
        line = format(ppl["name"], ppl["work"], wpt, ppl["exam"], score, grade)
        
        res_t.write(line)
        res_c.write(";".join([id, ppl['name'], str(grade)]) + "\n")
