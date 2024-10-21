import os
import shutil

from file_helpers import create_folder


def prepare_static_files():
    print("Preparing static files...")

    clear_old_files()
    copy_all_static()

    print("Static files are ready to use!")


def clear_old_files():
    if os.path.exists("./public"):
        try:
            print("Clearing up old files...")
            shutil.rmtree("./public")
        except Exception as err:
            raise Exception("Failed to clear old files:", err)


def copy_all_static():
    print("Copying files and folders to /public...")
    create_folder("public")
    copy_files("./static", "./public")


def copy_files(src, dst):
    dir = os.listdir(src)
    for path in dir:
        path_src = os.path.join(src, path)
        path_dst = os.path.join(dst, path)
        if os.path.isfile(path_src):
            try:
                print(f"Copying file {path_src} to {path_dst}...")
                shutil.copy(path_src, path_dst)
            except Exception as err:
                raise Exception("Failed to copy file:", path_src, err)
        else:
            print(f"Creating folder {path_src} at {dst}")
            create_folder(path_dst)
            copy_files(path_src, path_dst)
