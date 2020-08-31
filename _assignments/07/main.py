import os
# import csv
# import requests
# from bs4 import BeautifulSoup
from alba import getRecruitInfo
from save import saveToFile


os.system("clear")

recruitInfo = getRecruitInfo()
print("Scrapping Done!")
saveToFile(recruitInfo)
print("Saving Done!")