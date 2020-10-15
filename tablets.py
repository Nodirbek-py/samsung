from selenium import webdriver
from bs4 import BeautifulSoup
import json

chrome = "./chromedriver_win32/chromedriver.exe"
tablet = {
    "status": "1",
    "categories": [
        {
            "title": "Galaxy Tab S",
            "items": []
        },
        {
            "title": "Galaxy Tab A",
            "items": []
        },
        {
            "title": "Galaxy Tab E",
            "items": []
        }
    ]
}

driver_s = webdriver.Chrome(executable_path=chrome)
# Tab S
driver_s.get("https://www.samsung.com/uz_ru/tablets/galaxy-tab-s/")
html = driver_s.page_source
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
    
    capacity = detail.findAll(class_="product-card__img-ctrl-item")
    available_capacity = []
    for i in capacity:
        if i.text.isalpha() is False:
            available_capacity.append(i.text.replace("selected", ""))
    galaxy_tab_s = {
        "id": id,
        "name": name,
        "image": image,
        "color": str(','.join(color)),
        "capacity": str(''.join(available_capacity).replace("\\u200e", ""))
    }
    tablet["categories"][0]["items"].append(galaxy_tab_s)  

# Tab A
driver_a = driver_s
driver_a.get("https://www.samsung.com/uz_ru/tablets/galaxy-tab-a/")
html = driver_a.page_source
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
    
    capacity = detail.findAll(class_="product-card__img-ctrl-item")
    available_capacity = []
    for i in capacity:
        if i.text.isalpha() is False:
            available_capacity.append(i.text.replace("selected", ""))
    galaxy_tab_a = {
        "id": id,
        "name": name,
        "image": image,
        "color": str(','.join(color)),
        "capacity": str(''.join(available_capacity).replace("\\u200e", ""))
    }
    tablet["categories"][1]["items"].append(galaxy_tab_a) 



# Tab E
driver_e = driver_a
driver_e.get("https://www.samsung.com/uz_ru/tablets/galaxy-tab-e/")
html = driver_e.page_source
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
    
    capacity = detail.findAll(class_="product-card__img-ctrl-item")
    available_capacity = []
    for i in capacity:
        if i.text.isalpha() is False:
            available_capacity.append(i.text.replace("selected", ""))
    galaxy_tab_e = {
        "id": id,
        "name": name,
        "image": image,
        "color": str(','.join(color)),
        "capacity": str(''.join(available_capacity).replace("\\u200e", ""))
    }
    tablet["categories"][2]["items"].append(galaxy_tab_e) 

with open('tablet.json', 'w', encoding='utf-8') as file:
   json.dump(tablet, file, ensure_ascii=False, indent=4)

driver_e.close()