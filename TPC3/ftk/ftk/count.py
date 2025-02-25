import json
import jjcli
from collections import Counter

def main():
    cl = jjcli.clfilter(opt="i:o:p")
    files = cl.opt.get("-i", "").split(",")
    outputFile = cl.opt.get("-o", "totalOutput.json")
    totalCounter = Counter()
    for f in files:
        with open(f, "r") as file:
            data = json.load(file)
            partialCounter = Counter(data)
            totalCounter.update(partialCounter)
    totalWords = totalCounter.total()
    if "-o" in cl.opt:
        with open(outputFile, "w") as file:
            json.dump(totalCounter, file)
    if "-p" in cl.opt:
        print(f"\nTotal number of words: {totalWords}\n")
        print(f"{'Word':<20}{'Count':<10}{'Frequency':<10}")
        print("-" * 40)
        for word, count in sorted(totalCounter.items(), key=lambda x: (-x[1], x[0])):
            percentage = (count / totalWords) * 100
            print(f"{word:<20}{count:<10}{percentage:.2f}%")

if __name__ == "__main__":
    main()
