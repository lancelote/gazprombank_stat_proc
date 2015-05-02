import os
import zipfile


def get_files(directory):
    """
    Returns a list of all files in the target directory
    """
    # ToDo : add NoSuchFile case
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    return files


def unzip(file, directory):
    """
    Unzip a file
    """
    # ToDo : add CanNotCreateFileOrDir case
    zipped_file = zipfile.ZipFile(os.path.join(directory, file), "r")
    zipped_file.extractall(path=os.path.join(directory, "unzipped"))


