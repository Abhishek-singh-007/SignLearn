from flask import Flask, request, jsonify, send_from_directory
from cvzone.ClassificationModule import Classifier
import numpy as np
import cv2
import os
app = Flask(__name__, static_folder='static', template_folder='templates')


# Load the model
model_path = 'model1/keras_model.h5'
labels_path = 'model1/labels.txt'
classifier = Classifier(model_path, labels_path)

# Import functions from your scripts
from dataCollection import collect_data
from testing import run_testing

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/learn-alphabets', methods=['POST'])
def learn_alphabets():
    try:
        # Trigger data collection (if needed)
        # collect_data()
        
        # Run the model testing
        result = run_testing()
        
        response = {
            "status": "success",
            "message": result
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
