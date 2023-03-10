from flask import Flask
from flask_pymongo import PyMongo
import os
import time

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:qrFiSNz1reAdy9LNpBaj@containers-us-west-89.railway.app:7218"
mongo = PyMongo(app)

@app.route("/")
def hello_world():
    for _ in range(50):
        return "<p>Hello, Railway! :D</p>"
    time.sleep(5)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("PORT", default=5000), debug=True) 
