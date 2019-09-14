# Libraries
from flask import Flask, request, render_template, url_for, redirect, jsonify
import random, json

# Variables
USER_XCOORDINATE = ""
USER_YCOORDINATE = ""
USER_ID = ""

API_KEY = "AIzaSyDySz37lxM4MpNo3tuUEVF7SOk26eDAr-8"

# Create Dataset instance from Brendon's code and call function. 
# dataset = Dataset(kevins_data)
# locations = dataset.get_recommendations(dictionary_of_sliders_and_lat_long)

# Instantiating app
app = Flask(__name__)
app.config['SECRET_KEY'] = "YnJRcS9HWjY+DZoFHtE"

# Establishing route for home connection
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', api_key = API_KEY)

# Posts data using jQuery
@app.route('/reciever', methods = ['POST'])
def worker():
    # Data recieved right now is not in correct JSON format
    #print("python")
    #print(request.data)
    
    if request.is_json:
        print("Is json")
    else:
        print("Not json")

    data = request.get_json()
    print(data)

    print(data['test'])
    return jsonify(data)

# Running app in debug mode
if __name__ == '__main__':
    app.debug = True
    app.run(debug = True)