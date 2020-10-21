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
        },
        {
            "title": "Curved Monitors",
            "items": []
        },
        {
            "title": "TV Monitors",
            "items": []
        },
        {
            "title": "Led Monitors",
            "items": []
        },
        {
            "title": "Professional Monitors",
            "items": []
        },
        {
            "title": "Gamer Monitors",
            "items": []
        }
    ]
}

driver_uhd = webdriver.Chrome(executable_path=chrome)
# UHD Monitors
driver_uhd.get("https://www.samsung.com/uz_ru/monitors/all-monitors/?uhd")
html = driver_uhd.page_source
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
    
    monitor_uhd = {
        "id": id,
        "name": name,
        "image":"https:" + image,
        "size": size.replace("\\u200e", "")
    }
    monitors["categories"][0]["items"].append(monitor_uhd) 
# Curved monitors
driver_curved = driver_uhd
driver_curved.get("https://www.samsung.com/uz_ru/monitors/all-monitors/?curved")
html = driver_curved.page_source
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
    
    monitor_curved = {
        "id": id,
        "name": name,
        "image":"https:" + image,
        "size": size.replace("\\u200e", "")
    }
    monitors["categories"][1]["items"].append(monitor_curved) 

# TV Monitors
driver_tv = driver_curved
driver_tv.get("https://www.samsung.com/uz_ru/monitors/all-monitors/?tv")
html = driver_tv.page_source
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
    
    monitor_tv = {
        "id": id,
        "name": name,
        "image":"https:" + image,
        "size": size.replace("\\u200e", "")
    }
    monitors["categories"][2]["items"].append(monitor_tv)

# LED monitors
driver_led = driver_tv
driver_led.get("https://www.samsung.com/uz_ru/monitors/all-monitors/?led")
html = driver_led.page_source
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
    
    monitor_led = {
        "id": id,
        "name": name,
        "image":"https:" + image,
        "size": size.replace("\\u200e", "")
    }
    monitors["categories"][3]["items"].append(monitor_led)
# Professional Monitors
driver_pro = driver_led
driver_pro.get("https://www.samsung.com/uz_ru/monitors/all-monitors/?professional")
html = driver_pro.page_source
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
    
    monitor_pro = {
        "id": id,
        "name": name,
        "image":"https:" + image,
        "size": size.replace("\\u200e", "")
    }
    monitors["categories"][4]["items"].append(monitor_pro)

# Gaming Monitors
driver_gaming = driver_pro
driver_gaming.get("https://www.samsung.com/uz_ru/monitors/all-monitors/?gaming")
html = driver_gaming.page_source
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
    
    monitor_gaming = {
        "id": id,
        "name": name,
        "image":"https:" + image,
        "size": size.replace("\\u200e", "")
    }
    monitors["categories"][5]["items"].append(monitor_gaming)


with open('it.json', 'w', encoding='utf-8') as file:
   json.dump(monitors, file, ensure_ascii=False, indent=4)

driver_gaming.close()