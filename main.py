"""
This program will have two core functionalities:
    1) Given an ingredient list, compile a list of recipes that include them.
    2) Given a list of recipes, compile either a list of ingredients or
       recommend new recipes.
This will be written in Flask to ensure that the webapp functioanlity is easy
to use.
"""

# importing the module
from flask import Flask, render_template

# instantiating the flask object
app = Flask(__name__)

# defining the home page
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()