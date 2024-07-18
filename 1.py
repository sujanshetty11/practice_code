import nltk
from nltk import CFG
grammar=CFG.fromstring(""" 
S -> NP VP 
VP -> V NP 
NP -> "rahil" | "market" | "moon"
V -> "went"|"go"| "saw"
""")
sentence="rahil saw moon".split()
def parse_and_print(parser,sentence):
    try:
        trees=list(parser.parse(sentence))
        for tree in trees:
            tree.pretty_print()
            tree.draw()
    except ValueError as e:
        print(f"error in parser {e}")

print(" b to u")
b_U_P=nltk.ChartParser(grammar)
parse_and_print(b_U_P,sentence)
t_to_b=nltk.RecursiveDescentParser(grammar)
parse_and_print(t_to_b,sentence)

