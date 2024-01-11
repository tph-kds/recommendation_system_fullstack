from flask import Flask, render_template, json, jsonify
import pandas as pd 
import numpy as np 
from app import *


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("app/index.html")



if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=True)