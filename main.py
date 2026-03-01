import requests
import datetime

date = datetime.date.today()

response = requests.get("https://api.alquran.cloud/v1/surah/1")
quranData = response.json()

response_02 = requests.get("https://api.aladhan.com/v1/timings/{date}?latitude=31.520370&longitude=74.358749")
print(response_02.json())

for ayah in quranData["data"]["ayahs"]:
    surah = ayah["text"]
    print(surah)


# clean and understand data what's going on
# design frontend layout it contains navebar with logo home Prayer Time Quran page link
# in design use green color most
# header contain navebar and header with random Quran ayah