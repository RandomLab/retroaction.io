from app import app

from flask import render_template

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/radio")
def radio():
  return render_template("radio.html")