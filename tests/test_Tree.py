from Tree import Node


tree1 = Node()
tree2 = Node().addChild(Node().addChild(Node()).addChild(Node()))
tree3 = Node().addChild(Node().addChild(Node().addChild(Node().addChild(Node().addChild(Node())))))

def test_count():
    assert tree1.count() == 1
    assert tree2.count() == 4
    assert tree3.count() == 6


def test_depth():
    assert tree1.depth() == 1
    assert tree2.depth() == 3
    assert tree3.depth() == 6