from flask import Flask, render_template, request

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uberman")
def uberman():
    return render_template("uberman.html")

@app.route("/dymaxion")
def dymaxion():
    return  render_template("dymaxion.html")


"""
@app.route("/uberman")
def uberman():
    return render_template("uberman.html")

@app.route("/dymaxion")
def dymaxion():
    return render_template("dymaxion.html")
"""