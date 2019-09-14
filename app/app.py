# Libraries
from flask import Flask, request, render_template, url_for, redirect

# Variables
USER_XCOORDINATE = ""
USER_YCOORDINATE = ""
USER_ID = ""

API_KEY = ""

# Create Dataset instance from Brendon's code and call function. 
dataset = Dataset(kevins_data)
locations = dataset.get_recommendations(dictionary_of_sliders_and_lat_long)

# Instantiating app
app = Flask(__name__)
app.config['SECRET_KEY'] = "YnJRcS9HWjY+DZoFHtE"

# Establishing route for home connection
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', api_key = API_KEY)

# Running app in debug mode
if __name__ == '__main__':
    app.run(debug = True)