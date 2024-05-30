import os
import json
import time
import sys
from datetime import datetime

def modify_time(file_path, timestamp):
    dt = datetime.utcfromtimestamp(timestamp)
    atime = os.stat(file_path).st_atime
    os.utime(file_path, (atime, time.mktime(dt.timetuple())))

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            json_path = os.path.join(directory, f"{filename}.json")
            jpg_path = os.path.join(directory, filename)
            
            if os.path.exists(json_path):
                with open(json_path, 'r') as json_file:
                    data = json.load(json_file)
                    timestamp = int(data['photoTakenTime']['timestamp'])
                    modify_time(jpg_path, timestamp)
                    
                    print(f"Updated {jpg_path} with timestamp {timestamp}")
                os.remove(json_path)
                print(f"Removed {json_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python unix.py <directory_path1> <directory_path2> ...")
    else:
        for directory in sys.argv[1:]:
            if os.path.isdir(directory):
                process_directory(directory)
            else:
                print(f"The path '{directory}' is not a valid directory.")
