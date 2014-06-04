__author__ = 'Dilan'


def generate_pw():
    asciitable = []
    for i in range(65, 91):
        asciitable.append(i)
    for i in range(97, 123):
        asciitable.append(i)
    print asciitable
    for i in range(len(asciitable)):
        print str(unichr(asciitable[i]))
generate_pw()