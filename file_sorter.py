import os
import shutil


class FileSorter:
    """
    A utility class to automatically sort and organize files in a target directory
    based on their file extensions using predefined categories.
    """

    def __init__(self):
        # Set the target directory to the user's Downloads folder
        self.downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

        # fmt: off
        self.categories = {
            "Photos": (".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".jfif", ".svg"),
            "Videos": (".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"),
            "Music": (".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"),
            "Documents": (".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".json", ".md"),
            "Compressed": (".zip", ".rar", ".7z", ".tar", ".gz"),
            "Programs": (".exe", ".msi", ".apk"),
        }
        # fmt: on

    def organize_files(self):
        """
        Iterates through the target directory and categorizes each file.
        Unrecognized formats are moved to an 'Others' folder.
        """
        moved_count = 0

        for file in os.listdir(self.downloads_dir):
            full_path = os.path.join(self.downloads_dir, file)

            # Skip directories, process only files
            if not os.path.isfile(full_path):
                continue

            moved = False

            # Check file extension against predefined categories
            for category_name, formats in self.categories.items():
                if file.lower().endswith(formats):
                    self._move_file(file, full_path, category_name)
                    moved_count += 1
                    moved = True
                    break

            # If the file extension is not in our dictionary, move it to 'Others'
            if not moved:
                self._move_file(file, full_path, "Others")
                moved_count += 1

        print("-" * 30)
        print(f"Task completed! Total files moved: {moved_count}")
        return moved_count

    def _move_file(self, file_name, full_path, category_name):
        """
        Helper method to handle the creation of category directories
        and the safe moving of files.
        """
        category_dir = os.path.join(self.downloads_dir, category_name)

        # Create the specific category folder if it doesn't exist
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
            print(f"Created new folder: {category_dir}")

        # Move the file and handle potential permission or IO errors
        try:
            shutil.move(full_path, category_dir)
            print(f"Moved: {file_name} -> {category_name}/")
        except Exception as e:
            print(f"Error moving {file_name}: {e}")


if __name__ == "__main__":
    sorter = FileSorter()
    sorter.organize_files()
