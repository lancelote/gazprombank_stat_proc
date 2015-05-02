import os
import zipfile
from codecs import open


class Statement():

    def __init__(self, text, date):
        self.text = text
        self.date = date


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


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
    # Retrieve file text
    text = []
    for line in file:
        text.append(line)

    # File date
    date = {}
    if is_number(text[6][9]):
        date["day"] = text[6][9:11]
    else:
        date["day"] = text[6][10:11]
    date["month"] = text[6][12:14]
    date["year"] = text[6][15:19]

    # Create a statement
    statement = Statement(text, date)

    return statement


def write(statement, directory):
    file_path = os.path.join(directory, "processed", statement.date["year"], statement.date["month"])
    file_name = statement.date["day"] + ".txt"

    # Create directory tree is needed
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # Create a statement file
    with open(os.path.join(file_path, file_name), "w+", encoding="utf-8") as file:
        for line in statement.text:
            file.write("%s" % line)


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
        with open(os.path.join(directory, "unzipped", unzipped_file), "r", encoding="cp1251") as file:
            statement = process(file)
        write(statement, directory)


main("test/test_data/test_statements")