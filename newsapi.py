import requests
from bs4 import BeautifulSoup
# print("Which type of news do you want to see\n 1.Medical 3.Political\n 2.Financial 4.Sports ")

# interest = int(input("Enter the number whose type of news you want to see: "))

# if interest == 2:
#     financial = requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=39920781504f49b5b97ef4d2ec9afb7b")
#     print(financial.text)

# elif interest == 1:
medical = requests.get("https://newsapi.org/v2/everything?q=Apple&from=2023-10-26&sortBy=popularity&apiKey=39920781504f49b5b97ef4d2ec9afb7b")
print(medical.text)
print(medical.json)