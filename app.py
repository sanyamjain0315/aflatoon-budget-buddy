from flask import Flask , render_template
from finance import search_youtube_videos
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

@app.route("/Scanner/")
def Scanner():
    return render_template('Scanner.html')

@app.route("/videos/")
def videos():
    data = search_youtube_videos("financa advice for students", 6)
    return render_template("videos.html", length = len(data), data=data)

@app.route("/Signup/")
def Signup():
    return render_template('signup.html')


@app.route("/Signin/")
def Signin():
    return render_template('signin.html')
