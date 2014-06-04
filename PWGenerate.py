from os import urandom
from struct import unpack
import sys

__author__ = 'Dilan'


def generate_pw(length):
    """
    This is our password generating function. It will take in the length, whether characters should be repeated,
    a string that determines whether to include numbers only, letters only, both, and whether special characters are
    allowed. It will return the string that contains the new random password.

    """
    asciitable = []
    password = ""
    for i in range(35, 127):
        asciitable.append(i)
    for i in range(length):
        try:
            rand = unpack("I",urandom(4))
        except NotImplementedError:
            print("Your operating system does not support random number generation and this program cannot generate a "
                  "truly random password for you.")
            sys.exit(0)

        rand = rand[0]
        rand %= 91
        password += str(unichr(asciitable[rand]))
    return password
def main():
    if len(sys.argv) < 2:
        print "Invalid number of arguments, usage is: PWGenerate.py length"
        sys.exit(0)
    else:
       length =  int(sys.argv[1])
       print generate_pw(10)

if __name__ == '__main__':
  main()

