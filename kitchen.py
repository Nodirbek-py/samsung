from selenium import webdriver
from bs4 import BeautifulSoup
import json

chrome = "./chromedriver_win32/chromedriver.exe"
kitchen = {
    "status": "1",
    "categories": [
        {
            "title": "Ovens",
            "items": []
        },
        {
            "title": "Cooktops",
            "items": []
        },
        {
            "title": "Microwave ovens",
            "items": []
        },
        {
            "title": "Dishwashers",
            "items": []
        },
        {
            "title": "Hoods",
            "items": []
        }
    ]
}

driver_oven = webdriver.Chrome(executable_path=chrome)
# Oven
driver_oven.get("https://www.samsung.com/uz_ru/cooking-appliances/all-cooking-appliances/?oven")
html = driver_oven.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    oven = {
        "id": id,
        "name": name,
        "image": image,
    }
    kitchen["categories"][0]["items"].append(oven)

# Cooktops 
driver_cook = driver_oven
driver_cook.get("https://www.samsung.com/uz_ru/cooking-appliances/all-cooking-appliances/?cooktops")
html = driver_cook.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    cooktops = {
        "id": id,
        "name": name,
        "image": image,
    }
    kitchen["categories"][1]["items"].append(cooktops)

# Microwave oven
driver_mic = driver_cook
driver_mic.get("https://www.samsung.com/uz_ru/cooking-appliances/all-cooking-appliances/?microwave-ovens")
html = driver_mic.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    microwave = {
        "id": id,
        "name": name,
        "image": image,
    }
    kitchen["categories"][2]["items"].append(microwave)


# Dishwashers
driver_dish = driver_mic
driver_dish.get("https://www.samsung.com/uz_ru/cooking-appliances/all-cooking-appliances/?dishwashers")
html = driver_dish.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    dishwasher = {
        "id": id,
        "name": name,
        "image": image,
    }
    kitchen["categories"][3]["items"].append(dishwasher)

# Hood

driver_hood = driver_dish
driver_hood.get("https://www.samsung.com/uz_ru/cooking-appliances/all-cooking-appliances/?hoods")
html = driver_hood.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    hoods = {
        "id": id,
        "name": name,
        "image": image,
    }
    kitchen["categories"][4]["items"].append(hoods)

with open('kitchen.json', 'w', encoding='utf-8') as file:
    json.dump(kitchen, file, ensure_ascii=False, indent=4)
print(kitchen)