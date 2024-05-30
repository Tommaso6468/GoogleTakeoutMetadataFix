import os
import json
import sys
from datetime import datetime
import win32file
import win32con

def modify_time(file_path, timestamp):
    dt = datetime.utcfromtimestamp(timestamp)
    handle = win32file.CreateFile(file_path, win32file.GENERIC_WRITE, 0, None, win32con.OPEN_EXISTING, win32con.FILE_ATTRIBUTE_NORMAL, None)
    win32file.SetFileTime(handle, dt, None, None)
    handle.close()

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
        print("Usage: python windows.py <directory_path1> <directory_path2> ...")
    else:
        for directory in sys.argv[1:]:
            if os.path.isdir(directory):
                process_directory(directory)
            else:
                print(f"The path '{directory}' is not a valid directory.")
