# Sign Language Learning Web App

This web application is designed to help deaf and mute individuals learn sign language in an interactive and engaging manner. The application integrates machine learning models to recognize and interpret sign language gestures, offering users the opportunity to learn alphabets and words in sign language.

## Features
- **Learn Alphabets and Words**: Users can interactively learn sign language alphabets and words.
- **Machine Learning Integration**: The app uses trained ML models (`keras_model.h5` and `labels.txt`) for accurate gesture recognition.
- **Interactive Interface**: A user-friendly interface with animations for an enhanced learning experience.
- **Flask Framework**: Built using the Flask web framework for seamless back-end and front-end integration.

## Learning Flow
1. **Select Learning Module**:  
   From the homepage, users can choose between "Learn Alphabets" and "Learn Words."

2. **Gesture Recognition**:  
   The application uses a webcam to capture the user’s gestures in real-time. The integrated ML model interprets these gestures and provides immediate feedback.

3. **Learning Feedback**:  
   - For alphabets: The app displays recognized letters and suggests corrections if gestures don’t match.
   - For words: Users are guided through word gestures step-by-step with visual aids.

4. **Completion and Review**:  
   After completing a session, users can review their performance and retry exercises.

## Technologies Used
- **Front-End**: HTML, CSS, JavaScript
- **Back-End**: Flask (Python Framework)
- **Machine Learning Framework**: TensorFlow and Keras
- **Other Tools**: OpenCV for video processing

## Machine Learning Model
The application leverages a pre-trained neural network model built using TensorFlow and Keras.  
- **Model File**: `keras_model.h5`  
  This file contains the trained neural network capable of recognizing sign language gestures.  
- **Labels File**: `labels.txt`  
  This file maps the output of the model to corresponding sign language characters or words.  

The model was trained using a dataset of hand gestures, and OpenCV was used for preprocessing video frames to extract relevant features for training.

## Installation and Setup
To set up and run the application locally, follow these steps:

1. Clone the repository and navigate to its directory:
   ```bash
     git clone <repository-url>
     cd <repository-directory>
2. Set up a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate    # For Linux/Mac
    venv\Scripts\activate       # For Windows
3. pip install -r requirements.txt

   pip install -r requirements.txt
   
4.Run the Flask application:
 
  python app.py


Some images of project:-
![Screenshot 2024-09-08 043844](https://github.com/user-attachments/assets/78a68547-e1db-4752-b5ad-cf5ae690cab7)
![Screenshot 2024-09-08 043857](https://github.com/user-attachments/assets/7896bbfe-dce2-46eb-9696-3016ad245fb3)
![Screenshot 2024-09-08 041240](https://github.com/user-attachments/assets/3f6b1e7c-87ad-4800-abed-a5d3b419cb83)
![Screenshot 2024-08-31 103022](https://github.com/user-attachments/assets/f4684c1d-79b5-46b2-8813-dc36d36d5fa6)
