import os

# Print current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Define directory name
directory_name = "test_directory"

# Create directory if it doesn't exist
os.makedirs(directory_name, exist_ok=True)
print(f"Directory '{directory_name}' created or already exists")
