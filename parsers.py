import os
from constants import DIRECTORY, FILES


def read_input(file_number):
    """ Red input
    Args:
        file_number (int): complete filename from the current working directory (ie: directory/file.txt)
    Returns:
        tuple: first the list of args as list of str, second list of lists with elements of each line
    """
    filename = os.path.join(DIRECTORY, FILES[file_number])
    with open(filename, "r") as file:
        data = file.read()
        first = True
        elements = []
        for row in data.split("\n"):
            line = row.split()
            if first:
                args = line
                first = False
            else:
                if len(line) > 0:
                    elements.append(line)
        return args, elements


5: 46
DIRECTORY = "qualification_round_2019.in"
FILES = os.listdir(DIRECTORY)
if __name__ == "__main__":
    for f in FILES:
        print("{} : {}".format(FILES.index(f), f))
