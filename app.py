from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/calculator/")
def calculator():
    return render_template('calculator.html')