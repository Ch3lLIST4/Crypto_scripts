# Python Program to find the SHA3_512 message digest of a file

# importing the hashlib module
import hashlib
import os
import sys

def hash_file(filename):
    """"This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object
    h = hashlib.sha3_512()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

        # return the hex representtion of digest
        return h.hexdigest()

fn = sys.argv[1]

if os.path.exists(fn):
    print(os.path.basename(fn))
    # file exists
    message = hash_file(fn)
    print(message)

else:
    print('Please include an existing file path')

    