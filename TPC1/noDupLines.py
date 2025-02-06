import sys
import argparse

def removeDuplicates(inputFile, outputFile):
    linesSet = set()  # Guardar as linhas únicas, permite lookup eficiente
    linesList = []  # Guardar as linhas mantendo a ordem

    with (sys.stdin if inputFile == sys.stdin else open(inputFile, "r")) as input:
        for line in input:
            line = line.strip()
            if line not in linesSet:
                linesSet.add(line)
                linesList.append(line)

    with (sys.stdout if outputFile == sys.stdout else open(outputFile, "w")) as output:
        for line in linesList:
            print(line, file=output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove duplicate lines from a file while preserving order.")
    parser.add_argument("input_file", nargs="?", default=sys.stdin, help="Input file (default: stdin)")
    parser.add_argument("output_file", nargs="?", default=sys.stdout, help="Output file (default: stdout)")

    args = parser.parse_args()

    removeDuplicates(args.input_file, args.output_file)
