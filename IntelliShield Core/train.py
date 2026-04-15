# Purpose: Train Random Forest model and save it as classifier/random_forest.pkl

import numpy as np
import os
import joblib
from sklearn.ensemble import RandomForestClassifier

# ====================== CONFIG ======================
DATASET_PATH = 'dataset/Training Dataset.arff'
MODEL_DIR = 'classifier'
MODEL_PATH = os.path.join(MODEL_DIR, 'random_forest.pkl')

# Create classifier directory if it doesn't exist
os.makedirs(MODEL_DIR, exist_ok=True)

print("Loading dataset...")
data_file = open(DATASET_PATH, 'r', encoding='utf-8').read()

data_list = data_file.split('\n')          # Use '\n' instead of '\r\n' for better compatibility
data = np.array(data_list)

# Convert to list of lists
data1 = [line.split(',') for line in data if line.strip() and not line.startswith('@')]

print(f"Total samples loaded: {len(data1)}")

# Extract labels (last column)
labels = [row[-1] for row in data1]

# Convert to numpy array and remove last column (label)
data1 = np.array(data1)
features = data1[:, :-1]

# Select only the most relevant features (as per your original selection)
selected_features = [0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 24, 25, 27, 29]
features = features[:, selected_features]

# Convert to float
features = features.astype(np.float64)

print(f"Features shape: {features.shape}")
print(f"Number of selected features: {features.shape[1]}")

# ====================== TRAINING ======================
print("\nTraining Random Forest Model...")

clf = RandomForestClassifier(
    n_estimators=100,
    min_samples_split=7,
    random_state=42,
    n_jobs=-1,           # Use all CPU cores
    verbose=True
)

clf.fit(features, labels)

# ====================== FEATURE IMPORTANCE ======================
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]

print("\nFeature ranking:")
for f in range(features.shape[1]):
    print(f"{f+1:2d}. Feature {indices[f]:2d} — Importance: {importances[indices[f]]:.6f}")

# ====================== SAVE MODEL ======================
joblib.dump(clf, MODEL_PATH, compress=9)
print(f"\n✅ Model successfully saved at: {MODEL_PATH}")
print("You can now use this model with test.py")