import requests

def getFeed(url):
    feed = []
    data = requests.get(url).json()
    newsFeed = data.get("hits")
    
    for news in newsFeed:
        title = news.get("title")
        id = news.get("objectID")
        url = news.get("url")
        points = news.get("points")
        author = news.get("author")
        num_comments = news.get("num_comments")

        feed.append({"title":title, "id":id, "url":url, "points":points, "author":author, "num_comments":num_comments})
    
    return feed


def getComments(url):
    comments = []
    news = requests.get(url).json()

    title = news.get("title")
    points = news.get("points")
    author = news.get("author")
    url = news.get("url")

    info = {"title":title, "points":points, "author":author, "url":url}

    data = news.get("children")

    for comment in data:
        author = comment.get("author")
        text = comment.get("text")
        comments.append({"author":author, "text":text})

    return info, comments

