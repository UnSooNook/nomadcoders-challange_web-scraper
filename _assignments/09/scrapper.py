import requests
from bs4 import BeautifulSoup


def getPosts(subreddit, headers):
    posts = []
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    feed = soup.find_all("div", {"class": "Post"})

    for post in feed:
        ad = post.find("span", {"class": "_2oEYZXchPfHwcf9mTMGMg8"})
        if ad:
            continue

        title = post.find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"}).string

        upvote = post.find("div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"}).string
        if "k" in upvote:
            upvote = (float)(upvote.replace("k", ""))
            upvote = (int)(upvote * 1000)
        else:
            upvote = (int)(upvote)
        
        link = "https://www.reddit.com" + post.find("div", {"class":"y8HYJ-y_lTUHkQIc1mdCq"}).find("a")["href"]
        
        posts.append({"subreddit":subreddit,,"title":title, "upvote":upvote, "link":link})

    return posts

