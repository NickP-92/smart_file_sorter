import os
import shutil
import argparse

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def get_category(extension):
    for category, exts in FILE_TYPES.items():
        if extension.lower() in exts:
            return category
    return "Other"    
    
def sort_files(folder):
    with open("log.txt", "a") as log:
        for file in os.listdir(folder):
            file_path = os.path.join(folder,file)
            if os.path.isfile(file_path):
                name, ext = os.path.splitext(file)
                category = get_category(ext)
                dest_folder = os.path.join(os.path.join(folder,category))
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder,file))
                log.write(f"Moved {file} -> {category} /\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort files by type.")
    parser.add_argument("folder", help="Folder path to sort")
    args = parser.parse_args()
    sort_files(args.folder)