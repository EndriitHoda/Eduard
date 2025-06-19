from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = "Have a nice trip Eduard on Vacation"
    return render_template("greeting.html", message=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
