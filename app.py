from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    message = "Have a nice trip Eduard on Vacation"
    return render_template("greeting.html", message=message)
