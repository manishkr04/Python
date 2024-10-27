import os


def list_files_in_folder(folder_path):
    try:
        file = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"
    
def main():
    folder_paths = input("Enter a list of folder paths seperated by space: ").split()

    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Erron in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()
    