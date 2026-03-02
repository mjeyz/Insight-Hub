import requests
import random

random_number = random.randint(1, 6237)

response = requests.get(f"https://api.alquran.cloud/v1/ayah/{random_number}/ar.asad")
data = response.json()
random_ayah = data["data"]["text"]
print(random_ayah)