import argparse
import os

from datetime import datetime, timedelta
import shutil


def get_date(path):
    mod_date = os.path.getmtime(path)
    return datetime.fromtimestamp(mod_date)

#TODO: create folders by date
def create_folders(source_folder, target, extensions, months):
    n_months = datetime.now() - timedelta(days=months *30.44) #get the time n months ago in number of months
   
    for root, directories, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(tuple(extensions)): #check file extensions
                file_path = os.path.join(root, file)
                mod_date  = get_date(file_path)
               
                if mod_date  >=n_months: 
                    print("less than ",months, " months old: ", file, 'modified at: ', mod_date)
               
#months and extensions are optional
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