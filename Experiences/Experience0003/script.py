from flask import Flask
from file1 import file1_api
from file2 import file2_api

app = Flask(__name__)

app.register_blueprint(file1_api)
app.register_blueprint(file2_api, url_prefix='/experience0003')

@app.route("/experience0003")
def hello_world():
    return "File script"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)