from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars
from splinter import Browser

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    mission_mars_data= mongo.db.mission_mars_data.find_one()
    return render_template("index.html", mars = mission_mars_data)


@app.route("/scrape")
def scrape():
    mission_mars_data = mongo.db.mission_mars_data
    mars_data = scrape_mars.scrape()
    mission_mars_data.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)