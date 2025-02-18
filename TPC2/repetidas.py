#!/usr/bin/env python3
"""
Repetidas - Removes duplicate lines from a program.

Usage - 
    repetidas options file*

Options -
    -s : Keep spaces
    -e : Remove duplicated empty lines
    -p prefix : Add the symbol to the start of the duplicated lines
"""

from jjcli import clfilter


def remove_linhas_repetidas(cl):
    linhas = set()
    for linha in cl.input():
        if "-s" not in cl.opt:
            ln = linha.strip()
        else:
            ln = linha
        
        if not ln and "-e" not in cl.opt:
            print(linha)
        elif ln not in linhas:
            linhas.add(linha)
            print(linha)
        elif "-p" in cl.opt:
            prefix = cl.opt.get("-p", "")
            print(f"{prefix}{linha}")

def main():
    cl = clfilter(opt="sep:p", man=__doc__)  # -s and -e do not need arguments, p does
    remove_linhas_repetidas(cl)


if __name__ == "__main__":
    main()
