__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# best to import these within or outside function?
import os
import shutil
from zipfile import ZipFile
import glob


def clean_cache():
    # creates an empty folder 'cache' in the current directory if it does not exist,
    # cleans the cache folder if it already exists

    if not os.path.exists(".\cache"):               # better to use absolute or relative path here?
        print("dir does not exist, creating dir")
        os.mkdir(".\cache")                         # use mkdir or mkdirs? I don't understand the difference
    else:
        print("dir already exists, cleaning dir")
        shutil.rmtree(".\cache")
        os.mkdir(".\cache")


def cache_zip(zip_path, cache_path):
    # unpack zip file into a clean cache folder

    clean_cache()
    with ZipFile(zip_path, "r") as zip:
        zip.extractall(cache_path)


def cached_files():
    # returns a list of all files in the cache.

    path = os.getcwd() + "\cache\\"
    files_list = glob.glob(path + "*.txt")

    return files_list


def find_password(files_list):
    # read contents of each file toin files_list
    # to find and extract a password

    # loop over each file in files_list
    for file in files_list:
        # open the text file in read mode
        with open(file, "r") as f:
            # check each line in the file for flagword
            for line in f.readlines():
                # if the flagword is found
                # extract and return the password in the line
                if "password" in line:
                    return (line.split(": ")[1]).strip()


# is it best to search for the password line by line for each file as done above,
# OR check for the password per file with 'if flag in f.read():', and only when this condition is true,
# then go line by line to extract the password. What would be more efficient?


if __name__ == "__main__":
    clean_cache()
    cache_zip(".\data.zip", ".\cache")
    files_list = cached_files()
    print(find_password(files_list))
