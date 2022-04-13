import os


def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("File is not exist...")
    infile = open(filename, "r")
    line = infile.readline()
    return line
