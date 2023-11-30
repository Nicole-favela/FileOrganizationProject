import argparse
import os

from datetime import datetime
import shutil


def get_date(path):
    creation_date = os.path.getctime(path)
    return datetime.fromtimestamp(creation_date)

#TODO: group by date
def create_folders(source_folder, target, extensions, months):
   
    for root, directories, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(tuple(extensions)): #check file extensions
                file_path = os.path.join(root, file)
                created_at = get_date(file_path)
                print("the file: ", file ,"was created at: ", created_at)
               

def main():
    parser = argparse.ArgumentParser(description="Organize files by date.")
    parser.add_argument("source_folder", help="Path to the folder to organize.")
    parser.add_argument("target_folder", help="Path to the target folder where the organized folders will be created (can be the same as source).")
    parser.add_argument("--extensions", nargs="+", default=["jpg", "png", "jpeg"],
                        help="File extensions to organize. Default are jpg, png, and jpeg.")
    parser.add_argument("--months", type=int, default=12,
                        help="Organize files created in the past N months.")
    

    args = parser.parse_args()
    create_folders(args.source_folder, args.target_folder, args.extensions, args.months)
if __name__ == "__main__":
    main()