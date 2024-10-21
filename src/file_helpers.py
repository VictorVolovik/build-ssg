import os

def create_folder(path):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as err:
            raise Exception("Failed to create new folder:", path, err)
