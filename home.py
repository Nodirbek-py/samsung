from selenium import webdriver
from bs4 import BeautifulSoup
import json

chrome = "./chromedriver_win32/chromedriver.exe"
home = {
    "status": "1",
    "categories": [
        {
            "title": "Washing Machines",
            "items": []
        },
        {
            "title": "Refregirators",
            "items": []
        },
        {
            "title": "Vacuum Cleaner",
            "items": []
        },
        {
            "title": "SteamCase",
            "items": []
        },
        {
            "title": "Air Conditioner",
            "items": []
        }
    ]
}

driver_wash = webdriver.Chrome(executable_path=chrome)

# Washing machines

driver_wash.get("https://www.samsung.com/uz_ru/washing-machines/all-washing-machines/?slim")
html = driver_wash.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_wash.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_wash.page_source, "html.parser")
    volume = detail_info.find_all(class_="product-specs__spec-title")[0]["title"]
    size = detail_info.find_all(class_="product-specs__spec-title")[1]["title"]
    washing = {
        "id": id,
        "name": name,
        "image": image,
        "volume": volume,
        "size": size
    }
    home["categories"][0]["items"].append(washing)

# Refregirator
driver_ref = driver_wash
driver_ref.get("https://www.samsung.com/uz_ru/refrigerators/all-refrigerators/?tmf")
html = driver_ref.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_ref.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_ref.page_source, "html.parser")
    volume = detail_info.find_all(class_="product-specs__spec-title")[0]["title"]
    height = detail_info.find_all(class_="product-specs__spec-title")[2]["title"]
    refregirator = {
        "id": id,
        "name": name,
        "image": image,
        "useful volume": volume.replace('\\xa0', ""),
        "height": height.replace("\\xa0", "")
    }
    home["categories"][1]["items"].append(refregirator)

# Vacuum Cleaner
driver_vac = driver_ref
driver_vac.get("https://www.samsung.com/uz_ru/vacuum-cleaners/all-vacuum-cleaners/?bagless")
html = driver_vac.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_vac.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_vac.page_source, "html.parser")
    power_of_suction = detail_info.find_all("span", class_="product-specs__highlights-desc")[4].text

    vacuum_cleaner = {
        "id": id,
        "name": name,
        "image": image,
        "power of suction": power_of_suction
    }
    home["categories"][2]["items"].append(vacuum_cleaner) 


# SteamCase
driver_steam = driver_vac
driver_steam.get("https://www.samsung.com/uz_ru/washing-machines/dryer-df60r8600cg/")
html = driver_steam.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
id = 0
name = soup.find(class_="product-details__title").text
image = "https://images.samsung.com/is/image/samsung/uz-ru-dryer-df60r8600cg-df60r8600cg-lp-frontaurablue-246913966?$PD_GALLERY_L_JPG$"
characteristics = soup.findAll(class_="product-summary__card no-border")
character = []
for i in characteristics:
    character.append(i.text)
character = ','.join(character)

steam_case = {
    "id": id,
    "name": name,
    "image": image,
    "character": character
}
home["categories"][3]["items"].append(steam_case) 




# Air conditioner
driver_air = driver_steam
driver_air.get("https://www.samsung.com/uz_ru/air-conditioners/all-air-conditioners/")
html = driver_air.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_air.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_air.page_source, "html.parser")
    energy_efficency = detail_info.find("ul", class_="product-specs__highlights-list").find_all("li")[9]
    energy_efficency = energy_efficency.find_all("span")
    energy = []
    for i in energy_efficency:
        energy.append(i.text)

    if len(energy) < 3:
        air_conditioner = {
            "id": id,
            "name": name,
            "image": image,
            "energy efficiency grade": "C"
        }
        home["categories"][4]["items"].append(air_conditioner) 
    else:
        air_conditioner = {
            "id": id,
            "name": name,
            "image": image,
            "energy efficiency grade": energy[4]
        }
        home["categories"][4]["items"].append(air_conditioner)


with open('home.json', 'w', encoding='utf-8') as file:
   json.dump(home, file, ensure_ascii=False, indent=4)

driver_air.close()
