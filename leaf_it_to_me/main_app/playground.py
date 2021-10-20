import requests
from bs4 import BeautifulSoup

# URL = "https://permapeople.org/search?sort=name_asc"
URL = "https://permapeople.org/plants/thermopsis-villosa-aaron-s-rod"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="layout-grid")
# print(results.prettify())
plant_elements = results.find_all("div", class_="data-set")
for plant_elements in plant_elements:
    data_key = plant_elements.find("label", class_="data-key")
    data_value = plant_elements.find("span", class_="data-value")
    # print(plant_elements, end="\n" * 2)
    print(data_key.text)
    print(data_value.text)
    print()
