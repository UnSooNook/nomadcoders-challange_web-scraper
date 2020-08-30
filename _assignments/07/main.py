import os
# import requests
# from bs4 import BeautifulSoup
# from babel.numbers import format_currency

from country import getCountryInfo, printCountryInfo, getCountryIndex2
from currencyConverter import askAmount, currencyConvert

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

# print(format_currency(5000, "KRW", locale="ko_KR"))

print("Welcome to CurencyConvert PRO 2000\n")

countryInfo = getCountryInfo()
printCountryInfo(countryInfo)

A, B = getCountryIndex2(countryInfo)
A = countryInfo[A]
B = countryInfo[B]

amount = askAmount(A, B)
currencyConvert(A, B, amount)