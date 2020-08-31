import requests
from bs4 import BeautifulSoup

alba_url = "http://www.alba.co.kr"


def getJobs(company):
    request = requests.get(company["link"])
    soup = BeautifulSoup(request.text, "html.parser")
    jobTable = soup.find("div", {
        "id": "SubWrap"
    }).find("div", {
        "class": "goodsList"
    }).find("table")
    jobList = jobTable.find("tbody").find_all("tr")

    jobs = []
    if len(jobList) > 1:
        i = 1
        for job in jobList:
            if i % 2 == 1:
                place = job.find("td", {"class": "local"}).get_text()
                title = job.find("span", {"class": "company"}).string
                time = job.find("td", {"class": "data"}).find("span").string
                pay = job.find("span", {
                    "class": "payIcon"
                }).string + job.find("span", {
                    "class": "number"
                }).string
                date = job.find("td", {"class": "regDate"}).string
                if date.string == None:
                    date = date.find("strong").string
                # print(f"{place} / {title} / {time} / {pay} / {date}")
                jobs.append({
                    "place": place,
                    "title": title,
                    "time": time,
                    "pay": pay,
                    "date": date
                })
            i += 1

    return jobs


def getCompanyInfo(companyList):
    list = companyList.find("ul", {"class": "goodsBox"}).find_all("li")

    companyInfo = []
    for company in list:
        links = company.find_all("a", {"class": "brandHover"})
        for link in links:
            name = link.find("strong").string
            companyInfo.append({"name": name, "link": link["href"]})

    return companyInfo


def getRecruitInfo():
    request = requests.get(alba_url)
    soup = BeautifulSoup(request.text, "html.parser")
    companyList = soup.find("div", {"id": "MainSuperBrand"})

    companyInfo = getCompanyInfo(companyList)

    recruitInfo = []
    i = 1
    for company in companyInfo:
        print(f"Scrapping {company['name']}..({i}/{len(companyInfo)})")
        jobs = getJobs(company)
        recruitInfo.append({"name": company["name"], "jobs": jobs})
        i += 1

    return recruitInfo

