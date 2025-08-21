import os
import glob
from PIL import ImageGrab

# Directory to save the clipboard image
target_dir = os.path.expanduser(r"~\Pictures\ClipboardImage")
os.makedirs(target_dir, exist_ok=True)

# Delete old images
def delete_previous_images():
    for file in glob.glob(os.path.join(target_dir, "*")):
        try:
            os.remove(file)
        except Exception as e:
            print(f"Could not delete {file}: {e}")

# Grab image from clipboard
img = ImageGrab.grabclipboard()

if img is None:
    print("No image found in clipboard.")
else:
    delete_previous_images()
    
    save_path = os.path.join(target_dir, "clipboard.png")
    img.save(save_path, "PNG")
    print(f"Saved clipboard image to {save_path}")

input()