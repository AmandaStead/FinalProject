import pip
import requests
from flask import flask, request, jsonify, make_response, Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('MovieTitles.html')

@app.route("/Receipt")
def receipt():
    return render_template('Receipt.html')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Click to See Descriptions':
            return render_template("description.html")  # This will be for Movie Descriptions

@app.route('/Date')
def date():
    return render_template('DateTime.html')

@app.route("/Snacks")
def snacks():
    return render_template('Snacks.html')

@app.route("/Booking")
def booking():
    return render_template('BookingTitles.html')

@app.route("/description")
def description():
    return render_template('description.html')

@app.route("/seatSelection")
def seatSelection():
    return render_template('seatSelection.html')

@app.route("/Location")
def location():
    return render_template('LocationTitle.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')


@app.route("/trailers")
def trailers():
    return render_template('trailers.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
