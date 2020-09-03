import requests
from bs4 import BeautifulSoup


def getPosts(subreddit):
    # url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
    url = "https://www.reddit.com/r/javascript/top/?t=month"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    body = soup.find("body")



    feed = soup.find("div", {"id":"2x-container"})
    feed2 = feed.find("div", {"class":"_1vyLCp-v-tE5QvZovwrASa"})
    feed3 = soup.find_all("div", {"class":"scrollerItem"})
    print(body)
    # feed = soup.find_all("div", {"class":"_1OVBBWLtHoSPfGCRaPzpTf"})
    # posts = feed.find("div", {"class":"_Post"})

getPosts("javascript")