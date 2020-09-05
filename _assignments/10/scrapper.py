import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def getSOLastPage(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "s-pagination"})
    page = pagination.find_all("a")[-2]

    maxPage = int(page.get_text(strip=True))

    return maxPage


def getSOJobs(url):
    jobs = []
    lastPage = getSOLastPage(url)

    for page in range(lastPage):
        print(f"Scrapping Stackoverflow page {page+1}/{lastPage}..")

        result = requests.get(f"{url}&pg={page+1}", headers=headers)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})

        for job in results:
            isFeatured = job.find("span", {"class":"bar-sm"})
            if isFeatured:
                continue
            
            info = job.find("a", {"class":"s-link"})
            title = info["title"]
            company = job.find("h3", {"class":"mb4"}).find_all("span")[0].get_text(strip=True)
            link = "https://stackoverflow.com" + info["href"]
            
            jobs.append({"title":title, "company":company, "link":link})

    return jobs


def getWWRJobs(url):
    jobs = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    ul = soup.find("section", {"class":"jobs"}).find("ul").find_all("li")

    print(f"Scrapping WeWorkRemotely..")
    for li in ul[:-1]:
        info = li.find_all("a", recursive=False)[-1]
        
        title = info.find("span", {"class":"title"}).string
        company = info.find("span", {"class":"company"}).string
        link = "https://weworkremotely.com" + info["href"]

        jobs.append({"title":title, "company":company, "link":link})

    return jobs


def getROKJobs(url):
    jobs = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    td = soup.find_all("td", {"class":"company position company_and_position"})

    print(f"Scrapping RemoteOK..")
    for job in td[1:]:
        title = job.find("h2", {"itemprop":"title"}).string
        company = job.find("a", {"class":"companyLink"}).find("h3").string
        link = "https://remoteok.io" + job.find("a", {"class":"preventLink"})["href"]

        jobs.append({"title":title, "company":company, "link":link})
        
    return jobs


def getJobs(term):
    jobs = []

    soURL = f"https://stackoverflow.com/jobs?r=true&q={term}"
    wwrURL = f"https://weworkremotely.com/remote-jobs/search?term={term}"
    rokURL = f"https://remoteok.io/remote-dev+{term}-jobs"

    jobs = getSOJobs(soURL)
    jobs += getWWRJobs(wwrURL)
    jobs += getROKJobs(rokURL)

    return jobs

