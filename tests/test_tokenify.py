from tokenify import tokenify

def _getTestCode(path):
    with open("tests/data/" + path) as f:
        code = f.read()
    return code

def test_statement_a():
    code = _getTestCode("test1.k")
    ts = tokenify((code, []))
    assert len(ts) == 16
    assert ts.count(("statement_start", "statement_start")) == 8
    assert ts.count(("statement_end", "statement_end")) == 8

def test_statement_b():
    code = _getTestCode("test2.k")
    ts = tokenify((code, []))
    assert len(ts) == 16
    assert ts.count(("statement_start", "statement_start")) == 8
    assert ts.count(("statement_end", "statement_end")) == 8

def test_function_call_params():
    expected = [('statement_start', 'statement_start'), ('function_call', 'test'), ('additional_parameter', 'aditional_parameter'), ('statement_start', 'statement_start'), ('statement_end', 'statement_end'), ('additional_parameter', 'aditional_parameter'), ('statement_start', 'statement_start'), ('statement_end', 'statement_end'), ('statement_end', 'statement_end')]

    code = _getTestCode("test3.k")
    ts = tokenify((code, []))
    assert len(ts) == 9

    for i, t in enumerate(ts):
        assert t == expected[i]

def test_function_definition():
    code = _getTestCode("test4.k")
    ts = tokenify((code, []))

    assert len(ts) == 9
    assert ts.count(("statement_start", "statement_start")) == 2
    assert ts.count(("statement_end", "statement_end")) == 2
    assert ts.count(("function_definition", "hello")) == 1
    assert ts.count(("function_definition", "test")) == 1
    assert ts.count(("parameter_definition", "message")) == 1
    assert ts.count(("parameter_definition", "bar")) == 1
    assert ts.count(("parameter_definition", "foo")) == 1

    

