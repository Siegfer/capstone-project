import requests
from bs4 import BeautifulSoup
from typing import List

URL = "https://permapeople.org/search?sort=name_asc"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")
# # results = soup.find(id="list-entry-")
# table = soup.find("tbody")
# plant_elements = table.find_all("div", class_="list-row-text")
# # print(len(plant_elements))
# for plant_elements in plant_elements:
#     tag = plant_elements.find("a", href=True)
#     # print(tag["href"], end="\n" * 2)


def scrape_plant_page_uri(
    link: str,
) -> List[str]:
    # TODO: Write a function that will take in a page, which is a string that
    # represents the url pointing to the db page being referenced. The expected
    # output will be a list of all scraped routes from the contents of the pagination
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("tbody")
    plant_elements = table.find_all("div", class_="list-row-text")
    results = []
    for plant_elements in plant_elements:
        tag = plant_elements.find("a", href=True)
        save_list = tag["href"]
        results.append(save_list)
    return results


print(scrape_plant_page_uri(URL))
