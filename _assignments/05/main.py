import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"
countryInfo = []

def finalPrint(n):
  country = countryInfo[n]
  print(f"You choose {country['name']}")
  print(f"The currency code is {country['code']}")


def getNumber():
  isNum = False
  num = -1
  while isNum is False:
    num = input("#: ")
    if num.isdecimal():
      num = int(num)
      if num > 0 and num < (len(countryInfo) + 1):
        num -= 1
        isNum = True
      else:
        print("Choose a number from the list.")
    else:
      print("That wasn't a number.")
  return num


def printCountry():
  request = requests.get(url)
  soup = BeautifulSoup(request.text, "html.parser")
  countryTable = soup.find("table", {"class":"table"}).find("tbody")
  countryList = countryTable.find_all("tr")
  i = 1
  for country in countryList:
    name, currency, code, number = country.find_all("td")
    name = name.string
    currency = currency.string
    code = code.string
    number = number.string
    info = {"name":name, "currency":currency, "code": code, "number":number}
    countryInfo.append(info)
    print(f"# {i} {info['name']}")
    i+=1


def initPrint():
  print("Hello! Please choose select a country by number:")
  printCountry()


initPrint()
selected = getNumber()
finalPrint(selected)