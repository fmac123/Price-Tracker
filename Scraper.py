import requests
import smtplib
import time
from bs4 import BeautifulSoup


URL = 'https://www.amazon.com.au/Avatar-Airbender-Legend-Complete-Collection/dp/B07J4MV6GC'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}

def check_price():

    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    #print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])

    print(title.strip())
    print(converted_price)

    if(converted_price > 80):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #gmail app login (get password from gmail)
    server.login('macaulay.fraser@gmail.com','')

    subject="HEY THE PRICE WENT DOWN!!!!!!!"
    body="Check the amazon link: https://www.amazon.com.au/Avatar-Airbender-Legend-Complete-Collection/dp/B07J4MV6GC"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'macaulay.fraser@gmail.com',
        'macaulay.fraser@gmail.com',
        msg
    )

    print("EMAIL HAS BEEN SENT")

    server.quit()

while(True):
    check_price()
    time.sleep(60)


