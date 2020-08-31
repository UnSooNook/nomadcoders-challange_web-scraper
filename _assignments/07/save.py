import csv


def saveCompany(company):
    file = open(f"{company['name']}.csv", mode="w")
    writer = csv.writer(file)
    
    writer.writerow(["place", "title", "time", "pay", "date"])
    jobs = company["jobs"]
    for job in jobs:
        writer.writerow(list(job.values()))
    
    file.close()

    return


def saveToFile(recruitInfo):
    i = 1
    for company in recruitInfo:
        print(f"Saving {company['name']}..({i}/{len(recruitInfo)})")
        saveCompany(company)
        i += 1
    
    return

