import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

def getNumber(maxValue):
  isNum = False
  num = -1
  while isNum is False:
    num = input("#: ")
    if num.isdecimal():
      num = int(num)
      if num > 0 and num <= maxValue:
        num -= 1
        isNum = True
      else:
        print("Choose a number from the list.")
    else:
      print("That wasn't a number.")
  
  return num


def getCountryIndex2(countryInfo):
  maxNum = len(countryInfo)
  print("\nWhere are you from? Choose a country by number.\n")

  A = getNumber(maxNum)
  print(countryInfo[A]["name"])

  print("\nNow choose another country.\n")

  B = getNumber(maxNum)
  print(countryInfo[B]["name"])

  return A, B


def printCountryInfo(countryInfo):
  i = 1
  for country in countryInfo:
    print(f"# {i} {country['name']}")
    i += 1


def getCountryInfo():
  countryInfo = []
  request = requests.get(url)
  soup = BeautifulSoup(request.text, "html.parser")
  countryTable = soup.find("table", {"class": "table"}).find("tbody")
  countryList = countryTable.find_all("tr")

  for country in countryList:
    name, currency, code, number = country.find_all("td")
    name = name.string
    currency = currency.string
    code = code.string
    number = number.string
    info = {
      "name": name,
      "currency": currency,
      "code": code,
      "number": number
    }
    countryInfo.append(info)
  
  return countryInfo

