import sys


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white
Y = '\033[33m' # yellow


def isInt(key):
    try: 
        int(key)
        return True
    except ValueError:
        return False

def move():
    try:
        flag = sys.argv[1].strip()
        key = sys.argv[2].strip()
        message = sys.argv[3].strip()

        outputMessage = ""

        selection = 0

        if flag == '-d':
            selection = 1
        elif flag == '-e':
            selection = 2
        else:
            pass
        
        if not (selection == 1 or selection == 2):
            print('\nUnknown mode flag\n')
            sys.exit()

        if isInt(key):
            pass
        else:
            print('\nKey must be an Integer\n')
            sys.exit()

        for x in message:
            if x.isalpha():
                if selection == 1:
                    outputMessage += chr(ord(x) - int(key))
                elif selection == 2:
                    outputMessage += chr(ord(x) + int(key))
                else:
                    pass
            else:
                outputMessage += x

        print(outputMessage)

        # char -> Return the Unicode string of one character
        # ord -> Return the Unicode code point
    except IndexError as identifier:
        print("""
Usage: caesar.py [-d/-e] key[int] message 
        """)
    except Exception as e:
        print('\n' + R + '[-] Exception : ' + C + str(e) + W + '\n')
        exit()


if __name__ == "__main__":
    move()