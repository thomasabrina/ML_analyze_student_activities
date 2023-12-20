from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import joblib
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Get the system path
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the model paths
model_filename = 'forest_model_third.pkl'
classification_model_filename = 'classification_model.joblib'
model_path = os.path.join(script_dir, 'models', model_filename)
classification_model_path = os.path.join(script_dir, 'models', classification_model_filename)

# Load prediction model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    file = request.files['file']  # Get uploaded file
    print('Received file: ' + file.filename)  # Print the file name

    data = pd.read_csv(file)  # Read the file 
    print('Data: ' + str(data))  # Print the data 

    prediction = model.predict(data)  # Predict using the model
    print('Prediction: ' + str(prediction))  # Print prediction results

    return jsonify('\n'.join(map(str, prediction.tolist())))  # Print result on website

@app.route('/classify', methods=['POST'])
def classify_route():
    file = request.files['file']  # Get uploaded file
    print('Received file: ' + file.filename)  # Print the file name

    data = pd.read_csv(file)  # Read the file 
    data = data[['attempts_sum', 'maxscore_sum', 'Score']]  # Select 'attempts_sum', 'maxscore_sum' and 'Score'
    print('Data: ' + str(data))  # Print the data 

    # Load classification model
    classification_model = joblib.load(classification_model_path)

    clusters = classification_model.predict(data)  # Classify using model
    print('Clusters: ' + str(clusters))  # Print calssification results

    return jsonify('\n'.join(map(str, clusters.tolist())))  # Print result on website

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True)