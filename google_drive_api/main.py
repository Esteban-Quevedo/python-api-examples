# -*- coding: utf-8 -*-

from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = "PUT YOUR PARENT FOLDER ID HERE"


def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
    return creds


def upload_file(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': "Test Name",
        'parents': [PARENT_FOLDER_ID]

    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()

    return file


if __name__ == "__main__":
    result = upload_file('test-file.pdf')
    print(f'File {result['name']} was upload successfully.')
