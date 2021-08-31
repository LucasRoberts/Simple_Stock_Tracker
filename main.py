import requests
from bs4 import BeautifulSoup
import datetime as dt
from datetime import date
import time

ticker = input("Please enter the ticker symbol of the stock you would like to see: ").upper()
interval = input("How often do you want to retrieve the stock price (in minutes): ")
try:
    interval = int(interval)
    if interval <= 0:
        interval = (interval * -1) * 60
    else:
        interval = interval * 60
except ValueError:
    interval = 600

url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch"

# One major reason the price hasn't been updating was because the website was checking the user-agent
# Now that it thinks it's a browser it will return updated prices
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/72.0. 3626.121 Safari/537.36."}

current_date = date.today()
market_close = dt.datetime(year=current_date.year, month=current_date.month, day=current_date.day, hour=16, minute=0)
current_time = dt.datetime.now()
market_hours = ""
if current_time < market_close:
    market_hours = True
else:
    market_hours = False

while market_hours:
    r = requests.get(url, headers=headers)

    html = r.text
    soup = BeautifulSoup(html, "lxml")

    # Again, there has to be an easier way I simply have not found that way yet. Edit: Found
    # I originally tried using "find" this way but I typed instead of copying the class... at least I know now
    current_stock_price = soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    print(f"{ticker} is currently at: ${current_stock_price}")

    # Creating and reading a data.txt file to store the stocks past prices
    with open("data.txt", "r") as f:
        count = int(f.readline().strip("counter:")) + 1
        data = f.readlines()
        f.close()

    with open("data.txt", "w") as f:
        f.write(f"counter:{count}\n")
        f.close()

    with open("data.txt", "a") as f:
        for line in range(len(data)):
            f.write(data[line])
        f.write(f"Time:{current_time}\nStock:{ticker},Price:{current_stock_price}\n")
        f.close()
    time.sleep(interval)
    current_time = dt.datetime.now()
    if current_time < market_close:
        market_hours = True
    else:
        market_hours = False

# TODO Modularize code
# TODO Find a better way to access the current stock price
# TODO Create line graph tracking stock price
