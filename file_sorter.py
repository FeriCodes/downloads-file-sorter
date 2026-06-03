import os 
import shutil

def organize_photos():
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    photo_dir = os.path.join(downloads_dir, "photo")

    if not os.path.exists(photo_dir):
        os.makedirs(photo_dir)
        print("new folder name photo create successfully!")
    else:
        print("this folder is already exist!")


    photo_formats = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".jfif")
    moved_count = 0

    for file in os.listdir(downloads_dir):
        full_path = os.path.join(downloads_dir, file)

        if os.path.isfile(full_path) and file.endswith(photo_formats):
            try:
                file.endswith(photo_formats)
                shutil.move(full_path, photo_dir)
                moved_count += 1
            except Exception as e:
                print(f"Error moving {file}: {e}")
        
    print("-" * 30)
    print(f"Task completed! Total photos moved: {moved_count}")
    return moved_count
        
organize_photos()
