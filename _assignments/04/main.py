import os
import requests

def askStartOver():
  answer = input("Do you want to start over? y/n ")
  if answer == "y"  or answer == "Y":
    return True
  elif answer == "n" or answer == "N":
    print("k. bye!")
    return False
  else:
    print("That's not a valid answer")
    return askStartOver()


def isItDown(urls):
  for url in urls:
    if url.find(".") is -1:
      print(f"{url} is not a valid URL")
      continue

    if url.startswith("http://") is False and url.startswith("https://") is False:
      url = "http://" + url
    try:
      r = requests.get(url)
      r.raise_for_status()
      print(f"{url} is up!")
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
      print(f"{url} is down!")


def parseInput(inputs):
  inputs = inputs.split(",")
  urls = []
  for url in inputs:
    urls.append(url.strip())
  return urls


def getInput():
  inputs = input()
  urls = parseInput(inputs)
  return urls


def printStart():
  os.system("clear")
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (seperated by comma)")


startOver = True
urlInput = ""

while startOver:
  printStart()
  urlInput = getInput()
  isItDown(urlInput)
  startOver = askStartOver()