#import libraries
import numpy as np
from flask import Flask, render_template
import pickle

#Initialize the flask App
app = Flask(__name__)

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)