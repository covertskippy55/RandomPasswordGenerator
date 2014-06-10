from os import urandom
from struct import unpack
import sys
__author__ = 'Dilan'


def generate_pw(length, pw_type, specials):
    """
    This is our password generating function. It will take in the length, whether characters should be repeated,
    a string that determines whether to include numeric, alphanumeric or alphabet only, it will also take in whether to
    allow special characters, but only when the alphabet is involved, meaning you can have special characters with
    either the alphabet or alphanumeric, NOTE that this means you cannot have a numeric password with special characters

    :param length: length of the desired password, must be greater than zero
    :param pw_type: the type of the password( numeric, alphabet, alphanumeric)
    """
    asciitable = {}
    password = ""
    asciivalue = 48
    for i in range(10):
        asciitable[i] = asciivalue
        asciivalue += 1
    asciivalue = 65
    for i in range(10, 36):
        asciitable[i] = asciivalue
        asciivalue += 1
    asciivalue = 97
    for i in range(36, 62):
        asciitable[i] = asciivalue
        asciivalue += 1
    asciivalue = 33
    for i in range(62, 77):
        asciitable[i] = asciivalue
        asciivalue += 1
    asciivalue = 58
    for i in range(77, 84):
        asciitable[i] = asciivalue
        asciivalue += 1
    asciivalue = 91
    for i in range(84, 90):
        asciitable[i] = asciivalue
        asciivalue += 1
    asciivalue = 123
    for i in range(90, 94):
        asciitable[i] = asciivalue
        asciivalue += 1
    #print asciitable
    # for i in range(len(asciitable)):
    #     print i, str(unichr(asciitable.get(i)))

    if pw_type == "alphabet":
        if not specials:
            for i in range(length):
                rand = unpack("I", urandom(4))[0]
                rand %= 62
                if rand < 10:
                    rand += 10
                password += str(unichr(asciitable.get(rand)))
        else:
            for i in range(length):
                rand = unpack("I", urandom(4))[0]
                rand %= 93
                if rand < 10:
                    rand += 10
                password += str(unichr(asciitable.get(rand)))
    if pw_type == "numeric":
        for i in range(length):
            rand = unpack("I", urandom(4))[0]
            rand %= 10
            password += str(unichr(asciitable.get(rand)))
    if pw_type == "alphanumeric":
        if not specials:
            for i in range(length):
                rand = unpack("I", urandom(4))[0]
                rand %= 62
                password += str(unichr(asciitable.get(rand)))
        else:
            for i in range(length):
                rand = unpack("I", urandom(4))[0]
                rand %= 93
                if rand < 10:
                    rand += 10
                password += str(unichr(asciitable.get(rand)))
    return password


def main():
    if len(sys.argv) < 3:
        print "Invalid number of arguments, usage is: PWGenerate.py length PW_Type(alphabet, numeric," \
              " alphanumeric) [sc]  **Note that the sc flag is optional and is used to include special characters" \
              "in your password**"
        sys.exit(0)
    if len(sys.argv) == 3:
        print generate_pw(int(sys.argv[1]), sys.argv[2], False)
    elif (sys.argv[2] == "numeric") and (sys.argv[3] == "sc"):
        print "You cannot generate a password with numeric and special characters."
    else:
        print generate_pw(int(sys.argv[1]), sys.argv[2], True)

if __name__ == '__main__':
    main()