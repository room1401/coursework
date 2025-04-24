'''
Please write a function named final_points(), which returns the 
final exam points received by the students, in a dictionary format, 
following these criteria:

- If there are multiple submissions for the same task, the submission 
with the highest number of points is taken into account.
- If the submission was made over 3 hours after the start time, the 
submission is ignored.
- The tasks are numbered 1 to 8, and each submission is graded with 0 
to 6 points.

In the dicionary returned the key should be the name of the student, 
and the value the total points received by the student.
'''

# Write your solution here
import csv
from datetime import datetime as dt, timedelta as td

def final_points():
    db, format = dict(), "%H:%M"
    limit = td(hours=3)
    
    with open("start_times.csv") as file:
        data = csv.reader(file, delimiter=";")
        for ppl, time in data:
            time = dt.strptime(time, format) + limit
            db[ppl] = {"deadline": time, "best": [0] * 8}
    
    with open("submissions.csv") as file:
        data = csv.reader(file, delimiter=";")
        for ppl, task, pts, end in data:
            task, pts = int(task), int(pts)
            end = dt.strptime(end, format)
            if db[ppl]["deadline"] >= end and \
                pts > db[ppl]["best"][task - 1]:
                db[ppl]["best"][task - 1] = pts

    return dict((k, sum(v["best"])) for k, v in db.items())
