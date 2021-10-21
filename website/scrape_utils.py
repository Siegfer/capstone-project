import codecs
import json
from typing import Dict, List, Optional

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

PlantDetails = Dict[str, str]
Plants = Dict[str, PlantDetails]

def scrape_for_all_plant_routes(
    link: str,
) -> List[str]:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("tbody")
    plant_elements = table.find_all("div", class_="list-row-text")
    results = []
    for plant_elements in plant_elements:
        tag = plant_elements.find("a", href=True)
        save_list = tag["href"]
        results.append(save_list)
    return results


def format_column_name(name: str) -> str:
    arr = name.split()
    arr = [word.capitalize() for word in arr if word != "Help"]
    col = "".join(arr)
    return col


def scrape_plant_details(routes: List[str]) -> Plants:
    data: Plants = {}
    for route in routes:
        plant_url = f"https://permapeople.org{route}"
        response = requests.get(plant_url)
        page = BeautifulSoup(response.content, "html.parser")
        detail_box = page.find(class_="layout-grid")
        name_box = page.find(class_="data-primary")
        sci_name_box = name_box.em
        plant_attributes = detail_box.find_all("div", class_="data-set")
        name = str.strip(name_box.contents[0])
        sci_name = sci_name_box.text
        details = {"Name": f"{name}", "ScientificName": f"{sci_name}"}
        for attributes in plant_attributes:
            data_key = attributes.find("label", class_="data-key")
            key = format_column_name(data_key.text)
            value = attributes.find("span", class_="data-value").text
            details[str.strip(key)] = str.strip(value)
        data[route] = details
    return data


def scrape_all_pages(start: int, end: int, filename: str) -> None:
    base_uri = "https://permapeople.org/search?sort=name_asc"
    main_dictionary = {}
    with open(filename, "wb") as f:
        for i in tqdm(range(start, end + 1)):
            pagination_uri = base_uri + f"&page={i}"
            routes = scrape_for_all_plant_routes(pagination_uri)
            plants = scrape_plant_details(routes)
            # Do whatever you want for the "JSON" page_deets
            # Save to .json > Export as data frame, whatever
            main_dictionary = {**main_dictionary, **plants}
        json.dump(
            main_dictionary,
            codecs.getwriter("utf-8")(f),
            sort_keys=True,
            indent=4,
            ensure_ascii=False,
        )

if __name__ == "__main__":
    scrape_all_pages(1, 427, "test_scrape_dump.json")
