import requests
from bs4 import BeautifulSoup
from xlwt import Workbook
import datetime as dt

# Grabs user inputted stock ticker
ticker = input("Please enter the ticker symbol of the stock you would like to see: ").upper()

# AMD's URL link on Yahoo finance
url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch"
print(url)

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
print(f"{ticker} is currently at: ${current_stock_price}")

# Creates a workbook
wb = Workbook()

# Creates workbook sheet
sheet1 = wb.add_sheet("Stock Data")
sheet1.write(0, 0, "")
sheet1.write(0, 1, "Stock")
sheet1.write(0, 2, "Date")

# Checking to see if the time is during open market hours
current_time = dt.datetime.now()

# Market opens at 9:30
# Open hour
hour_open = 9
# Open minute
minute_open = 30
# Market closes at 4:30
# Close Hour 4
hour_close = 4
# Close minute
minute_close = 30

if current_time.hour >= hour_open and current_time.minute >= minute_open and current_time.hour <= hour_close and current_time.minute <= minute_close:
    print("hello")


# Adding the stock price and time to excel sheet


wb.save("Stock Tracker.xls")

# TODO Send current stock price to excel sheet w/h time stamp
# TODO Update current stock price every x period of time
# TODO Add the option to change the stock with user input
# TODO Modularize code
# TODO Find a better way to access the current stock price
# TODO Create line graph tracking stock price
