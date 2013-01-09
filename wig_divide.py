#! /usr/bin/env python
"""this script was used to divide wig file into 24 wig files (24 chromosomes).
Date: 1-8-2013
Steven Yang @ Tongji University"""


# Gather our code in a main() function
def wigdivide(inputwig):
# open 24 wig files put each row into corresponding files

        chr1 = open('chr1.wig', 'w')
        chr2 = open('chr2.wig', 'w')
        chr3 = open('chr3.wig', 'w')
        chr4 = open('chr4.wig', 'w')
        chr5 = open('chr5.wig', 'w')
        chr6 = open('chr6.wig', 'w')
        chr7 = open('chr7.wig', 'w')
        chr8 = open('chr8.wig', 'w')
        chr9 = open('chr9.wig', 'w')
        chr10 = open('chr10.wig', 'w')
        chr11 = open('chr11.wig', 'w')
        chr12 = open('chr12.wig', 'w')
        chr13 = open('chr13.wig', 'w')
        chr14 = open('chr14.wig', 'w')
        chr15 = open('chr15.wig', 'w')
        chr16 = open('chr16.wig', 'w')
        chr17 = open('chr17.wig', 'w')
        chr18 = open('chr18.wig', 'w')
        chr19 = open('chr19.wig', 'w')
        chr20 = open('chr20.wig', 'w')
        chr21 = open('chr21.wig', 'w')
        chr22 = open('chr22.wig', 'w')
        chrX = open('chrX.wig', 'w')
        chrY = open('chrY.wig', 'w')

        import re
        f = open(inputwig, 'r')
        for line in f:
                if re.match("^chr1\t", line):
                        chr1.write(line)
                elif re.match("^chr2\t", line):
                        chr2.write(line)
                elif re.match("^chr3\t", line):
                        chr3.write(line)
                elif re.match("^chr4\t", line):
                        chr4.write(line)
                elif re.match("^chr5\t", line):
                        chr5.write(line)
                elif re.match("^chr6\t", line):
                        chr6.write(line)
                elif re.match("^chr7\t", line):
                        chr7.write(line)
                elif re.match("^chr8\t", line):
                        chr8.write(line)
                elif re.match("^chr9\t", line):
                        chr9.write(line)
                elif re.match("^chr10\t", line):
                        chr10.write(line)
                elif re.match("^chr11\t", line):
                        chr11.write(line)
                elif re.match("^chr12\t", line):
                        chr12.write(line)
                elif re.match("^chr13\t", line):
                        chr13.write(line)
                elif re.match("^chr14\t", line):
                        chr14.write(line)
                elif re.match("^chr15\t", line):
                        chr15.write(line)
                elif re.match("^chr16\t", line):
                        chr16.write(line)
                elif re.match("^chr17\t", line):
                        chr17.write(line)
                elif re.match("^chr18\t", line):
                        chr18.write(line)
                elif re.match("^chr19\t", line):
                        chr19.write(line)
                elif re.match("^chr20\t", line):
                        chr20.write(line)
                elif re.match("^chr21\t", line):
                        chr21.write(line)
                elif re.match("^chr22\t", line):
                        chr22.write(line)
                elif re.match("^chrX\t", line):
                        chrX.write(line)
                elif re.match("^chrY\t", line):
                        chrY.write(line)
        f.close()


# Standard boilerplate to call the main() function
# to begin the program.
if __name__ == '__main__':
        import sys
        from optparse import OptionParser

        usage = 'usage: python wig_divide.py -t inputwig'
        parser = OptionParser(usage)
        parser.add_option("-i", "--input", dest="input", help="input raw wig")

        (options, args) = parser.parse_args()

        if not options.input:   # only required argument
                parser.print_help()
                sys.exit(1)

        wigdivide(options.input)
