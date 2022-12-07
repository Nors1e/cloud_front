from flask import Flask, redirect, render_template, url_for, request
from markupsafe import escape


# Instance of a flask web application
app = Flask(__name__)

# Add in the 
@app.route("/")
def home():
    return render_template("index.html")
