from flask import Flask, request, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route("/experience0001/<int:id>")
def experience0001Id(id):
    return f"<p>Experience: {id}</p>"

@app.route("/experience0001")
def experience0001():
    return "<p>Experience 0001</p>"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/experience0001/login', methods=['POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        data = request.json
        return data

@app.route('/experience0001/redirection')
def redirection():
    return redirect(url_for('experience0001'))

@app.route('/experience0001/logs')
def logging():
    app.logger.debug('This is a test logger')
    app.logger.warning('This is a test warning')
    app.logger.error('This is a test error')
    return 'Test'