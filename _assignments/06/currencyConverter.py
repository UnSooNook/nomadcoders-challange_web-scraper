import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

url = "https://transferwise.com/gb/currency-converter"
# "https://transferwise.com/gb/currency-converter/eur-to-cad-rate?amount=50.2"

def currencyConvert(countryA, countryB, sourceAmount):

  request = requests.get(f"{url}/{countryA['code']}-to-{countryB['code']}-rate?amount={sourceAmount}")
  if request.status_code != 200:
    print("Wrong Currency...(Currency Not Found")
    return
  
  soup = BeautifulSoup(request.text, "html.parser")

  rate = float(soup.find("input", {"class" : "js-Rate"})["value"])
  targetAmount = rate * sourceAmount

  source = format_currency(sourceAmount, countryA["code"], locale="ko_KR")
  target = format_currency(targetAmount, countryB["code"], locale="ko_KR")
  print(f"\n{source} is {target}")


def getAmount():
  isNum = False
  num = -1
  while isNum is False:
    num = input()
    try:
      num = float(num)
      if num > 0:
        isNum = True
      else:
        print("Choose a positive number")
    except:
      print("That wasn't a number.")
  
  return num


def askAmount(countryA, countryB):
  print(f"\nHow many {countryA['code']} do you want to convert to {countryB['code']}?")
  
  amount = getAmount()

  return amount

