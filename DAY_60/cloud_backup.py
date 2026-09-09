# Day 60 - Google Drive Backup

from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive.file"]
CREDENTIALS_FILE = Path("credentials/credentials.json")
TOKEN_FILE = Path("credentials/token.json")

BACKUP_FOLDER_NAME = "Personal Diary Backup"

def authenticate_google_drive():
    """Authenticate with Google Drive."""
    credentials = None
    if TOKEN_FILE.exists():
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                raise FileNotFoundError("Google credentials.json was not found.")
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(TOKEN_FILE, "w") as token:
            token.write(credentials.to_json())

    return build("drive", "v3", credentials=credentials)

def get_backup_folder(service):
    """Find or create the diary backup folder."""
    query = (
        "name = 'Personal Diary Backup' "
        "and mimeType = 'application/vnd.google-apps.folder' "
        "and trashed = false"
    )

    results = service.files().list(q=query, spaces="drive", fields="files(id, name)").execute()
    folders = results.get("files", [])
    if folders:
        return folders[0]["id"]

    folder_metadata = {"name": BACKUP_FOLDER_NAME, "mimeType": "application/vnd.google-apps.folder"}
    folder = service.files().create(body=folder_metadata, fields="id").execute()
    return folder["id"]

def backup_entries():
    """Upload encrypted diary entries to Google Drive."""
    from diary_manager import get_entries

    entries = get_entries()
    if not entries:
        return 0

    service = authenticate_google_drive()
    folder_id = get_backup_folder(service)
    uploaded = 0

    for entry in entries:
        file_metadata = {"name": entry.name, "parents": [folder_id]}
        media = MediaFileUpload(str(entry), mimetype="application/octet-stream")
        service.files().create(body=file_metadata, media_body=media, fields="id").execute()
        uploaded += 1
    return uploaded

def restore_entries():
    """Download encrypted diary entries from Google Drive."""
    from diary_manager import ENTRIES_FOLDER

    service = authenticate_google_drive()
    folder_id = get_backup_folder(service)
    query = (
        f"'{folder_id}' in parents "
        "and trashed = false"
    )

    results = service.files().list(q=query, spaces="drive", fields="files(id, name)").execute()
    files = results.get("files", [])
    ENTRIES_FOLDER.mkdir(parents=True, exist_ok=True)
    restored = 0

    for item in files:
        file_path = ENTRIES_FOLDER / item["name"]
        request = service.files().get_media(fileId=item["id"])

        with open(file_path, "wb") as file:
            downloader = MediaIoBaseDownload(file, request)
            done = False

            while not done:
                _, done = downloader.next_chunk()
        restored += 1
    return restored

# Done