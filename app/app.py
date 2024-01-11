import numpy as np 
import pandas as pd 
from flask import Flask, render_template, request, json, jsonify, url_for
from components.functions import Model
from components.read_file import file, read_file_csv
k = 50

data_weight, data_cb, similarity_cb, model_cfb, bg_pivot_cfb = file()
data = read_file_csv()
data.loc[data["yearpublished"] < 0, "yearpublished"] = "Không có thông tin"
data_test = data.iloc[:7, :]
data_test["rating"] = data_test["rating"].round(1)

data_ranking = data.sort_values(by=["Board Game Rank"], ascending=True)
data_ranking = data_ranking.iloc[:5, :]
data_ranking = data_ranking.T

# data


app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("index.html", data = data )

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html", data = data )

@app.route("/informations", methods = ["GET", "POST"])
def shop():
    return render_template("shop.html", data = data_test.T , data_ranking = data_ranking)

@app.route("/product_details", methods = ["GET", "POST"])
def product_details():
    return render_template("product-details.html", data = data )

@app.route("/recommendation", methods = ["GET", "POST"])
def recommendations():
    return render_template("recommendation.html",data = data_test.T , data_ranking = data_ranking)

@app.route("/recommendation/success", methods = ["GET","POST"])
def recommendations_success():
    if request.method == "POST":
        boardgame_name = request.form["boardgame_name"]
        print(boardgame_name)
    model = Model(data_cb, data_weight, similarity_cb,model_cfb,  boardgame_name,bg_pivot_cfb, k)
    data_rs = model.hybrid_rs()
    data_rs = data_rs.iloc[:10, :]
    print(data_rs)
    return render_template('recommendation.html' , data = data_rs.T, boardgame_name = boardgame_name)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)