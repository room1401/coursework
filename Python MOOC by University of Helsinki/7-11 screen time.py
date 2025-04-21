# Write your solution here
from datetime import datetime as dt, timedelta as td

format = "%d.%m.%Y"

# get user inputs
fname = input("Filename: ")
start = dt.strptime(input("Start: "), format)
days = int(input("Days "))
print("Screen time:")
times, total = [], 0
for i in range(days):
    dummy = input("Time: ").split()
    total += sum(int(x) for x in dummy)
    date = (start + td(days=i)).strftime(format)
    times.append((date, "/".join(dummy)))

# write data
with open(fname, "w") as file:
    file.write(f"Time period: {start.strftime(format)}-{times[-1][0]}\n")
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {total / days:.1f}\n")
    for (date, time) in times:
        file.write(f"{date}: {time}\n")
