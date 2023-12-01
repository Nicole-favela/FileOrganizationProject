import argparse
import os
from datetime import datetime, timedelta
import shutil


def get_date(path):
    mod_date = os.path.getmtime(path) #get file modification date
    return datetime.fromtimestamp(mod_date)

#iterates files and creates folders grouped by date
def create_folders(source_folder, target, extensions, months):
    n_months = datetime.now() - timedelta(days=months * 30.44) #get the time n months ago in number of months
   
    #iterate root: full path to source folder
    for root, directories, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(tuple(extensions)): #check file extensions
                file_path = os.path.join(root, file) # the path root/file
                mod_date  = get_date(file_path)
               
                if mod_date  >=n_months: #only grab last n months files
                   
                    #create folder name with year and month
                    folder_name = mod_date.strftime('%Y-%m')
                    #create target folder path where the files will be grouped
                    folder_path = os.path.join(target, folder_name)
                 
                    #make directory if path doesn't exist
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
                    #create destination path: full/path/Y-M/movedfile 
                    dest_path = os.path.join(folder_path, file)
                    move_files(file_path, dest_path)

                 
def move_files(file_path_of_src, file_path_of_dest):
     #move source (file_path: original location) into dest_path
    shutil.move(file_path_of_src, file_path_of_dest)

#months and extensions are optional, but have defaults
def main():
    parser = argparse.ArgumentParser(description="Organize files by date and file types.")
    parser.add_argument("source_folder", help="Path to the folder to organize.")
    parser.add_argument("target_folder", help="Path to the target folder where the organized folders will be created (can be the same as source).")
    parser.add_argument("--extensions", nargs="+", default=["jpg", "png"],
                        help="File extensions to organize. Default are jpg, png")
    parser.add_argument("--months", type=int, default=12,
                        help="Organize files created in the past N months.")
    

    args = parser.parse_args()
    create_folders(args.source_folder, args.target_folder, args.extensions, args.months)
if __name__ == "__main__":
    main()