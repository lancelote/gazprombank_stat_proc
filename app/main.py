import os
import zipfile


class Statement():

    pass


def get_files(directory):
    """
    Returns a list of all files in the target directory
    """
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    return files


def unzip(file, directory):
    """
    Unzip a file
    """
    zipped_file = zipfile.ZipFile(os.path.join(directory, file), "r")
    zipped_file.extractall(path=os.path.join(directory, "unzipped"))


def process(file):
    pass


def write(file):
    pass


def main(directory):
    """
    Main logic controller
    """
    # Create a list of zipped files
    zipped_files = get_files(directory)

    # Unzip files
    for zipped_file in zipped_files:
        unzip(zipped_file, directory)

    # Create a list of unzipped files
    unzipped_files = get_files(os.path.join(directory, "unzipped"))

    # Process and write unzipped files
    for unzipped_file in unzipped_files:
        statement = process(unzipped_file)
        write(statement)