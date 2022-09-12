import getopt
import os
import sys

HELP_MESSAGE = ('\nOPTIONS:\n'
                '-i <inputfile>, --ifile=<inputfile>\n'
                '-o <outputpath>, --ipath=<outputpath>\n\n'
                'EXAMPLE:\n'
                'python3 ccfl.py --ifile=/documents/hostlist.txt '
                '--ipath=/documents/output\n')


def main(argv):
    inputfile = ''
    outputpath = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "opath="])
    except getopt.GetoptError:
        print(HELP_MESSAGE)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(HELP_MESSAGE)
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-o', '--opath'):
            outputpath = arg
    if outputpath and inputfile:
        try:
            with open(inputfile, 'r') as infile:
                data = infile.readlines()
                for host in data:
                    cmd = ('cutycapt --url=' + host + ' --out='
                           + outputpath + ' ' + host + '.png')
                    os.system(cmd)
                    print(f'Screenshot of {host} done.')
        except Exception as error:
            raise Exception(f'File open error: {error}')


if __name__ == "__main__":
    main(sys.argv[1:])
