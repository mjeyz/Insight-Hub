import requests
import datetime
from flask import Flask, request, redirect, render_template, url_for
import random

app  = Flask(__name__)
app.config["SECRET_KEY"] = "123adacxcx"

date = datetime.date.today()
random_number = random.randint(1, 6237)

try:
    response = requests.get("https://api.alquran.cloud/v1/surah/1/ayah/1/ar.asad")
    response_02 = requests.get("https://api.aladhan.com/v1/timings/{date}?latitude=31.520370&longitude=74.358749")
    response_03 = requests.get(f"https://api.alquran.cloud/v1/ayah/{random_number}/ar.asad")
except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
else:
    quranData = response.json()
    ayah_data = response_03.json()

    random_ayah = ayah_data["data"]["text"]

    for ayah in quranData["data"]["ayahs"]:
        surah = ayah["text"]


@app.route("/", methods=["GET","POST"])
def home():
    return render_template("index.html", ayaah=random_ayah)

if __name__ == "__main__":
    app.run(debug=True)

# clean and understand data what's going on
# design frontend layout it contains navebar with logo home Prayer Time Quran page link
# in design use green color most
# header contain navebar and header with random Quran ayah