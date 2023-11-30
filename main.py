import os
import re
import datetime
import shutil

EXTENSTIONS = ("jpg", "png") #extensions of interest
 
# files = os.listdir(source) #lists all files in that folder

#regex for year and month. (yr)-(mo)-(day)
# DATE_MATCH = '.*(20\d\d)-?([01]\d)-?([0123]\d).*'
def get_date(path):
    creation_date = os.path.getctime(path)
    return datetime.fromtimestamp(creation_date)
def create_folders(script_folder, target, EXTENSIONS):
    return ''
script_folder = os.path.dirname(os.path.abspath(__file__))
target_folder = 'PythonFileAutomationTest1'
 
# create_folders(script_folder, target_folder,EXTENSTIONS)