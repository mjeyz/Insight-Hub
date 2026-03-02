import requests
import datetime
from flask import Flask, request, redirect, render_template, url_for
from test import random_ayah

app  = Flask(__name__)
app.config["SECRET_KEY"] = "123adacxcx"

date = datetime.date.today()

response = requests.get("https://api.alquran.cloud/v1/surah/1/ayah/1/ar.asad")
quranData = response.json()

response_02 = requests.get("https://api.aladhan.com/v1/timings/{date}?latitude=31.520370&longitude=74.358749")

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