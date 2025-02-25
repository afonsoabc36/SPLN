"""
Calcular ocorrencias
Frequencia absoluta/relativa, x vezes em y palavras, % de vezes


calculador - Outro modulo ao lado do base
Script calcular frequencias dado output de 2programas ig (??)
"""
import re
import json
import jjcli
from collections import Counter

def lexer(text):
    # FIXME: Not using patterns, stopwords
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+',text)

def main():
    cl = jjcli.clfilter(opt="i*o:o")
    tokens = []
    for text in cl.text():
        t = lexer(text)
        tokens.append(t)
    c = Counter(*tokens)
    d = dict(c)
    print(d)
    if "-o" in cl.opt:
        file = cl.opt.get("-o", "output.json")
        with open(file ,"w") as f:
            json.dump(d,f)
