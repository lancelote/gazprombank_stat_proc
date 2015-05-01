import os
import zipfile


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

    zipped_file = zipfile.ZipFile(directory + "/" + file, "r")
    zipped_file.extractall(path="./unzipped")


def compilation(file, directory, start_line, end_line, start_shift, end_shift):
    """
    Returns block of text between line contained start_line + start_shift and
    line contained end_line + end_shift
    """

    result = list()
    start_pos = 1000
    end_pos = 1000

    with open(directory + "/unzipped/" + file, "r") as file:
        for num, line in enumerate(file, 1):
            if start_line in line:
                start_pos = num + start_shift
            elif end_line in line:
                end_pos = num + end_shift
                result.append(line)
            elif start_pos < num < end_pos:
                result.append(line)

    return result


def text_processing(data_file, directory):
    """
    Processes a bank statement text and:
        1) appends new data to the summary file
        2) creates a bank transfer order for each transaction
    """

    # summary compilation #
    #######################

    # TODO remove space before new summary entry
    summary = compilation(data_file, directory, "Выписка по лицевому счету",
                          "Исходящее сальдо", 2, 0)

    # summary save #
    ################

    #with open(directory + "/sum.txt", "a+", encoding='utf8') as file:
    #    for line in summary:
    #        file.write("%s" % line)

    # bank transfer order #
    #######################

    #transfer_order = compilation(data_file, directory, 'Исходящее сальдо',
    #                             'Отметки банка', 4, 12)

    # bank transfer order save #
    ############################

    #with open(directory + "/" + "order" + ".txt", "a+",
    #          encoding='utf8') as file:
    #    for line in transfer_order:
    #        file.write("%s" % line)
