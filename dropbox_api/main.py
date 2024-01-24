# -*- coding: utf-8 -*-
import dropbox

# Replace this with your Dropbox access token
DROPBOX_TOKEN = 'REPLACE_THIS_WITH_YOUR_TOKEN'


def authenticate_dropbox():
    """
    Authenticate with Dropbox using the provided access token.

    Returns:
        Dropbox: The Dropbox client object.
    """
    dropbox_client = dropbox.Dropbox(DROPBOX_TOKEN)
    return dropbox_client


def upload_file_to_dropbox(file_path):
    """
    Upload a file to Dropbox.

    Args:
        file_path (str): The path to the file to be uploaded.

    Returns:
        dropbox.files.FileMetadata: Information about the uploaded file.
    """
    client = authenticate_dropbox()

    with open(file_path, 'rb') as file:
        file_data = file.read()

    file_name = file_path.split("/")[-1]  # Extract the file name from the file path

    # Upload the file to the root directory on Dropbox
    uploaded_file = client.files_upload(file_data, f'/{file_name}')

    return uploaded_file


if __name__ == "__main__":
    file_to_upload = 'test-file.pdf'
    result = upload_file_to_dropbox(file_to_upload)
    print(f'File "{result.name}" was uploaded successfully to Dropbox.')
