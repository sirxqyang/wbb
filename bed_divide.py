#! /usr/bin/env python
"""this script was used to divide wig file into 24 wig files (24 chromosomes).
positive sense strand

Date: 1-9-2013
Steven Yang @ Tongji University"""


# Gather My code in a main() function
def wigdivide(inputbed):
# open 24 wig files put each row into corresponding files

        import os
        if not os.path.exists('positive'):
                os.makedirs('positive')
        chr1p = open('positive/chr1.bed', 'w')
        chr2p = open('positive/chr2.bed', 'w')
        chr3p = open('positive/chr3.bed', 'w')
        chr4p = open('positive/chr4.bed', 'w')
        chr5p = open('positive/chr5.bed', 'w')
        chr6p = open('positive/chr6.bed', 'w')
        chr7p = open('positive/chr7.bed', 'w')
        chr8p = open('positive/chr8.bed', 'w')
        chr9p = open('positive/chr9.bed', 'w')
        chr10p = open('positive/chr10.bed', 'w')
        chr11p = open('positive/chr11.bed', 'w')
        chr12p = open('positive/chr12.bed', 'w')
        chr13p = open('positive/chr13.bed', 'w')
        chr14p = open('positive/chr14.bed', 'w')
        chr15p = open('positive/chr15.bed', 'w')
        chr16p = open('positive/chr16.bed', 'w')
        chr17p = open('positive/chr17.bed', 'w')
        chr18p = open('positive/chr18.bed', 'w')
        chr19p = open('positive/chr19.bed', 'w')
        chr20p = open('positive/chr20.bed', 'w')
        chr21p = open('positive/chr21.bed', 'w')
        chr22p = open('positive/chr22.bed', 'w')
        chrXp = open('positive/chrX.bed', 'w')
        chrYp = open('positive/chrY.bed', 'w')

        if not os.path.exists('negative'):
                os.makedirs('negative')
        chr1n = open('negative/chr1.bed', 'w')
        chr2n = open('negative/chr2.bed', 'w')
        chr3n = open('negative/chr3.bed', 'w')
        chr4n = open('negative/chr4.bed', 'w')
        chr5n = open('negative/chr5.bed', 'w')
        chr6n = open('negative/chr6.bed', 'w')
        chr7n = open('negative/chr7.bed', 'w')
        chr8n = open('negative/chr8.bed', 'w')
        chr9n = open('negative/chr9.bed', 'w')
        chr10n = open('negative/chr10.bed', 'w')
        chr11n = open('negative/chr11.bed', 'w')
        chr12n = open('negative/chr12.bed', 'w')
        chr13n = open('negative/chr13.bed', 'w')
        chr14n = open('negative/chr14.bed', 'w')
        chr15n = open('negative/chr15.bed', 'w')
        chr16n = open('negative/chr16.bed', 'w')
        chr17n = open('negative/chr17.bed', 'w')
        chr18n = open('negative/chr18.bed', 'w')
        chr19n = open('negative/chr19.bed', 'w')
        chr20n = open('negative/chr20.bed', 'w')
        chr21n = open('negative/chr21.bed', 'w')
        chr22n = open('negative/chr22.bed', 'w')
        chrXn = open('negative/chrX.bed', 'w')
        chrYn = open('negative/chrY.bed', 'w')

        import re
        f = open(inputbed, 'r')
        for line in f:
                parts = re.split(r'\t', line)
                if re.search("\t[\+]\n", line):
                        Start = int(parts[1])
                        End = int(parts[1]) + 1
                        Line = parts[0] + "\t" + str(Start) + "\t" + str(End) + "\n"
                        if re.search("^chr1\t", line):
                                chr1p.write(Line)
                        elif re.search("^chr2\t", line):
                                chr2p.write(Line)
                        elif re.search("^chr3\t", line):
                                chr3p.write(Line)
                        elif re.search("^chr4\t", line):
                                chr4p.write(Line)
                        elif re.search("^chr5\t", line):
                                chr5p.write(Line)
                        elif re.search("^chr6\t", line):
                                chr6p.write(Line)
                        elif re.search("^chr7\t", line):
                                chr7p.write(Line)
                        elif re.search("^chr8\t", line):
                                chr8p.write(Line)
                        elif re.search("^chr9\t", line):
                                chr9p.write(Line)
                        elif re.search("^chr10\t", line):
                                chr10p.write(Line)
                        elif re.search("^chr11\t", line):
                                chr11p.write(Line)
                        elif re.search("^chr12\t", line):
                                chr12p.write(Line)
                        elif re.search("^chr13\t", line):
                                chr13p.write(Line)
                        elif re.search("^chr14\t", line):
                                chr14p.write(Line)
                        elif re.search("^chr15\t", line):
                                chr15p.write(Line)
                        elif re.search("^chr16\t", line):
                                chr16p.write(Line)
                        elif re.search("^chr17\t", line):
                                chr17p.write(Line)
                        elif re.search("^chr18\t", line):
                                chr18p.write(Line)
                        elif re.search("^chr19\t", line):
                                chr19p.write(Line)
                        elif re.search("^chr20\t", line):
                                chr20p.write(Line)
                        elif re.search("^chr21\t", line):
                                chr21p.write(Line)
                        elif re.search("^chr22\t", line):
                                chr22p.write(Line)
                        elif re.search("^chrX\t", line):
                                chrXp.write(Line)
                        elif re.search("^chrY\t", line):
                                chrYp.write(Line)

                if re.search("\t[\-]\n", line):
                        Start = int(parts[2]) - 1
                        End = int(parts[2])
                        Line = parts[0] + "\t" + str(Start) + "\t" + str(End) + "\n"
                        if re.search("^chr1\t", line):
                                chr1n.write(Line)
                        elif re.search("^chr2\t", line):
                                chr2n.write(Line)
                        elif re.search("^chr3\t", line):
                                chr3n.write(Line)
                        elif re.search("^chr4\t", line):
                                chr4n.write(Line)
                        elif re.search("^chr5\t", line):
                                chr5n.write(Line)
                        elif re.search("^chr6\t", line):
                                chr6n.write(Line)
                        elif re.search("^chr7\t", line):
                                chr7n.write(Line)
                        elif re.search("^chr8\t", line):
                                chr8n.write(Line)
                        elif re.search("^chr9\t", line):
                                chr9n.write(Line)
                        elif re.search("^chr10\t", line):
                                chr10n.write(Line)
                        elif re.search("^chr11\t", line):
                                chr11n.write(Line)
                        elif re.search("^chr12\t", line):
                                chr12n.write(Line)
                        elif re.search("^chr13\t", line):
                                chr13n.write(Line)
                        elif re.search("^chr14\t", line):
                                chr14n.write(Line)
                        elif re.search("^chr15\t", line):
                                chr15n.write(Line)
                        elif re.search("^chr16\t", line):
                                chr16n.write(Line)
                        elif re.search("^chr17\t", line):
                                chr17n.write(Line)
                        elif re.search("^chr18\t", line):
                                chr18n.write(Line)
                        elif re.search("^chr19\t", line):
                                chr19n.write(Line)
                        elif re.search("^chr20\t", line):
                                chr20n.write(Line)
                        elif re.search("^chr21\t", line):
                                chr21n.write(Line)
                        elif re.search("^chr22\t", line):
                                chr22n.write(Line)
                        elif re.search("^chrX\t", line):
                                chrXn.write(Line)
                        elif re.search("^chrY\t", line):
                                chrYn.write(Line)

        f.close()


# Standard boilerplate to call the main() function
# to begin the program.
if __name__ == '__main__':

        import sys
        from optparse import OptionParser

        usage = 'usage: python wig_divide.py -t inputbed'
        parser = OptionParser(usage)
        parser.add_option("-i", "--input", dest="input", help="input bed file")

        (options, args) = parser.parse_args()

        if not options.input:   # only required argument
                parser.print_help()
                sys.exit(1)

        wigdivide(options.input)
