import os

# Create directories if they don't exist
os.makedirs('successful', exist_ok=True)
os.makedirs('unsuccessful', exist_ok=True)

# ... Other code ...

# Log directory creation
print(f"Directories created: {os.listdir()}")