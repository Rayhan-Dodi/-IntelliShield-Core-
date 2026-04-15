

# IntelliShield Core

#### Video Demo: <[Youtube Explanation Video](https://youtu.be/FFAQSNanKgg)>

## Description

**IntelliShield Core** is a machine learning–powered browser security system designed to detect and block phishing and malicious websites in real time. It operates as a Chrome extension supported by a backend ML pipeline that analyzes URL structure, extracted behavioral features, and trained classification models to determine whether a website is safe or potentially harmful.

Unlike traditional security systems that depend on static blacklists or manually updated threat databases, IntelliShield Core uses a trained machine learning model to generalize patterns of malicious behavior. This allows it to detect both known phishing websites and previously unseen or evolving attack patterns. The system combines browser-side components (extension) with a Python-based training and feature engineering pipeline.

---

# Project Structure Overview

The project is divided into four major layers:

1. **Chrome Extension (Frontend Security Layer)**
2. **Machine Learning Training & Inference Pipeline**
3. **Data Processing & Feature Engineering**
4. **Documentation & Configuration**

---

# 1. Chrome Extension (Extension/)

### `Manifest.json`

This file defines the Chrome extension configuration, permissions, and execution context. It specifies:

* Background scripts for monitoring tab activity
* Popup UI entry point
* Required permissions (tabs, storage, web navigation)

It acts as the backbone of the extension, enabling interaction between browser events and the ML-based detection system.

### `popup.html`

This file provides the user interface shown when clicking the extension icon. It displays:

* Current website safety status
* Warning messages (if detected malicious)
* Basic analytics such as last scan result

### `popup.js`

Handles logic for the popup UI. It communicates with background scripts to:

* Fetch classification results for the current tab
* Update UI dynamically based on prediction output
* Trigger user notifications for unsafe websites

### `style.css`

Defines styling for the popup interface. It ensures:

* Clear visual separation between safe and dangerous states
* Responsive UI layout
* Warning emphasis using color-coded alerts

---

# 2. Machine Learning Core (classifier/)

### `random_forest.pkl`

This is the trained **Random Forest classifier model**, serialized after training. It is the core decision-making engine that classifies URLs as:

* Safe (0)
* Phishing/Malicious (1)

The model was selected due to its:

* Strong performance on tabular feature data
* Resistance to overfitting
* Fast inference suitable for real-time browser usage

---

# 3. Dataset & Training (dataset/, train.py)

### `Training Dataset.arff`

This dataset contains labeled URL samples used to train the classifier. It includes:

* Benign websites
* Phishing websites
* Feature vectors extracted from URLs

### `train.py`

This script handles the full ML training pipeline:

* Loads dataset
* Cleans and preprocesses features
* Trains Random Forest classifier
* Evaluates accuracy
* Saves trained model to `random_forest.pkl`

This file is central to the ML lifecycle of the project.

---

# 4. Feature Engineering & Detection Logic

### `features_extraction.py`

This script converts raw URLs into numerical feature vectors used by the ML model. Features include:

* URL length
* Number of special characters
* Presence of suspicious keywords (e.g., “login”, “verify”)
* Subdomain depth
* HTTPS usage
* Entropy of domain name

This step is critical because model accuracy depends heavily on feature quality.

---

### `patterns.py`

Defines rule-based heuristics used alongside ML classification. These include:

* Known phishing keyword patterns
* Suspicious domain structures
* Common obfuscation patterns

This hybrid approach improves detection reliability by combining ML prediction with rule-based safeguards.

---

### `data_validation.py`

Ensures dataset and extracted features are valid before training or inference. It checks:

* Missing values
* Incorrect feature formats
* Invalid URL structures

This prevents corrupted data from affecting model performance.

---

### `clientServer.php`

Acts as a lightweight server-side interface (if used in testing or logging). It may:

* Log detected threats
* Store classification results
* Serve as a bridge for analytics or debugging

---

# 5. Testing & Utility Scripts (tst/, test.py)

### `tst/features_extraction.py`

A testing version of the feature extraction pipeline used to validate:

* Feature consistency
* Extraction correctness
* Edge cases in URL parsing

### `test.py`

Used to evaluate the trained model on unseen data. It:

* Loads `random_forest.pkl`
* Runs predictions on test samples
* Computes accuracy, precision, recall

This ensures the model generalizes well beyond training data.

---

# 6. Documentation (docs/)

### `CODE_OF_CONDUCT.md`

Defines project collaboration standards, ethical usage, and contribution guidelines.

### `Troubleshooting.md`

Provides solutions for common issues such as:

* Extension not loading
* Model prediction errors
* Feature extraction failures
* Permission issues in Chrome

---

# 7. Configuration & Dependencies

### `requirements.txt`

Lists all Python dependencies required for training and feature extraction, such as:

* scikit-learn
* pandas
* numpy
* scipy

---

### `_config.yml`

Configuration file used for documentation or deployment (likely GitHub Pages). It may define:

* Site theme
* Metadata
* Build settings

---

### `license`

Defines legal usage terms for the project.

---

# Design Choices

A key architectural decision was separating the system into **browser-side detection (extension)** and **offline ML training (Python pipeline)**. This ensures that the browser extension remains lightweight and does not require heavy computation.

The Random Forest model was chosen after evaluating multiple classifiers because it provides a strong balance between accuracy and runtime efficiency. Deep learning models were considered but rejected due to latency and browser deployment limitations.

Another important decision was adopting a **hybrid detection strategy**, combining:

* Machine learning predictions
* Rule-based pattern detection (`patterns.py`)

This improves robustness against adversarial URL structures that may confuse pure ML models.

---

# Limitations

While IntelliShield Core provides strong protection against phishing URLs, it has some limitations:

* It primarily analyzes URL-based features and not full webpage content
* It cannot deeply inspect encrypted scripts or dynamic runtime behavior
* Performance depends on quality of training dataset

---

# Future Improvements

Planned enhancements include:

* Real-time cloud threat intelligence integration
* Deep learning-based URL embedding models
* Browser DOM behavior analysis
* Multi-browser support (Firefox, Edge)
* Improved dataset expansion and adversarial training

---

# Conclusion

IntelliShield Core demonstrates a practical implementation of machine learning in cybersecurity, combining Python-based model training with a real-time Chrome extension. The system shows how lightweight ML models, when paired with effective feature engineering and browser integration, can provide adaptive protection against phishing threats in modern web environments.
