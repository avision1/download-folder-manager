import os
import shutil


def get_user_confirmation(message):
    """Prompts the user for confirmation and returns True/False"""
    response = input(message + " (y/n): ").lower()
    return response == 'y'


download_folder = 'C:\\Users\\<user>\\Downloads'
file_list = []

with os.scandir(download_folder) as entries:
    for entry in entries:
        file_info = {
            'ext': os.path.splitext(entry.name)[1],
            'last_modified': os.path.getmtime(entry.path),
            'filepath': entry.path,
            'filename': entry.name
        }
        file_list.append(file_info)

for file in file_list:
    print(file['filename'])

    destination_folder = os.path.join('E:\\Downloads', file['ext'])
    os.makedirs(destination_folder, exist_ok=True)  # Create folder if needed

    destination = os.path.join(destination_folder, file['filename'])

    # Check if file already exists
    if os.path.exists(destination):
        if not get_user_confirmation(f"File '{file['filename']}' already exists. Overwrite?"):
            continue  # Skip to next file if user doesn't confirm overwrite

    # Move the file
    shutil.move(file['filepath'], destination)
    print(f"Moved '{file['filename']}' to {destination_folder}")
