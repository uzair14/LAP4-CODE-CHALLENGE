from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS

from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')


# if __name__ == '__main__':
#     app.run(debug = True)
