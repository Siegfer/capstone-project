import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api = os.getenv('API_KEY')
photo1 = "project4/project4/plant/IMG/photo1.jpeg"

def encode_file(file_name):
    with open(file_name, 'rb') as file:
        return base64.b64encode(file.read()).decode('ascii')
    
def identify_plant(file_names):
    params= {
        "api_key": "api",
        "images": [encode_file(img) for img in file_names],
        "modifiers": ["crops_fast", "similar_images", "health_all"],
        "plant_language": "en",
        "plant_details": ["common_names",
            "edible_parts",
            "gbif_id",
            "name_authority",
            "propagation_methods",
            "synonyms",
            "taxonomy",
            "url",
            "wiki_description",
            "wiki_image",
                          ],
    }

    headers = {
    "Content-Type": "application/json"
    }

    response = requests.post("https://api.plant.id/v2/identify", 
    json=params,
    headers=headers)
    
    return response.json()


if __name__ == "__main__":
    # print(identify_plant([photo1]))
    pass