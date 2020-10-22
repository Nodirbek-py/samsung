import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import json
chrome = "./chromedriver_win32/chromedriver.exe"
driver_z = webdriver.Chrome(executable_path=chrome)
url = "https://www.samsung.com/uz_ru/smartphones/all-smartphones/"

mobile = {
    "status": "1",
    "categories":[
        {
            "title": "Galaxy Z",
            "items": []
        },
        {
            "title": "Galaxy S",
            "items": []
        },
        {
            "title":"Galaxy Note",
            "items":[]
        },
        {
            "title": "Galaxy A",
            "items":[]
        }
    ]
}

# Galaxy Z
driver_z.implicitly_wait(10)

url = url + "?galaxy-z"
driver_z.get(url)
names = driver_z.find_elements_by_class_name('product-card__prd-info-title-name')
names = [x.text for x in names]
while("" in names) : 
    names.remove("")


colors = driver_z.find_elements_by_class_name("product-card__img-ctrl-list")
color = [x.text.replace("\nselected", "") for x in colors]
available_colors = color[:-1]
available_colors[1] = available_colors[1].replace("\n", ",")

capacity = driver_z.find_elements_by_class_name("product-card__img-ctrl-list")
available_capacity = [x.text.replace("\nselected", "") for x in capacity]
available_capacity = available_capacity[2:]

image_urls = []
image_links = driver_z.find_elements_by_xpath('//a[@class="product-card-pdp-link"]/img')
for i in image_links:
    image_urls.append(i.get_attribute('src'))

for i in range(0, len(names)):
    galaxy_z = {
        "id": i,
        "name": names[i],
        "image": image_urls[i],
        "params":[{
            "colors": available_colors[i]
        }]
    }

    mobile["categories"][0]["items"].append(galaxy_z)
driver_z.close()

# Galaxy S
driver_s = webdriver.Chrome(executable_path = chrome)
driver_s.implicitly_wait(10)
driver_s.get("https://www.samsung.com/uz_ru/smartphones/all-smartphones/?galaxy-s")
names = driver_s.find_elements_by_class_name('product-card__prd-info-title-name')
names = [x.text for x in names]
while("" in names) : 
    names.remove("") 


colors = driver_s.find_elements_by_class_name("product-card__img-ctrl-list")
color = [x.text.replace("\nselected", "") for x in colors]
color = color[:-1]
while("128 ГБ" in color):
    color.remove("128 ГБ")


for i in range(0, len(color)):
    color[i] = color[i].replace("\n", ",")


capacity = driver_s.find_elements_by_class_name("product-card__img-ctrl-list")
available_capacity = [x.text.replace("\nselected", "") for x in capacity]
for i in range(0, len(available_capacity)):
    available_capacity[i] = available_capacity[i].replace("\n", ",")

for i in available_capacity:
    if any(map(str.isdigit, i)) is False:
        available_capacity.remove(i)
available_capacity = available_capacity[1:]
available_capacity.insert(0, "None")

image_urls = []
image_links = driver_s.find_elements_by_xpath('//a[@class="product-card-pdp-link"]/img')
for i in image_links:
    image_urls.append(i.get_attribute('src'))

for i in range(0, len(names)):
    galaxy_s = {
        "id": i,
        "name": names[i],
        "image": image_urls[i],
        "params": [{
            "colors": color[i],
            "capacity": available_capacity[i]   
        }]
    }

    mobile["categories"][1]["items"].append(galaxy_s)
driver_s.close()
# Galaxy Note
driver_note = webdriver.Chrome(executable_path = chrome)
driver_note.implicitly_wait(10)
driver_note.get("https://www.samsung.com/uz_ru/smartphones/all-smartphones/?galaxy-note")
names = driver_note.find_elements_by_class_name('product-card__prd-info-title-name')
names = [x.text for x in names]
while("" in names) : 
    names.remove("") 

colors = driver_note.find_elements_by_class_name("product-card__img-ctrl-list")
color = [x.text.replace("\nselected", "") for x in colors]
color = color[:-1]
while("128 ГБ" in color):
    color.remove("128 ГБ")
while("256 ГБ" in color):
    color.remove("256 ГБ")
for i in range(0, len(color)):
    color[i] = color[i].replace("\n", ",")

capacity = driver_note.find_elements_by_class_name("product-card__img-ctrl-list")
available_capacity = [x.text.replace("\nselected", "") for x in capacity]
for i in range(0, len(available_capacity)):
    available_capacity[i] = available_capacity[i].replace("\n", ",")

for i in available_capacity:
    if any(map(str.isdigit, i)) is False:
        available_capacity.remove(i)
available_capacity = available_capacity[1:]
available_capacity.insert(0, "None")
available_capacity.insert(1, "None")


image_urls = []
image_links = driver_note.find_elements_by_xpath('//a[@class="product-card-pdp-link"]/img')
for i in image_links:
    image_urls.append(i.get_attribute('src'))

for i in range(0, len(names)):
    galaxy_note = {
        "id": i,
        "name": names[i],
        "image": image_urls[i],
        "params": [{
            "colors": color[i],
            "capacity": available_capacity[i]   
        }]
    }
    mobile["categories"][2]["items"].append(galaxy_note)
driver_note.close()



# Galaxy A
driver_a = webdriver.Chrome(executable_path = chrome)

driver_a.get("https://www.samsung.com/uz_ru/smartphones/all-smartphones/?galaxy-a")


names = driver_a.find_elements_by_class_name('product-card__prd-info-title-name')
names = [x.text for x in names]
while("" in names) : 
    names.remove("") 
colors = driver_a.find_elements_by_class_name("product-card__img-ctrl-list")
color = [x.text.replace("\nselected", "") for x in colors]
color = color[:-1]
while("128 ГБ" in color):
    color.remove("128 ГБ")
while("64 ГБ" in color):
    color.remove("64 ГБ")
while("32 ГБ" in color):
    color.remove("32 ГБ")
while("16 ГБ" in color):
    color.remove("16 ГБ")
while("64 ГБ\n128 ГБ" in color):
    color.remove("64 ГБ\n128 ГБ")

for i in range(0, len(color)):
    color[i] = color[i].replace("\n", ",")


capacity = driver_a.find_elements_by_class_name("product-card__img-ctrl-list")
available_capacity = [x.text.replace("\nselected", "") for x in capacity]
for i in range(0, len(available_capacity)):
    available_capacity[i] = available_capacity[i].replace("\n", ",")

for i in available_capacity:
    if any(map(str.isdigit, i)) is False:
        available_capacity.remove(i)
available_capacity = available_capacity[1:]
available_capacity.remove(available_capacity[-3])

image_urls = []
image_links = driver_a.find_elements_by_xpath('//a[@class="product-card-pdp-link"]/img')
for i in image_links:
    image_urls.append(i.get_attribute('src'))
print(len(available_capacity))

for i in range(0, len(names)):
    galaxy_a = {
        "id": i,
        "name": names[i],
        "image": image_urls[i],
        "params": [{
            "colors": color[i-1],
            "capacity": available_capacity[i-2]   
        }]
    }
driver_a.close()


with open('mobile.json', 'w', encoding='utf-8') as file:
   json.dump(mobile, file, ensure_ascii=False, indent=4)
