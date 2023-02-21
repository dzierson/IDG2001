from flask import Flask
from pymongo import MongoClient
import os
import time

app = Flask(__name__)

client = MongoClient('0.0.0.0', 'PORT')

db = client.flask_db
todos = db.todos

@app.route("/")
def hello_world():
    for _ in range(50):
        return "<p>Hello, Railway! :D</p>"
    time.sleep(5)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv("PORT", default=5000), debug=True) 
