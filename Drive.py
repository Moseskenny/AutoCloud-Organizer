import os
import tkinter as tk
from tkinter import filedialog
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload, HttpRequest

# OAuth 2.0 scope
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Main Drive folder where categorized folders will be created
MAIN_FOLDER_ID = 'Enter_your_folder_id_here'

# Mapping extensions to categories
CATEGORIES = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'Others': []  # Any file type not matched above
}

def authenticate():
    
    flow = InstalledAppFlow.from_client_secrets_file('cre.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def select_files():
    
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames()
    return file_paths

def get_category(file_path):
    
    ext = os.path.splitext(file_path)[1].lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return 'Others'

def get_or_create_folder(service, folder_name, parent_id):
    
    query = f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and '{parent_id}' in parents"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    items = results.get('files', [])
    if items:
        return items[0]['id']
    # Folder doesn't exist, create it
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    folder = service.files().create(body=file_metadata, fields='id').execute()
    return folder.get('id')

def upload_file(service, file_path, parent_id):
    """Upload a single file to the specified Google Drive folder."""
    filename = os.path.basename(file_path)
    media = MediaFileUpload(file_path, resumable=False)
    file_metadata = {
        'name': filename,
        'parents': [parent_id]
    }
    try:
        file = service.files().create(body=file_metadata, media_body=media).execute()
        print(f"Uploaded '{filename}' to folder ID {parent_id} (File ID: {file.get('id')})")
    except Exception as e:
        print(f"An error occurred while uploading '{filename}': {e}")

def upload():
    
    file_paths = select_files()
    if not file_paths:
        print("No files selected.")
        return

    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    summary = {}

    for file_path in file_paths:
        category = get_category(file_path)
        folder_id = get_or_create_folder(service, category, MAIN_FOLDER_ID)
        upload_file(service, file_path, folder_id)
        summary.setdefault(category, []).append(os.path.basename(file_path))

    print("\nUpload Summary:")
    for cat, files in summary.items():
        print(f"{cat} ({len(files)} files): {', '.join(files)}")

if __name__ == "__main__":
    HttpRequest.timeout = 300
    upload()
