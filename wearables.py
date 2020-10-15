from selenium import webdriver
from bs4 import BeautifulSoup
import json

chrome = "./chromedriver_win32/chromedriver.exe"
wearable = {
    "status": "1",
    "categories": [
        {
            "title": "Galaxy Buds",
            "items": []
        },
        {
            "title": "Galaxy Fit",
            "items": []
        },
        {
            "title": "Galaxy Watch",
            "items": []
        }
    ]
}

driver_buds = webdriver.Chrome(executable_path=chrome)
# Galaxy Buds
driver_buds.get("https://www.samsung.com/uz_ru/wearables/all-wearables/?headphones")
html = driver_buds.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    colors = detail.find(class_ = "product-card__img-ctrl-wrap")
    color = []
    for i in colors:
        for x in i.findAll("span"):
            color.append(x.text)
    
    galaxy_buds = {
        "id": id,
        "name": name,
        "image": image,
        "color": str(','.join(color))
    }
    wearable["categories"][0]["items"].append(galaxy_buds)  


# Galaxy Fit
driver_fit = driver_buds
driver_fit.get("https://www.samsung.com/uz_ru/wearables/all-wearables/?fitness")
html = driver_fit.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    colors = detail.find(class_ = "product-card__img-ctrl-wrap")
    color = []
    for i in colors:
        for x in i.findAll("span"):
            color.append(x.text)
    
    galaxy_fit = {
        "id": id,
        "name": name,
        "image": image,
        "color": str(','.join(color))
    }
    wearable["categories"][1]["items"].append(galaxy_fit) 


# Galaxy Watch
driver_watch = driver_fit
driver_watch.get("https://www.samsung.com/uz_ru/wearables/all-wearables/?galaxy-watch")
html = driver_watch.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    colors = detail.find(class_ = "product-card__img-ctrl-wrap")
    color = []
    for i in colors:
        for x in i.findAll("span"):
            color.append(x.text)
    
    galaxy_watch = {
        "id": id,
        "name": name,
        "image": image,
        "color": str(','.join(color))
    }
    wearable["categories"][2]["items"].append(galaxy_watch) 

with open('wearable.json', 'w', encoding='utf-8') as file:
   json.dump(wearable, file, ensure_ascii=False, indent=4)

driver_watch.close() 