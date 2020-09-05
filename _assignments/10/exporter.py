import csv

def saveToFile(term, jobs):
    file = open(f"{term}-jobs.csv", mode="w")
    writer = csv.writer(file)

    writer.writerow(["title", "company", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))

    return

