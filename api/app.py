from flask import Flask
import pymongo

app = Flask(__name__)

@app.route("/")
def hey():
  return "Hello, World!!"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000, debug=True)