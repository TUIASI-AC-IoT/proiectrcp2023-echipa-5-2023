import os

def delete_file(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
            return True
        except OSError as e:
            print(f"Failed to delete file: {file_path}. {e}")
    else:
        print(f"The specified file does not exist: {file_path}")
    return False

def create_empty_file(folder_path, file_name):
    os.makedirs(folder_path, exist_ok=True) 
    file_path = os.path.join(folder_path, file_name)
    try:
        with open(file_path, 'w'):
            pass
        print(f"Created empty file: {file_path}")
        return True
    except OSError as e:
        print(f"Failed to create empty file: {file_path}. {e}")
        return False


def update_file(folder_path, file_name, new_content):
    file_path = os.path.join(folder_path, file_name)
    try:
        with open(file_path, 'a') as file:
            file.write(new_content + "\n")
        print(f"Appended new content to file: {file_path}")
        return True
    except OSError as e:
        print(f"Failed to update file: {file_path}. {e}")
        return False


def read_file_content(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except OSError as e:
            print(f"Failed to read file: {file_path}. {e}")
            return None
    else:
        print(f"The specified file does not exist: {file_path}")
        return None



