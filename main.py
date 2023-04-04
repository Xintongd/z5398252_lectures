# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# noinspection PyUnresolvedReferences

import os

def safe_open(pth, mode='rt'):
    """ Opens the file in `pth` using the mode in `mode` and returns
    a file object.

    Will not open a file in writing mode if the file already exists and has
    some content.

    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading,
        and 'a' for appending. See the `open` function for more options.
        Defaults to 'rt'
    """
    with safe_open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: {line}")


if __name__ == "__main__":

    # Opening an existing file with content for reading
    with safe_open("test_file_exists_with_content.txt", mode='r') as fobj:
       print(fobj.read())

    # Opening an existing file with no content for writing - should work
    with safe_open("test_file_exists_no_content.txt", mode='w') as fobj:
       fobj.write('content')


    # Opening an existing file with content for writing - should raise Exception
    with safe_open("test_file_exists_with_content.txt", mode='w') as fobj:
       fobj.write('content')

