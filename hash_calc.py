# Python Program to find the SHA3_512 message digest of a file

# importing the hashlib module
import hashlib
import os
import sys

def hash_file(fn, hash_type):
    """"This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object based on types
    if hash_type == 'sha1':
        h = hashlib.sha1()
    elif hash_type == 'sha224':
        h = hashlib.sha224()
    elif hash_type == 'sha256':
        h = hashlib.sha256()
    elif hash_type == 'sha384':
        h = hashlib.sha384()
    elif hash_type == 'sha512':
        h = hashlib.sha512()
    elif hash_type == 'sha3_224':
        h = hashlib.sha3_224()
    elif hash_type == 'sha3_256':
        h = hashlib.sha3_256()
    elif hash_type == 'sha3_384':
        h = hashlib.sha3_384()
    elif hash_type == 'sha3_512':
        h = hashlib.sha3_512()    

    # open file for reading in binary mode
    with open(fn, 'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

        # return the hex representtion of digest
        return h.hexdigest()

 
print(sys.argv)
hash_type = sys.argv[1]
fn = sys.argv[2]

if os.path.exists(fn):
    print(os.path.basename(fn))
    # file exists
    message = hash_file(fn, hash_type)
    print(message)

else:
    print('Please include an existing file path')
