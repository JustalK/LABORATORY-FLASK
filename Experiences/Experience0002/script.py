import requests

from flask import Flask, Response

app = Flask(__name__)

@app.route("/experience0002")
def test1():
    rsl = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return rsl.text

@app.route("/experience0002/2")
def test2():
    try:
        raise Exception
    except Exception:
        return "error"

@app.route("/experience0002/3")
def test3():
    return Response("Whatever", status=201, mimetype='application/json')
