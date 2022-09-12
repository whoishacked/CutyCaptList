import getopt
import os
import re
import subprocess
import sys

HELP_MESSAGE = ('\nOPTIONS:\n'
                '-i <inputfile>, --ifile=<inputfile>\n'
                '-o <outputpath>, --ipath=<outputpath>\n\n'
                'EXAMPLE:\n'
                'python3 ccfl.py --ifile=/documents/hostlist.txt '
                '--ipath=/documents/output\n')


def main(argv):
    inputfile: str = ''
    outputpath: str = ''
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
                    host = host.replace('\n', '')
                    filename: str = re.sub('[\W_]+', '', host) + '.png'
                    cmd: str = ('cutycapt --url=' + host + ' --out='
                                + outputpath + filename)
                    subprocess.call(
                        cmd,
                        shell=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT
                    )
                    if os.path.exists(outputpath + filename):
                        print(f'Screenshot of {host} done.')
                    else:
                        print(f'Screenshot wasn\'t created')
        except Exception as error:
            raise Exception(f'File open error: {error}')


if __name__ == "__main__":
    main(sys.argv[1:])
