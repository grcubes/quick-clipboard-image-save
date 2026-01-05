import os
import glob
from PIL import ImageGrab


def get_target_dir():
    return os.path.expanduser(r"~\Pictures\ClipboardImage")


def delete_previous_images():
    for file in glob.glob(os.path.join(get_target_dir(), "*")):
        try:
            os.remove(file)
        except Exception as e:
            print(f"Could not delete {file}: {e}")


def save_image(img):
    if img is None:
        print("No image found in clipboard.")
    else:
        print("\n")
    
        # Delete old images
        delete_previous_images()
    
        save_image_path = os.path.join(get_target_dir(), "clipboard")

        img.save(f"{save_image_path}PNG.png", "PNG")
        
        try:
            img.save(f"{save_image_path}JPG.jpg", "JPEG")
        except OSError:
            print("OSError, skipping JPG...")
        print(f"Saved clipboard image to {get_target_dir()}")


def main():
    # Create directory
    os.makedirs(get_target_dir(), exist_ok=True)

    # Grab image from clipboard
    img = ImageGrab.grabclipboard()

    save_image(img)


if __name__ == "__main__":
    main()