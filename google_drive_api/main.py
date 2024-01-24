# -*- coding: utf-8 -*-
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_KEY_FILE = 'service_account.json'
PARENT_FOLDER_ID = "PUT_YOUR_PARENT_FOLDER_ID_HERE"


def authenticate_google_drive():
    """
    Authenticate with Google Drive using the provided service account key credentials.

    Returns:
        googleapiclient.discovery.Resource: The Google Drive service resource.
    """
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY_FILE)
    drive_service = build('drive', 'v3', credentials=credentials)
    return drive_service


def upload_file_to_google_drive(file_path):
    """
    Upload a file to Google Drive.

    Args:
        file_path (str): The path to the file to be uploaded.

    Returns:
        dict: Information about the uploaded file.
    """
    drive_service = authenticate_google_drive()

    file_metadata = {
        'name': "Test Name",
        'parents': [PARENT_FOLDER_ID]
    }

    media_body = file_path

    # Upload the file to the specified parent folder on Google Drive
    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media_body
    ).execute()

    return uploaded_file


if __name__ == "__main__":
    file_to_upload = 'test-file.pdf'
    result = upload_file_to_google_drive(file_to_upload)
    print(f'File "{result["name"]}" was uploaded successfully to Google Drive.')
