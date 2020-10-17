from selenium import webdriver
from bs4 import BeautifulSoup
import json

chrome = "./chromedriver_win32/chromedriver.exe"
monitors = {
    "status": "1",
    "categories": [
        {
            "title": "UHD Monitors",
            "items": []
        }
    ]
}

driver_monitor = webdriver.Chrome(executable_path=chrome)
# UHD Monitors
driver_monitor.get("https://www.samsung.com/uz_ru/monitors/uhd-monitor/")
html = driver_monitor.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    size = detail.findAll(class_="product-card__img-ctrl-item")
    available_size = []
    for i in size:
        if i.text.isalpha() is False:
            available_size.append(i.text.replace("selected", ""))
    size = str(', '.join(available_size).replace("\\u200e", ""))
    print(size)
    monitor = {
        "id": id,
        "name": name,
        "image": image,
        "size": size.replace("\\u200e", "")
    }
    monitors["categories"][0]["items"].append(monitor) 

with open('it.json', 'w', encoding='utf-8') as file:
   json.dump(monitors, file, ensure_ascii=False, indent=4)

driver_monitor.close()