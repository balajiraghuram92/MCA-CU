import os
import shutil

def move_and_overwrite(src_folder, dest_folder):
    # Ensure the source folder exists
    if not os.path.exists(src_folder):
        print(f"Source folder '{src_folder}' does not exist.")
        return

    # Ensure the destination folder exists, create if it doesn't
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Iterate over all files and directories in the source folder
    for item in os.listdir(src_folder):
        src_path = os.path.join(src_folder, item)
        dest_path = os.path.join(dest_folder, item)

        # Move the item, overwriting if it exists
        if os.path.isdir(src_path):
            # If it's a directory, use shutil.move
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)
            shutil.move(src_path, dest_path)
        else:
            # If it's a file, use shutil.move
            if os.path.exists(dest_path):
                os.remove(dest_path)
            shutil.move(src_path, dest_path)

    print(f"All contents moved from '{src_folder}' to '{dest_folder}'.")

# Example usage
src_folder = '/home/root-php/MCA-CU/PHP'
dest_folder = '/var/www/html'
move_and_overwrite(src_folder, dest_folder)

