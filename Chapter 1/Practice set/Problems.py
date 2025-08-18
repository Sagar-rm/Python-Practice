import os

def print_directory_contents(path='.'):
    """
    Print all items in the given directory path (default: current directory).
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return
    except OSError as e:
        print(f"Error accessing '{path}': {e}")
        return

    print(f"Contents of directory '{path}':")
    for entry in sorted(entries):
        print(f"  - {entry}")

if __name__ == "__main__":
    # Example usage: specify a path or leave blank for the current folder
    print_directory_contents('/path/to/your/directory')
