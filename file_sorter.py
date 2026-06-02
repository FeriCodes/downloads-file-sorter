import os 
import shutil


downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

photo_dir = os.path.join(downloads_dir, "photo")

if not os.path.exists(photo_dir):
    os.makedirs(photo_dir)
    print("new folder name photo create successfully!")
else:
    print("this folder is already exist!")


photo_formats = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".jfif")
number = 0
for file in os.listdir(downloads_dir):
      

    full_path = os.path.join(downloads_dir, file)

    if not os.path.isfile(full_path):
        continue

    elif file.endswith(photo_formats):
        shutil.move(full_path, photo_dir)
        number += 1

        print(f"Moved: {file}")
print(f"the number of all files is: {number}")
