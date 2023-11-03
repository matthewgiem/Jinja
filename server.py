from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, footer=year)

if __name__ == "__main__":
    app.run(debug=True)