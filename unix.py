import os
import json
import time
import sys
from datetime import datetime, timezone

def modify_time(file_path, timestamp):
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    atime = os.stat(file_path).st_atime
    os.utime(file_path, (atime, time.mktime(dt.timetuple())))

def get_timestamp(data):
    if 'photoTakenTime' in data and 'timestamp' in data['photoTakenTime']:
        return int(data['photoTakenTime']['timestamp'])
    elif 'created' in data:
        dt = datetime.strptime(data['created'], "%Y-%m-%dT%H:%M:%S.%fZ")
        return int(dt.timestamp())
    else:
        raise KeyError("No valid timestamp found in JSON data")

def process_file(directory, filename):
    json_path = os.path.join(directory, f"{filename}.json")
    jpg_path = os.path.join(directory, filename)
    
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r') as json_file:
                data = json.load(json_file)
                timestamp = get_timestamp(data)
                modify_time(jpg_path, timestamp)
                print(f"Updated {jpg_path} with timestamp {timestamp}")
            
            os.remove(json_path)
            print(f"Removed {json_path}")
        except Exception as e:
            print(f"Failed to process {json_path}: {e}")

def process_directory(directory, recursive=False):
    for root, _, files in os.walk(directory):
        for filename in files:
            if not filename.lower().endswith('.json'):
                process_file(root, filename)
        if not recursive:
            break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python unix.py <directory_path1> <directory_path2> ...")
    else:
        recursive = input("Do you want to search all subdirectories? (y/n): ").strip().lower() == 'y'
        
        for directory in sys.argv[1:]:
            if os.path.isdir(directory):
                process_directory(directory, recursive)
            else:
                print(f"The path '{directory}' is not a valid directory.")
