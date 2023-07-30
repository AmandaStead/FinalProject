import random
from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)


# Routing to the local host with given "Location"
@app.route("/Location")
def booking():
    return render_template('LocationTitle.html')


# Below code will run on local host with port 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
