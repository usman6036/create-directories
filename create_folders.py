import os
import sys

# Get the directory path of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Create directories relative to the script's directory
os.makedirs(os.path.join(script_dir, 'successful'), exist_ok=True)
os.makedirs(os.path.join(script_dir, 'unsuccessful'), exist_ok=True)

# Log directory creation
print(f"Directories created in {script_dir}: {os.listdir(script_dir)}")
