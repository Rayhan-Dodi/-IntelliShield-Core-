# 🛡️ IntelliShield Core  

A machine learning-powered Chrome extension designed to help users detect and avoid malicious websites before interacting with them.

---

## ⚠️ Notes  
1. If you face any issues, first refer to [Troubleshooting.md](docs/Troubleshooting.md).  
   If the problem persists, please open an issue using the appropriate template (Bug Report, Question, Feature Request, or Custom Issue).  
2. Please support the project by giving it a ⭐.

---

## 🚀 Steps to Run the Project  

### 1. Install Dependencies  
Install all required packages:
```bash
pip install -r requirements.txt
````

Verify your pip version:

```bash
pip -V
```

---

### 2. Setup Local Environment

* Move the project folder to your localhost directory
  **Example (Mac):**

  ```
  /Library/WebServer/Documents
  ```

* **Mac Users Only:**
  Grant write permission:

  ```bash
  sudo chmod 777 markup.txt
  ```

---

### 3. Configuration

* Update Python 2.x path in:

  ```
  clientServer.php
  ```

* If you are **not using macOS**, update localhost path in:

  ```
  features_extraction.py
  ```

---

### 4. Load Chrome Extension

1. Go to:

   ```
   chrome://extensions
   ```
2. Enable **Developer Mode**
3. Click **Load Unpacked**
4. Select the `Extension` folder

---

### 5. Run the Extension

* Open any website
* Click the extension icon (top-right corner)
* Click **"Safe or Not?"**
* Wait for the result

✅ Done!

---

## 📄 Research Paper

[http://ieeexplore.ieee.org/document/8256834/](http://ieeexplore.ieee.org/document/8256834/)

---

## 🧠 Abstract

* Most users are unaware of the backend risks of websites.
* Malicious pages can trick users into sharing credentials or downloading harmful content.

This project introduces a **Chrome extension** that acts as a middleware layer between users and potentially harmful websites.

Unlike traditional methods that rely only on known blacklists, this system uses **Machine Learning** to:

* Analyze website behavior dynamically
* Detect new and unknown threats
* Classify web content in real-time

This ensures continuous protection against evolving cyber threats.

---

## 🎥 Demo

[Watch Demo](https://youtu.be/0-wky0h3hmM)

---

## 📸 Screenshots

### ✔️ Safe Website  
![safe_website](https://drive.google.com/uc?export=view&id=1_azuPW3WjV873WeVRlTTIgZjQSn_KkeG)  
_**Fig 1.** Safe website detected by IntelliShield Core_ - [www.spit.ac.in](http://www.spit.ac.in) (College website)*

---
### ⚠️ Phishing Website (Google Drive Clone)  
![drive_phishing](https://drive.google.com/uc?export=view&id=1jXs5r0h3TxVW1TuT0NflrJ5RPEFGzT2Y)  
_**Fig 2.** A phishing website mimicking Google Drive._
---

### ⚠️ Phishing Website (Dropbox Clone)  
![dropbox_phishing](https://drive.google.com/uc?export=view&id=1xaLXTqR4UmApJAxzQm8_W68Yn0kDCr51)  
_**Fig 3.** A phishing website mimicking Dropbox._

---

### ✔️ Safe Website

![moodle_safe](https://drive.google.com/uc?export=view&id=1pWKtJeMEeH1zimAVxLdMT6g-J6a_xf1M)  
***Fig 4.** A safe website. - [www.google.com](http://www.google.com)*

---

## 💡 Key Features

* 🔐 Real-time malicious website detection
* 🤖 Machine Learning-based classification
* 🌐 Chrome Extension integration
* ⚡ Fast and lightweight analysis

---

## 📌 Future Improvements

* Upgrade to Python 3.x
* Improve model accuracy with deep learning
* Deploy as a cloud-based API
* Enhance extension UI/UX

---

## 📜 License

This project is licensed under the MIT License.

```
