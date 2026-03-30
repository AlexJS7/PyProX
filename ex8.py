# Exercise 8 - Read Write File

"""
File I/O, or file input/output, allows your programs to read and write data to files on the hard drive.
"""

from pathlib import Path

FILE_DIR_PATH = Path(__file__).resolve().parent / 'files'
FILE_NAME = 'greet.txt'


def get_file_path(filename):
    return Path(FILE_DIR_PATH / filename)


def write_to_file(filename, text_content):
    # parents=True creates all missing parent directories in the path.
    # exist_ok=True avoids raising an error if the directory already exists.
    FILE_DIR_PATH.mkdir(parents=True, exist_ok=True)

    file_path = get_file_path(filename)
    file_path.write_text(text_content, encoding='utf-8')


def append_to_file(filename, text_content):
    file_path = get_file_path(filename)
    with file_path.open('a', encoding='utf-8') as f:
        f.write(text_content)


def read_from_file(filename):
    file_path = get_file_path(filename)
    return file_path.read_text(encoding='utf-8')


def delete_file(filename):
    file_path = get_file_path(filename)

    # missing_ok=True avoids error if file doesn’t exist.
    file_path.unlink(missing_ok=True)

    # `iterdir()` yields files/subfolders
    is_empty = not any(FILE_DIR_PATH.iterdir())
    if is_empty:
        FILE_DIR_PATH.rmdir()


write_to_file(FILE_NAME, 'Hello!\n')
append_to_file(FILE_NAME, 'Goodbye!\n')
assert read_from_file(FILE_NAME) == 'Hello!\nGoodbye!\n'
delete_file(FILE_NAME)
