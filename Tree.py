class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def addChild(self, child):

        self.children.append(child.setParent(self))
        return self

    def getChildren(self):
        return self.children

    def setParent(self, parent):
        self.parent = parent
        return self
    
    def getParent(self):
        return self.parent

    def prettyPrint(self, indent = 0):
        if (indent == 0):
            print(self.data)
        else:
            print("--"*indent, self.data)

        for child in self.children:
            child.prettyPrint(indent+1)