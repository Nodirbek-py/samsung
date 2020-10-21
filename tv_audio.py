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
            "title": "QLED 4K",
            "items": []
        },
        {
            "title": "Crystal UHD",
            "items": []
        },
        {
            "title": "Premium UHD",
            "items": []
        },
        {
            "title": "UHD",
            "items": []
        },
        {
            "title": "HD/FHD",
            "items": []
        },
        {
            "title": "The Serif",
            "items": []
        },
        {
            "title": "The Frame",
            "items": []
        },
        {
            "title": "Interior",
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
        "image": "https:" + image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][0]["items"].append(qled_8k) 

# QLED 4K
driver_4k = driver_qled_8k
driver_4k.get("https://www.samsung.com/uz_ru/tvs/all-tvs/?qled-4k")
html = driver_4k.page_source
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
    qled_4k = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][1]["items"].append(qled_4k)


# Crystall UHD
driver_crystal = driver_4k
driver_crystal.get("https://www.samsung.com/uz_ru/tvs/all-tvs/?crystal-uhd")
html = driver_crystal.page_source
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
    crystal = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][2]["items"].append(crystal)

# Premium UHD
driver_premium = driver_crystal
driver_premium.get("https://www.samsung.com/uz_ru/tvs/all-tvs/?premium-uhd")
html = driver_premium.page_source
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
    premium = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][3]["items"].append(premium)
# UHD
driver_uhd = driver_premium
driver_uhd.get("https://www.samsung.com/uz_ru/tvs/all-tvs/?uhd")
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
    print(size)
    uhd = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][4]["items"].append(uhd)
# HD/FHD
driver_hd = driver_uhd
driver_hd.get("https://www.samsung.com/uz_ru/tvs/all-tvs/?hdfull-hd")
html = driver_hd.page_source
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
    hd = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][5]["items"].append(hd)

# The Serif
driver_serif = driver_hd
driver_serif.get("https://www.samsung.com/uz_ru/tvs/all-tvs/?the-serif")
html = driver_serif.page_source
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
    serif = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][6]["items"].append(serif)
# The Frame
driver_frame = driver_serif
driver_frame.get("https://www.samsung.com/uz_ru/tvs/all-tvs/?the-frame")
html = driver_frame.page_source
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
    frame = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][7]["items"].append(frame)
# Interior TV
driver_interior = driver_frame
driver_interior.get("https://www.samsung.com/uz_ru/tvs/all-tvs/?interior-tv")
html = driver_interior.page_source
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
    interior = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "size": size.replace("\\u200e", "")
    }
    tv["categories"][8]["items"].append(interior) 




# Soundbars
driver_audio = driver_interior
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
        "image": "https:" + image,
        "color": str(','.join(color)),
    } 
    tv["categories"][9]["items"].append(audio) 


with open('tv_audio.json', 'w', encoding='utf-8') as file:
   json.dump(tv, file, ensure_ascii=False, indent=4)

driver_audio.close() 