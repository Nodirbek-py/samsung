from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time

chrome = "./chromedriver_win32/chromedriver.exe"
home = {
    "status": "1",
    "categories": [
        {
            "title": "Washing Machines Slim",
            "items": []
        },
        {
            "title": "Washing Machines Non-Slim",
            "items": []
        },
        {
            "title": "Refregirators Up",
            "items": []
        },
        {
            "title": "Refregirators Down",
            "items": []
        },
        {
            "title": "Refregirators SBS",
            "items": []
        },
        {
            "title": "Vacuum Cleaner With-Bag",
            "items": []
        },
        {
            "title": "Vacuum Cleaner No-Bag",
            "items": []
        },
        {
            "title": "Vacuum Cleaner Wet-Dry",
            "items": []
        },
        {
            "title": "Vacuum Cleaner Vertical",
            "items": []
        },
        {
            "title": "Vacuum Cleaner Robot",
            "items": []
        },
        {
            "title": "Vacuum Cleaner Wireless",
            "items": []
        },
        {
            "title": "SteamCase",
            "items": []
        },
        {
            "title": "Air Conditioner Wall-Mount",
            "items": []
        },
        {
            "title": "Air Conditioner Standing",
            "items": []
        }
    ]
}

driver_wash = webdriver.Chrome(executable_path=chrome)

# Washing machines Slim

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
    if id == 0 or id == 1 or id == 2 or id == 6 or id == 7:
        size = detail_info.find_all(class_="product-specs__spec-title")[1]["title"]
    elif id == 4 or id == 5:
        size = detail_info.find_all(class_="product-specs__spec-title")[3]["title"]
    else:
        size = detail_info.find_all(class_="product-specs__spec-title")[4]["title"]
    washing = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "volume": volume,
        "size": size
    }
    home["categories"][0]["items"].append(washing)

# Washing machines Non-Slim
driver_wash_non = driver_wash
driver_wash_non.get("https://www.samsung.com/uz_ru/washing-machines/all-washing-machines/?non-slim")
html = driver_wash_non.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_wash_non.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_wash_non.page_source, "html.parser")
    volume = detail_info.find_all(class_="product-specs__spec-title")[0]["title"]
    size = detail_info.find_all(class_="product-specs__spec-title")[2]["title"]
    washing_non = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "volume": volume,
        "size": size
    }
    home["categories"][1]["items"].append(washing_non)




# Refregirator
driver_ref = driver_wash_non
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
    time.sleep(3)
    volume = detail_info.find_all(class_="product-specs__spec-title")[0]["title"]
    if id == 0 or id == 5 or id == 8:
        height = detail_info.find_all(class_="product-specs__spec-title")[3]["title"]
    elif id == 1 or id == 2 or id == 3 or id == 4 or id == 6 or id == 7:
        height = detail_info.find_all(class_="product-specs__spec-title")[2]["title"]
        height = height.split("x")
        height = height[1] + "мм"
    elif id == 9:
        height = detail_info.find_all(class_="product-specs__spec-title")[2]["title"]
    elif id == 10 or id == 11:
        height = detail_info.find_all(class_="product-specs__spec-title")[5]["title"]

    if height[-1:] != "мм":
        height += " мм" 
    refregirator = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "useful": volume.replace('\\xa0', ""),
        "height": height.replace("\\xa0", "")
    }
    home["categories"][2]["items"].append(refregirator)
# Refregirator Down
driver_ref_down = driver_ref
driver_ref_down.get("https://www.samsung.com/uz_ru/refrigerators/all-refrigerators/?bmf")
html = driver_ref_down.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_ref_down.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_ref_down.page_source, "html.parser")
    time.sleep(3)

    if id == 0 or id == 1:
        height = detail_info.find_all(class_="product-specs__spec-title")[2]["title"]
        volume = detail_info.find_all(class_="product-specs__spec-title")[0]["title"]
    elif id == 2 or id == 3 or id == 4:
        volume = detail_info.find_all(class_="product-specs__spec-title")[5]["title"]
        height = "2010 мм"
    elif id == 5:
        volume = detail_info.find_all(class_="product-specs__spec-title")[1]["title"]
        height = detail_info.find_all(class_="product-specs__spec-title")[3]["title"]
    elif id == 6:
        height = detail_info.find_all(class_="product-specs__spec-title")[1]["title"]
        volume = detail_info.find_all(class_="product-specs__spec-title")[5]["title"]
    elif id == 7:
        height = "1850 мм"
        volume = "435 л"

    if height[-1:] != "мм":
        height += " мм" 
    refregirator_down = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "useful": volume.replace('\\xa0', ""),
        "height": height.replace("\\xa0", "")
    }
    home["categories"][3]["items"].append(refregirator_down)

# Refregirators SBS
driver_ref_sbs = driver_ref_down
driver_ref_sbs.get("https://www.samsung.com/uz_ru/refrigerators/all-refrigerators/?sbs")
html = driver_ref_sbs.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_ref_sbs.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_ref_sbs.page_source, "html.parser")
    time.sleep(3)
    volume = detail_info.find_all(class_="product-specs__spec-title")[0]["title"]
    if id == 0:
        height = detail_info.find_all(class_="product-specs__spec-title")[5]["title"]
    elif id == 2 or id == 3:
        height = "1780 мм"
    else:
        height = detail_info.find_all(class_="product-specs__spec-title")[3]["title"]
    refregirator_sbs = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "useful": volume.replace('\\xa0', ""),
        "height": height.replace("\\xa0", "")
    }
    home["categories"][4]["items"].append(refregirator_sbs)



# Vacuum Cleaner
driver_vac = driver_ref_sbs
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
        "image": "https:" + image,
        "power": power_of_suction
    }
    home["categories"][5]["items"].append(vacuum_cleaner) 
# Vacumm Cleaners without bag
driver_vac_bagless = driver_vac
driver_vac_bagless.get("https://www.samsung.com/uz_ru/vacuum-cleaners/all-vacuum-cleaners/?bagged")
html = driver_vac_bagless.page_source
soup = BeautifulSoup(html, "html.parser")
cards = soup.findAll(class_="product-card type-B")
for detail in cards:
    id = cards.index(detail)
    name = detail.find(class_="product-card__prd-info-title-name").text
    image = detail.find(class_ = "product-card__img-view-item").find("a").find("img")["src"]
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_vac_bagless.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_vac_bagless.page_source, "html.parser")
    power_of_suction = detail_info.find_all("span", class_="product-specs__highlights-desc")[4].text

    vacuum_cleaner_bagless = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "power": power_of_suction
    }
    home["categories"][6]["items"].append(vacuum_cleaner_bagless)

# VC = Vacuum Cleaners
# Wet-Dry VC
driver_vac_dry = driver_vac_bagless
driver_vac_dry.get("https://www.samsung.com/uz_ru/vacuum-cleaners/all-vacuum-cleaners/?wet-and-dry")
html = driver_vac_dry.page_source
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
    # link_detail = detail.find("a", class_="s-btn-encased")["href"]
    # driver_vac_dry.get("https://www.samsung.com" + link_detail)
    # detail_info = BeautifulSoup(driver_vac_dry.page_source, "html.parser")
    # power_of_suction = detail_info.find_all("span", class_="product-specs__highlights-desc")[4].text

    vacuum_cleaner_dry = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "colors": str(','.join(color)),
        "power": ""
    }
    home["categories"][7]["items"].append(vacuum_cleaner_dry)


# Vertical VC
driver_vac_vertical = driver_vac_dry
driver_vac_vertical.get("https://www.samsung.com/uz_ru/vacuum-cleaners/all-vacuum-cleaners/?stick-vc")
html = driver_vac_vertical.page_source
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
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_vac_vertical.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_vac_vertical.page_source, "html.parser")
    power_of_suction = detail_info.find_all("span", class_="product-specs__highlights-desc")[7].text

    vacuum_cleaner_vertical = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "colors": str(','.join(color)),
        "power": power_of_suction
    }
    home["categories"][8]["items"].append(vacuum_cleaner_vertical)

# Robot
vacuum_cleaner_robot = {
        "id": "None",
        "name": "None",
        "image": "None",
        "colors": "None",
        "power": "None"
    }
home["categories"][9]["items"].append(vacuum_cleaner_robot)

# Wireless
driver_vac_wireless = driver_vac_vertical
driver_vac_wireless.get("https://www.samsung.com/uz_ru/vacuum-cleaners/all-vacuum-cleaners/?wireless")
html = driver_vac_wireless.page_source
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
    link_detail = detail.find("a", class_="s-btn-encased")["href"]
    driver_vac_wireless.get("https://www.samsung.com" + link_detail)
    detail_info = BeautifulSoup(driver_vac_wireless.page_source, "html.parser")
    power_of_suction = detail_info.find_all("span", class_="product-specs__highlights-desc")[7].text

    vacuum_cleaner_wireless = {
        "id": id,
        "name": name,
        "image": "https:" + image,
        "colors": str(','.join(color)),
        "power": power_of_suction
    }
    home["categories"][10]["items"].append(vacuum_cleaner_wireless)



# SteamCase
driver_steam = driver_vac_wireless
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
    "image": "https:" + image,
    "character": "Парогенератор, Дезодорирующий фильтр, Тепловая сушка, Защита от складок на одежде"
}
home["categories"][11]["items"].append(steam_case) 




# Air conditioner Wall-Mount
driver_air = driver_steam
driver_air.get("https://www.samsung.com/uz_ru/air-conditioners/all-air-conditioners/?wall-mount")
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
            "image": "https:" + image,
            "energy": "C"
        }
        home["categories"][12]["items"].append(air_conditioner) 
    else:
        air_conditioner = {
            "id": id,
            "name": name,
            "image": "https:" + image,
            "energy": energy[4]
        }
        home["categories"][12]["items"].append(air_conditioner)
# Air Conditioner Standing
air_conditioner_standing = {
            "id": "None",
            "name": "None",
            "image": "None",
            "energy": "None"
    }
home["categories"][13]["items"].append(air_conditioner_standing)




with open('home.json', 'w', encoding='utf-8') as file:
   json.dump(home, file, ensure_ascii=False, indent=4)

driver_air.close()
