from tokenify import tokenify
from compiler import compiler

def _getTestCode(path):
    with open("tests/data/" + path) as f:
        code = f.read()
    return code

def _getTestTree(path):
    ts = tokenify((_getTestCode(path), []))
    return compiler(ts)

def test_tree_a():
    tree = _getTestTree("test1.k")
    assert tree.count() == 8
    assert tree.depth() == 1

def test_tree_a():
    tree = _getTestTree("test2.k")
    assert tree.count() == 9
    assert tree.depth() == 9

def test_tree_params():
    tree = _getTestTree("test3.k")
    assert tree.count() == 6
    assert tree.depth() == 4

def test_tree_definition():
    tree = _getTestTree("test4.k")
    assert tree.count() == 12
    assert tree.depth() == 4

    

