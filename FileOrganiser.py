import os
import shutil

# Dictionary mapping file types to folder names
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css'],
}

# Function to create folders based on file types
def create_folders(directory):
    for folder in file_types.keys():
        path = os.path.join(directory, folder)
        if not os.path.exists(path):
            os.makedirs(path)

# Function to move files to appropriate folders
def move_file(filepath, directory):
    file_extension = os.path.splitext(filepath)[1].lower()
    for folder, extensions in file_types.items():
        if file_extension in extensions:
            destination = os.path.join(directory, folder, os.path.basename(filepath))
            shutil.move(filepath, destination)
            print(f"Moved: {filepath} -> {destination}")
            break

# Function to organize files in the given directory
def organize_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            move_file(filepath, directory)

# Main function to run the program
def main():
    directory = input("Enter the directory to organize: ")
    if os.path.exists(directory) and os.path.isdir(directory):
        create_folders(directory)
        organize_files(directory)
        print("Files have been organized successfully!")
    else:
        print("Invalid directory. Please try again.")

if _name_ == "_main_":
    main()
