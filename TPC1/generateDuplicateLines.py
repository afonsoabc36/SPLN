import random
import argparse

def generateLines(outputFile, size):
    with open(outputFile, "w") as output:
        for i in range(size):
            randomNumber = random.randint(1, 3)
            output.write(f"Line {i}\n" * randomNumber)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate randomly duplicate lines in a file.")
    parser.add_argument("size", nargs="?", type=int, default=50, help="Number of unique lines (default: 50)")
    parser.add_argument("outputFile", nargs="?", default="input.txt", help="Output file (default: input.txt)")

    args = parser.parse_args()

    generateLines(args.outputFile, args.size)

