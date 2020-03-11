# import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_cdc

# Create an instance of Flask
app = Flask(__name__, static_url_path="/static")

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/cdc_app")

# create home route and define home function
@app.route("/")
def home():
    # Find one record of data from the mongo database
    cdc_info = mongo.db.cdc_collection.find_one()

    # Return template and data
    return render_template("index.html", cdc_data=cdc_info)

# create scrape route 
@app.route("/scrape")
def scrape():
    # run the scrape function
    cdc_data = scrape_cdc.scrape()

    # insert the mars data in to the collection
    mongo.db.cdc_collection.update({}, cdc_data, upsert=True)

    # go back to the home page
    return redirect("/")

# run the app
if __name__ == "__main__":
    app.run(debug=True)
