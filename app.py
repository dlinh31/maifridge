from flask import Flask, render_template, request, jsonify
from ai_response import get_dishes
from ai_images import get_images



food_dict = {}

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/start")
def start():
    return render_template("index.html")

@app.route('/process', methods=['POST']) 
def process(): 
    global food_dict
    data = request.get_json()['data'] # retrieve the data sent from JavaScript 
    print(data)
    # process the data using Python code 
    food_dict = get_dishes(data)
    print (food_dict)
    return jsonify(result=food_dict)

@app.route('/url', methods=['POST'])
def url():
    url_dict = get_images(food_dict)
    print(url_dict)
    return jsonify(result=url_dict)

@app.route('/food', methods=['POST']) 
def food():
    return render_template("index.html", food_dict=food_dict)


if __name__ == "__main__":
    app.run(debug=True)