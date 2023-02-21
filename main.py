from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    for _ in range(50):
        return "<p>Hello, Railway! :D</p>"
    time.sleep(5)

if __name__ == '__main__':
    app.run(host="0.0.0.0:$PORT")
