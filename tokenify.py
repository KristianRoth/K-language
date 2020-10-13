def prettyPrint(ts):
    for x in ts:
        print(x)


def read(code, end, skip = " \n", include_end = False):
    part = ""
    while True:
        op, *code = code
        if op in skip:
            continue
        if op in end:
            if include_end:
                return (part + op, code)
            return (part, code, op)
        part += op

def readList(code, end, delimitter, skip=" \n"):
    l = []
    while True:
        (part, code, de) = read(code, end+delimitter)
        l.append(part)
        if de in end:
            return (l, code)

def readWhile(code, wh = " \n"):
    while True:
        if (len(code) == 0):
            return False
        op, *code = code
        if op not in wh:
            return (op, op + "".join(code))

def expression(par):
    (code, ts) = par
    (lookup, code) = readWhile(code)

    if lookup == '"':
        #string literal
        start, *code = code
        (literal, code, end) = read(code, '"', skip="")
        ts.append(("string_literal", literal))
        return (code, ts)
    elif lookup == "$":
        #identifier
        op, *code = code
        (identifier, code, end) = read(code, ")")
        ts.append(("identifier", identifier))
        return (end + "".join(code), ts)
    else:
        #function_call
        (func, code, end) = read(code, ":")
        ts.append(("function_call", func))
        while True:
            ts.append(("additional_parameter", "aditional_parameter"))
            (code, ts) =  statement((code, ts))
            (lookup, code) = readWhile(code)
            if lookup != ",":
                break
            op, *code = code
        return (code, ts)

def statement(par):
    (code, ts) = par
    parenthesis, *code = code
    if (parenthesis != "("):
        raise ValueError("Error: invalid statement Start in \n" + "".join(code))
    ts.append(("statement_start", "statement_start"))

    (lookup, code) = readWhile(code)

    if lookup == ")":
        ## Empty statement
        pass
    elif lookup == "(":
        (code, ts) = statement((code, ts))
    else:
        (code, ts) = expression((code, ts))

    
    parenthesis, *code = code
    if (parenthesis != ")"):
        raise ValueError("Statement end expected")
    
    ts.append(("statement_end", "statement_end"))
    return (code, ts)


def tokenify(par):
    (code, ts) = par

    while True:
        a = readWhile(code)
        if not a:
            return ts
        (lookup, code) = a

        if lookup == "(":
            # Toplevel statement
            (code, ts) = statement((code, ts))
        else:
            # Function Definition
            (func, code, end) = read(code, ":")

            ts.append(("function_definition", func))

            (parameters, code) = readList(code, ":", ",")
            for parameter in parameters:
                ts.append(("parameter_definition", parameter))

            (code, ts) = statement((code, ts))
