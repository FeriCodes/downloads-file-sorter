import os
import shutil


class FileSorter:
    def __init__(self):
        self.downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
        self.photo_dir = os.path.join(self.downloads_dir, "photo")
        self.photo_formats = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".jfif")

    def organize_photos(self):

        if not os.path.exists(self.photo_dir):
            os.makedirs(self.photo_dir)
            print("new folder name photo create successfully!")
        else:
            print("this folder is already exist!")

        moved_count = 0

        for file in os.listdir(self.downloads_dir):
            full_path = os.path.join(self.downloads_dir, file)

            if os.path.isfile(full_path) and file.lower().endswith(self.photo_formats):
                try:
                    shutil.move(full_path, self.photo_dir)
                    moved_count += 1
                    print(f"Moved: {file} -> photo/")
                except Exception as e:
                    print(f"Error moving {file}: {e}")

        print("-" * 30)
        print(f"Task completed! Total photos moved: {moved_count}")
        return moved_count


if __name__ == "__main__":
    sorter = FileSorter()
    sorter.organize_photos()
