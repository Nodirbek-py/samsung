from selenium import webdriver
from bs4 import BeautifulSoup
import json

chrome = "./chromedriver_win32/chromedriver.exe"
tv = {
    "status": "1",
    "categories": [
        {
            "title": "QLED 8K",
            "items": []
        },
        {
            "title": "Soundbars",
            "items": []
        }
    ]
}

driver_qled_8k = webdriver.Chrome(executable_path=chrome)
# QLED 8K
driver_qled_8k.get("https://www.samsung.com/uz_ru/tvs/all-tvs/?qled-8k")
html = driver_qled_8k.page_source
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
    qled_8k = {
        "id": id,
        "name": name,
        "image": image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][0]["items"].append(qled_8k) 


# Soundbars
driver_audio = driver_qled_8k
driver_audio.get("https://www.samsung.com/uz_ru/audio-video/soundbar/")
html = driver_audio.page_source
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

    print(size)
    audio = {
        "id": id,
        "name": name,
        "image": image,
        "color": str(','.join(color)),
    }
    tv["categories"][1]["items"].append(audio) 


with open('tv_audio.json', 'w', encoding='utf-8') as file:
   json.dump(tv, file, ensure_ascii=False, indent=4)

driver_audio.close() 