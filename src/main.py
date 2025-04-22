from textnode import *
from converter import generate_page, generate_pages_rec
import os
import shutil

from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_rec("content", "template.html", "public")


main()
