from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


url = 'https://www.webull.com/quote/us/gainers/1d'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
title = soup.title
print(title)		


stock_data = soup.findAll("div", attrs={"class":"table-cell"})
print(stock_data[1].text)
print(stock_data[12].text)

counter = 1
for x in range(5):
    name = stock_data[counter].text
    change = float(stock_data[counter + 2].text.strip("%").strip("+"))
    last_price = float(stock_data[counter + 3].text)

    previous_price = round(last_price / (1 + change/100), 2)

    print(f"Company Name: {name}")
    print(f"Change {change}")
    print(f"Price {last_price}")
    print(f"Previous price: {previous_price}")

    counter += 11
