# 🚀 AutoCloud-Organizer
**An Intelligent, Category-Aware Cloud Ingestion Engine**

AutoCloud-Organizer is a Python-powered automation tool that streamlines cloud storage organization. It intelligently sorts local files into categorized Google Drive directories (Documents, Images, Videos) during the upload process, ensuring a structured remote environment.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Security: Least Privilege](https://img.shields.io/badge/Security-Least%20Privilege-green.svg)](https://en.wikipedia.org/wiki/Principle_of_least_privilege)

---

## DEMO:


![autodrive](https://github.com/user-attachments/assets/7ec74087-6f58-4d47-bda2-7b0520bbcd4b)


---


## 🏗️ Engineering Highlights (DevOps & Security)
* **Idempotent Folder Logic:** The script checks for the existence of category folders before creation, preventing duplicate resource bloat in the cloud.
* **Least Privilege Access:** Implements the `drive.file` OAuth scope, ensuring the application only accesses files it creates—a key cybersecurity best practice.
* **Batch Processing:** Engineered to handle multiple file selections in a single execution via a native OS GUI.
* **Resiliency:** Includes defined request timeouts to handle network latency during large batch uploads.

---

## ✨ Features
* **Automatic Categorization:** Routes files based on extensions (e.g., `.pdf` to Documents, `.mp4` to Videos).
* **Native UI Integration:** Uses `tkinter` for a seamless file selection experience.
* **Detailed Reporting:** Provides a post-upload summary in the CLI showing file distribution.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **APIs:** Google Drive API v3
* **Auth:** OAuth 2.0 (Installed App Flow)

---

## 🔑 Google Cloud Setup (Acquiring cre.json)
To enable the automation engine, you must configure a Google Cloud Project and generate an OAuth 2.0 Desktop Client key.

1. Project Initialization
Navigate to the Google Cloud Console.

Create a New Project named CloudBridge-Ops.

Go to APIs & Services > Library, search for Google Drive API, and click Enable.

2. Configure OAuth Consent
Go to APIs & Services > OAuth consent screen.

Select External and fill in the required App Name and Support Email.

Crucial Scope: Under "Scopes," manually add https://www.googleapis.com/auth/drive.file. This ensures the app follows the Principle of Least Privilege.

Add your own email under Test Users to allow development access.

3. Generate Credentials
Go to APIs & Services > Credentials.

Click Create Credentials > OAuth client ID.

Select Application type: Desktop App and click Create.

Download the JSON file and move it to the root of this project.

Rename the file to cre.json to match the application's source code.

[!CAUTION]
Security Warning: The cre.json contains your private client secret. Never commit this file to GitHub. Ensure your .gitignore is active before pushing.

---

## ⚙️ Setup & Installation
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/Moseskenny/AutoCloud-Organizer.git](https://github.com/Moseskenny/AutoCloud-Organizer.git)
   cd AutoCloud-Organizer

## 📜 License

MIT License

---

## 👤 Author

**Moses Kenny** *Cloud & DevOps Enthusiast | Python Developer* [GitHub](https://github.com/moseskenny) | [LinkedIn](https://linkedin.com/in/moses-kenny)

---

## ⭐ Support

If you like this project, please ⭐ the repository!
