import os
import shutil

# Define the directory to organize
directory_to_organize = "path/to/your/directory"

# Define the file types and corresponding folder names
file_types = {
    ".txt": "Text Files",
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "PDF Files",
    ".docx": "Documents"
}

def organize_files(directory):
    # Scan through all files in the directory
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                file_ext = os.path.splitext(entry.name)[1]  # Get the file extension
                folder_name = file_types.get(file_ext)  # Check if the extension is in the dictionary
                
                if folder_name:
                    folder_path = os.path.join(directory, folder_name)
                    
                    try:
                        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
                    except OSError as e:
                        print(f"Error creating directory {folder_path}: {e}")
                    
                    # Move the file to the corresponding folder
                    try:
                        shutil.move(entry.path, folder_path)
                        print(f"Moved {entry.name} to {folder_path}")
                    except shutil.Error as e:
                        print(f"Error moving file {entry.name}: {e}")

if __name__ == "__main__":
    organize_files(directory_to_organize)
