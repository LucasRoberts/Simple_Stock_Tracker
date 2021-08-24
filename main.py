import requests
from bs4 import BeautifulSoup
from xlwt import Workbook

# AMD's URL link on Yahoo finance
url = "https://finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-srch"

# using requests retrieves urls html docs
r = requests.get(url)

# converts html doc from string into bs4 usable text
html = r.content
soup = BeautifulSoup(html, "lxml")

# Grabs the title of the page, for this it will include the stocks name and ticker
# print(soup.title)

# Sets soup_body to the html body
soup_body = soup.body.div.div.div.div

# There must be an easier way to do this but this is what I have currently
current_stock_price = soup_body.find("div", class_="YDC-Lead").div.div.find("div", id="quote-header-info").find("div", class_="My(6px) Pos(r) smartphone_Mt(6px)").div.div.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
print(f" AMD is currently at: ${current_stock_price}")

# Creates a workbook
wb = Workbook()

# Creates workbook sheet
sheet1 = wb.add_sheet("Stock Data")
sheet1.write(0, 0, "")
sheet1.write(0, 1, "Stock")
sheet1.write(0, 2, "Date")

wb.save("Stock Tracker.xls")

# TODO Send current stock price to excel sheet w/h time stamp
# TODO Update current stock price every x period of time
# TODO Add the option to change the stock with user input
# TODO Modularize code
# TODO Find a better way to access the current stock price
# TODO Create line graph tracking stock price
