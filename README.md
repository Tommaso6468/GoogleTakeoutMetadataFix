# Google Photos & Drive Takeout Metadata Fix

![Python](https://img.shields.io/badge/Python-3)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Unix-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

This simple Python script helps you clean up your Google Photos/Drive export by updating the creation time of your files to the original creation time from the JSON files. Tt removes the JSON files after processing. Additionally, the script can search all directories within the given directory if you want. Other information in the JSON files is now discarded, maybe in the future I'll implement all the other data.

### Issues with Google Drive cleaning
If you pass a Google Drive takeout directory, it sometimes doesn't work for all of the files. This is because sometimes the filenames of the JSON files are quite different compared to the original file. You can try to add some specific patterns to the `process_file` function in the array `json_paths`.

## Prerequisites

- Python 3 or higher
- `pywin32` library for Windows file time modification (Windows only)

## Installation

### Step 1: Clone the repository

```sh
git clone https://github.com/Tommaso6468/GooglePhotosTakeoutMetadataFix.git
cd GooglePhotosTakeoutMetadataFix
```
### Step 2: Install dependencies (Windows only)
```sh
pip install pywin32
```

## Usage

### Command line arguments
The script accepts multiple directories as arguments. Each directory should contain the JPG files and their corresponding JSON metadata files.

### Example command
```sh
python windows.py "/path/to/your/photos1" "/path/to/your/photos2"
```

### Script execution
1. Open a terminal or command prompt
2. Navigate to the directory where you cloned the repository
3. Run the script for your OS with the desired directories as arguments

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
