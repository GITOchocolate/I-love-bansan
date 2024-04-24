from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/Page two")
def nopage():
    return render_template("Flask pepezi.html")

@app.route("/Page one")
def error():
    return render_template("Flask pipezii.html")

@app.route("/")
def normal():
    return render_template("Flask pamomizi.html")


app.run()