import sys
from itertools import count
from tokenify import tokenify, prettyPrint
from compiler import compiler



def compile(code):
    ts = tokenify((code, []))
    print("tokenized:")
    prettyPrint(ts)
    code = compiler(ts)





def main():
    if len(sys.argv) <= 1:
        print("Missing arguments")
        return

    with open(sys.argv[1]) as f:
        code = f.read()

    compile(code)

if __name__ == "__main__":
    main()