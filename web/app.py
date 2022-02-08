from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/show")
def show_template():
    # JSON file
    f = open ('/Users/devodriqroberts/Freelance/Webscraping/Playground/zillow/zillow_houses.json', "r")
    # Reading from file
    houses = json.loads(f.read())
    houses_data = json.dumps(houses)
    house = houses[0]
    columns = [col for col in house.keys()]
    # columns_clean

    return render_template("index.html", columns=columns, data=houses_data)

@app.route("/data")
def data():
    # JSON file
    f = open ('/Users/devodriqroberts/Freelance/Webscraping/Playground/zillow/zillow_houses.json', "r")
    
    # Reading from file
    houses = json.loads(f.read())
    houses = json.dumps(houses)
    return houses



if __name__ == '__main__':
    app.run(debug=True)