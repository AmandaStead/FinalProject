import pip
import requests
from flask import flask, request, jsonify, make_response, Flask, render_template
import json

app = Flask(__name__)


@app.route('/payment')
def home():
    return render_template('payment.html')


@app.route("/trailers")
def receipt():
    return render_template('trailers.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)