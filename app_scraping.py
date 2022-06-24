import requests
from bs4 import BeautifulSoup
from time import sleep
headers = {"User-Agent":
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"}
list_card_url = [

]

for count in range(1, 8):
    sleep(1)

    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    responce = requests.get(url)

    soup = BeautifulSoup(responce.text, "html.parser")

    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

    for i in data:
        card_url = "https://scrapingclub.com/" + i.find("a").get("href")
        list_card_url.append(card_url)

for card_url in list_card_url:
    responce = requests.get(card_url, headers=headers)

    soup = BeautifulSoup(responce.text, "html.parser")

    data = soup.find("div", class_="card mt-4 my-4")







