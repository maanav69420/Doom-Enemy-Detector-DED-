
import os
import random
from pathlib import Path
import shutil

# ||=============[ This program takes an image from a directory and transfers it to a new directory ]=============||

# ||=======[ Function to extract directory name from the path and create a new directory if it doesn't exist ]=======||
def extract_dir_name(current_root, dest):
    dir_name = os.path.basename(current_root)
    dest_dir = os.path.join(dest, dir_name)

    if not os.path.exists(dest_dir):  # Check if the destination directory exists
        os.makedirs(dest_dir)  # Create the directory if it doesn't exist

    return dir_name

# ||=======[ Function to randomly choose files from a list and mark them for transfer ]=======||
def random_choice(percent, get_item):
    # Convert get_item to a list to allow random.choice to work with it
    get_item_list = list(get_item)
    file_dict = {file_name: 0 for file_name in get_item_list if os.path.isfile(os.path.join(roots[counter], file_name))}
    
    total_files_to_pick = (percent * len(get_item_list)) // 100
    pick = 0
    random.seed(9)  # Setting seed for reproducibility

    while pick < total_files_to_pick:
        random_file = random.choice(get_item_list)  # Choose randomly from the list, not set
        if file_dict.get(random_file, 0) > 0:
            continue
        else:
            file_dict[random_file] += 1
            pick += 1

    return file_dict


# Main directory containing images
main = os.path.join(r"E:\enemies")
dest = os.path.join(r"Doom-Enemy-Detector-DED-\enemies\selective-dataset")

# Create destination directory if it doesn't exist
if not os.path.exists(dest):
    print(f"Creating destination directory: {dest}")
    os.makedirs(dest)

# Check if the main directory exists and get subdirectories
if os.path.exists(main) and os.path.isdir(main):
    print(f"Main directory found: {main}")
    roots = [root for root, _, _ in os.walk(main)]
    if roots:  # Ensure roots is not empty before trying to pop
        roots.pop(0)  # Remove the main directory from the list
    else:
        print("No subdirectories found in the main directory.")
        roots = []  # Initialize an empty list if no subdirectories are found
else:
    print(f"Error: The main directory '{main}' does not exist.")
    roots = []

counter = 0

# ||=======[ Loop through each subdirectory ]=======||
while counter < len(roots):
    dir_name = extract_dir_name(roots[counter], dest)

    # Get the list of files in source and destination directories
    src_list_dir = set(os.listdir(roots[counter]))
    dest_list_dir = set(os.listdir(os.path.join(dest, dir_name)))
    get_item = src_list_dir - dest_list_dir  # Files that are only in the source

    if not get_item:
        print(f"No new files found in {roots[counter]}")
        counter += 1
        continue

    percent = int(input(f"How much percent of images from {roots[counter]} to transfer? "))

    # Get a dictionary of files to transfer
    file_dict = random_choice(percent, get_item)
    file_dict = [file for file, count in file_dict.items() if count > 0]  # Files to be transferred

    # Transfer files based on percentage
    if percent <= 50:
        # If percentage is less than or equal to 50%, transfer files directly
        for file_name in file_dict:
            print(f"Transferring {file_name} to {dir_name}")
            src_path = Path(roots[counter]) / file_name
            dest_path = Path(dest) / dir_name / file_name
            shutil.copy(src_path, dest_path)
    else:
        # If percentage is more than 50%, use two pointers method
        left, right = 0, len(file_dict) - 1
        mid = (left + right) // 2
        directions = [left, right]

        while directions[0] < mid and directions[1] > mid:
            for point in directions:
                file_name = file_dict[point]
                print(f"Transferring {file_name} to {dir_name}")
                src_path = Path(roots[counter]) / file_name
                dest_path = Path(dest) / dir_name / file_name
                shutil.copy(src_path, dest_path)

            directions[0] += 1
            directions[1] -= 1

        # Transfer the middle file
        mid_file_name = file_dict[mid]
        print(f"Transferring {mid_file_name} to {dir_name}")
        src_path = Path(roots[counter]) / mid_file_name
        dest_path = Path(dest) / dir_name / mid_file_name
        shutil.copy(src_path, dest_path)

    counter += 1
