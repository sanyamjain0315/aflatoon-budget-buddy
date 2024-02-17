from flask import Flask , render_template, request, redirect
from finance import search_youtube_videos
import matplotlib.pyplot as plt
import os
import requests
from PIL import Image
from ocr import extract_receipt
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient("mongodb://localhost:27017")
db = client['budgetBuddy']
collection = db['users']


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


@app.route("/videos/")
def videos():
    data = search_youtube_videos("financa advice for students", 6)
    return render_template("videos.html", length = len(data), data=data)

@app.route("/Signup/")
def Signup():
    return render_template('signup.html')

@app.route("/Scanner/", methods=["GET", "POST"])
def Scanner():
    if request.method == "POST":
        if request.files:

            image = request.files['image']
            image.save("static/sample.png")
            try:
                unique = extract_receipt()
                return render_template('file_uploader.html', data=True, unique=unique, img=image)
            except:
                return render_template("file_uploader.html")

    return render_template('file_uploader.html', data=False)
@app.route("/Signin/")
def Signin():
    return render_template('signin.html')

@app.route("/chatbot/", methods=['POST', 'GET'])
def chatbot():
    if request.method == "POST":
        user_input = request.form['user_input']
        payload = {"question": user_input}
        response = requests.post(os.getenv("FLOWISE_URL"), json=payload).json()['text']
        print(r"{}".format(response))
        return render_template("chatbot.html", user_input=user_input, chatbot_response=response)
    else:
        return render_template("chatbot.html")


@app.route("/update-balance", methods=["POST"])
def getBalance():
    if request.method == "POST":
        global balance 
        balance = int(request.form['new_balance'])
        return render_template("balance_input.html")

@app.route("/create-user/", methods=['GET', "POST"])
def createUser():
    if request.method == "POST":
        username = request.form['username']
        user = collection.find_one({"username": username})
        if user:
            password = request.form['password']
            if password == user['password']:
                return render_template("user_input.html")

if __name__ == "__main__":
    app.run(debug=True)
