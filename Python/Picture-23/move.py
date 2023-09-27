import os
import shutil

# Define the base folder where you want to create subfolders
base_folder = 'C:\\Users\\anali\\OneDrive\\Documents\\Picture-23'

# Create subfolders if they don't exist
for i in range(1, 9):  # Create 8 subfolders
    subfolder = os.path.join(base_folder, f'folder_{i}')
    os.makedirs(subfolder, exist_ok=True)

# Move the images into the subfolders
for i in range(1, 51):  # Assuming you have 50 images
    source_file = os.path.join(base_folder, f'analia_{i}.jpg')
    destination_folder = os.path.join(base_folder, f'folder_{i % 8 + 1}')
    destination_file = os.path.join(destination_folder, f'analia_{i}.jpg')
    
    # Check if the file exists before moving
    if os.path.isfile(source_file):
        shutil.move(source_file, destination_file)
