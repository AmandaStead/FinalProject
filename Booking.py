import random
from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)


@app.route("/Booking")
def booking():
    return render_template('BookingTitles.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
