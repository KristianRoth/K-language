import sys
from itertools import count
from tokenize import tokenize, prettyPrint
from compiler import compiler



def compile(code):
    ts = tokenize((code, []))
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