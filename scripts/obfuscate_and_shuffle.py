import os
import random
import string

# Function to generate a random filename
def generate_random_filename(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Function to obfuscate filenames and shuffle them in a given directory
def obfuscate_and_shuffle_images(directory):
    files = os.listdir(directory)
    
    # Filter to include only image files
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.JPEG'))]
    
    # Shuffle the image files
    random.shuffle(image_files)
    
    # Obfuscate filenames
    for file_name in image_files:
        # Generate a new random filename
        new_name = generate_random_filename() + os.path.splitext(file_name)[1]
        # Rename the file
        os.rename(os.path.join(directory, file_name), os.path.join(directory, new_name))
        print(f"Renamed {file_name} to {new_name}")

# Function to recursively obfuscate and shuffle all images in subdirectories
def obfuscate_and_shuffle_recursive(root_directory):
    for subdir, _, _ in os.walk(root_directory):
        # Process each subdirectory containing images
        obfuscate_and_shuffle_images(subdir)

if __name__ == "__main__":
    # Specify the root directory where 'train' and 'validation' directories are housed
    root_dir = 'snazzy_closet/backend/ml/dataset/'  # Example: replace with the actual path
    
    obfuscate_and_shuffle_recursive(root_dir)
    print("All image filenames in subdirectories have been obfuscated and shuffled.")
