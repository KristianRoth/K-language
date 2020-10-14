from Tree import Node

def makeTree(ts, tree):
    while True:
        if (len(ts) == 0):
            return (ts, tree)
        (key, value), *ts = ts

        if key == "function_definition":
            print("Funciton Definition")
            funcTree = Node("function_defenition").addChild(Node(value))
            funcParams = Node("parameters")
            while True:
                if ts[0][0] != "parameter_definition":
                    break
                (key, value), *ts = ts
                funcParams.addChild(Node(value))
            funcTree.addChild(funcParams)
            (key, value), *ts = ts
            if key != "statement_start":
                raise ValueError("Function bondy is not a Statement '(' expected")
            statementTree = Node("statement")
            (ts, statementTree) = makeTree(ts, statementTree)
            funcTree.addChild(statementTree)
            tree.addChild(funcTree)
        elif key == "statement_start":
            print("Statement")
            statementTree = Node("statement")
            (ts, statementTree) = makeTree(ts, statementTree)
            tree.addChild(statementTree)
        elif key == "statement_end":
            return (ts, tree)
        elif key == "function_call":
            funcTree = Node("function_call")
            funcTree.addChild(Node(value))
            while True:
                if ts[0][0] != "additional_parameter":
                    break
                (key, value), *ts = ts
                (key, value), *ts = ts
                if key != "statement_start":
                    raise ValueError("Function call parameter is not a Statement '(' expected")
                statementTree = Node("statement")
                (ts, statementTree) = makeTree(ts, statementTree)
                funcTree.addChild(statementTree)
            tree.addChild(funcTree)
        elif key == "identifier":
            tree.addChild(Node("identifier").addChild(Node(value)))
        elif key == "string_literal":
            tree.addChild(Node("string_literal").addChild(Node(value)))
        else:
            raise ValueError("Something went wrong identifier: " + key)

def compiler(ts):
    (ts, tree) = makeTree(ts, Node("ROOT"))
    return tree