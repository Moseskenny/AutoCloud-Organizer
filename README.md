# 🚀 AutoCloud-Organizer
**An Intelligent, Category-Aware Cloud Ingestion Engine**

AutoCloud-Organizer is a Python-powered automation tool that streamlines cloud storage organization. It intelligently sorts local files into categorized Google Drive directories (Documents, Images, Videos) during the upload process, ensuring a structured remote environment.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Security: Least Privilege](https://img.shields.io/badge/Security-Least%20Privilege-green.svg)](https://en.wikipedia.org/wiki/Principle_of_least_privilege)

## 🏗️ Engineering Highlights (DevOps & Security)
* **Idempotent Folder Logic:** The script checks for the existence of category folders before creation, preventing duplicate resource bloat in the cloud.
* **Least Privilege Access:** Implements the `drive.file` OAuth scope, ensuring the application only accesses files it creates—a key cybersecurity best practice.
* **Batch Processing:** Engineered to handle multiple file selections in a single execution via a native OS GUI.
* **Resiliency:** Includes defined request timeouts to handle network latency during large batch uploads.

## ✨ Features
* **Automatic Categorization:** Routes files based on extensions (e.g., `.pdf` to Documents, `.mp4` to Videos).
* **Native UI Integration:** Uses `tkinter` for a seamless file selection experience.
* **Detailed Reporting:** Provides a post-upload summary in the CLI showing file distribution.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **APIs:** Google Drive API v3
* **Auth:** OAuth 2.0 (Installed App Flow)

## ⚙️ Setup & Installation
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/Moseskenny/AutoCloud-Organizer.git](https://github.com/Moseskenny/AutoCloud-Organizer.git)
   cd AutoCloud-Organizer
