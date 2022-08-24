from flask import Flask, redirect, render_template, request
import requests
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<url>', methods=['GET', 'POST'] )
def url(url):
    req = requests.get('https://urlshortnerfutureproof.herokuapp.com/urls')
    data = req.json()
    for i in data:
        if url == i['shorturl']:
            return redirect(i['longurl'])
    return redirect('http://localhost:5000/')

@app.route('/result', methods=['GET', 'POST'] )
def result():
    if request.method == 'POST':

        longurl = request.form['longurl']

        req = requests.get('https://urlshortnerfutureproof.herokuapp.com/urls')
        data = req.json()

        foundurl = False
        for i in data:
            if longurl == i['longurl']:
                shorturl = i['shorturl']
                foundurl = True
                
        if foundurl == False:
            length = 10
            letters = string.ascii_letters
            shorturl = ''.join(random.choice(letters) for i in range(length))
            dataSent = {'shorturl': shorturl, 'longurl': longurl}
        
            post = requests.post('https://urlshortnerfutureproof.herokuapp.com/urls', json = dataSent)
        
        return render_template('result.html', shorturl = shorturl, longurl = longurl)
    else:
        return redirect('http://localhost:5000/')

@app.errorhandler(404)
def handle_404(e):
    return redirect('http://localhost:5000/')


# # if __name__ == '__main__':
# #     app.run(debug = True)
