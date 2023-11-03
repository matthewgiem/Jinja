from flask import Flask, render_template
from markupsafe import escape
import random
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, footer=year)

@app.route('/guess/<name>')
def guess(name):
    year = datetime.datetime.now().year
    return render_template("guess.html", footer=year, name=escape(name))

if __name__ == "__main__":
    app.run(debug=True)