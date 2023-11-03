from flask import Flask, render_template
from markupsafe import escape
import random
import datetime
import requests
import json

AGEIFY_URL = "https://api.agify.io?name="
GENDERIZE_URL = "https://api.genderize.io?name="

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, footer=year)

@app.route('/guess/<name>')
def guess(name):
    age_json = requests.get(AGEIFY_URL + name)
    gender_json = requests.get(GENDERIZE_URL + name)
    age_result = json.loads(age_json.text)
    gender_result = json.loads(gender_json.text)
    age = age_result["age"]
    gender = gender_result["gender"]
    year = datetime.datetime.now().year
    return render_template("guess.html", age=age, gender=gender, footer=year, name=escape(name))

if __name__ == "__main__":
    app.run(debug=True)