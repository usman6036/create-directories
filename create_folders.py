import os

# Print current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Define directory names
successful_directory = "successful"
unsuccessful_directory = "unsuccessful"

# Create directories
os.makedirs(successful_directory, exist_ok=True)
os.makedirs(unsuccessful_directory, exist_ok=True)

print(f"Directories '{successful_directory}' and '{unsuccessful_directory}' created or already exist")
