from flask import Flask, jsonify, redirect, render_template, request
import requests
from flask_cors import CORS
import random
import string

from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/url/<url>', methods=['GET', 'POST'] )
def url(url):
    req = requests.get('https://urlshortnerfutureproof.herokuapp.com/urls')
    data = req.json()
    # print(data)
    for i in data:
        if url == i['shorturl']:
            print(i['longurl'])
            return redirect(i['longurl'])
        # print(i['shorturl'])
    return redirect('http://localhost:5000/')

@app.route('/result', methods=['GET', 'POST'] )
def result():
    if request.method == 'POST':
        longurl = request.form['longurl']
        length = 10
        letters = string.ascii_letters
        shorturl = ''.join(random.choice(letters) for i in range(length))
        data = {'shorturl': shorturl, 'longurl': longurl}
        # print(data)
        req = requests.post('https://urlshortnerfutureproof.herokuapp.com/urls', json = data)
        print(req)
        return render_template('result.html', shorturl = shorturl, longurl = longurl)
    else:
        return redirect('http://localhost:5000/')


# # if __name__ == '__main__':
# #     app.run(debug = True)
