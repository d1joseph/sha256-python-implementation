#!/usr/bin/python
import sys
import getopt


class Parameters:
    def __init__(self) -> None:
        pass


    # method 1
    def input_1(self):
        print('Number of arguments: ', len(sys.argv), 'arguments.')
        print('Argument List:', str(sys.argv))


    # method 2
    def input_2(self, argv):
        inputfile = ''
        outputfile = ''
        try:
            opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        except getopt.GetoptError:
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('test.py -i <inputfile> -o <outputfile>')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile= arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
        
        print('Input file is "', inputfile)
        print('Output file is "', outputfile)


if __name__ == "__main__":
    new_test = Parameters()
    new_test.input_2(sys.argv[1:])


        