import os
import flask
from flask import Flask
from flask_cors import CORS
import pandas as pd

# create Flask app
app = Flask(__name__)
CORS(app)

# Import some csv
data = pd.read_csv('exampleData.csv')
#### You'd manipulate the data and such in Python here with Pandas


# Simplest data passing
@app.route('/simpleData', methods=['GET'])
def get_signals():
    # We'd change the data to json to pass data to Observable
    return data.to_json(orient='index')

@app.route('/requestData', methods=['POST'])
def request_data():
    # Grab information from POST request
    requestData = flask.request.json

    # This filters the data frame by the difficulty column, it's like R!
    difficultyRequest = requestData['Difficulty']
    outData = data.loc[data['Difficulty'] == difficultyRequest]

    return outData.to_json(orient='index')

# execute the application (by default, it should be hosted at localhost:5000, which you will see in the output)
if __name__ == '__main__':
    app.run()