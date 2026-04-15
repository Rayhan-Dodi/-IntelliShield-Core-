# Purpose: Receive URL from Chrome extension (via PHP), extract features,
#          run ML model and return final result (SAFE / PHISHING)

import sys
import numpy as np
import joblib
import features_extraction
import os

# ====================== CONFIG ======================
# Update these paths according to your setup
LOCALHOST_PATH = "/Library/WebServer/Documents/"   # Change for Windows/Linux
DIRECTORY_NAME = "IntelliShield-Core"

MODEL_PATH = os.path.join(LOCALHOST_PATH, DIRECTORY_NAME, "classifier/random_forest.pkl")


def get_prediction_from_url(test_url):
    try:
        # Extract features
        features_list = features_extraction.main(test_url)
        
        # Convert to 2D array for scikit-learn
        features_array = np.array(features_list).reshape(1, -1)

        # Load the trained model
        clf = joblib.load(MODEL_PATH)

        # Make prediction
        prediction = clf.predict(features_array)[0]

        return int(prediction)

    except FileNotFoundError:
        print(f"Error: Model file not found at {MODEL_PATH}")
        return -1
    except Exception as e:
        print(f"Error during prediction: {e}")
        return -1


def main():
    if len(sys.argv) < 2:
        print("PHISHING")  # Default to safe side if no URL
        return

    url = sys.argv[1]

    prediction = get_prediction_from_url(url)

    if prediction == 1:
        print("SAFE")
    else:
        print("PHISHING")


if __name__ == "__main__":
    main()