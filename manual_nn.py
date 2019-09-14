#!/usr/bin/python
import numpy as np

class Operation():

    def __init__(self,inputnodes=[]):
        self.inputnodes=inputnodes
        self.outputnodes=[]

        for nodes in inputnodes:
            nodes.outputnodes.append(self)

        _default_graph.operations.append(self)
    def compute(self):
        pass

class add(Operation):
    """docstring for add in Operation"""
    def __init__ (self,x,y):
        super.__init__([x,y])
    def compute(self,x,y):
        self.inputs=[x,y]
        return x+y


class multiplication(Operation):
    """docstring for multiplication in Operation"""
    def __init__ (self,x,y):
        super.__init__([x,y])
    def compute(self,x,y):
        self.inputs=[x,y]
        return x*y


class matmul(Operation):
    """docstring for matmul in Operation"""
    def __init__ (self,x,y):
        super.__init__([x,y])
    def compute(self,x,y):
        self.inputs=[x,y]
        return x.dot(y)


class placeholder():

    def __init__(self):
        self.outputnodes=[]
        _default_graph.placeholders.append(self)

class Variable():

    def __init__(self,intial_value = None):
        self.value=intial_value
        self.outputnodes=[]
        _default_graph.variables.append(self)


class Graph():

    def __init__(self):
        self.opertaions=[]
        self.placeholders=[]
        self.variables=[]


    def set_as_default(self):
        global _default_graph
        _default_graph = self


g = Graph
g.set_as_default()
A = Variable(10)
b = Variable(1)
x = placeholder()
y = multiplication(A,x)
z = add(y,b)
""" the above is for z=Ax+b"""

def traverse_postorder(Operation):
    """
    PostOrder Traversal of nodes. Basically makes sure computations are done in the correct order."""
    nodes_postorder=[]
    if isinstance(node, Operation):
        for input_node in node.input_nodes:
            recurse(input_node)
        nodes_postorder.append(node)

    recurse(operation)
    return nodes_postorder

class Session(object):
    def run(self,operation,feed_dict={}):
        nodes_postorder=traverse_postorder(operation)

        for node in nodes_postorder:
            if type(node) == placeholder:
                node.output = feed_dict[node]

            elif type(node) == Variable:

                node.output = node.value

            else:
                #perform the operation

                node.inputs = [input_node.output for input_node in node.input_nodes]

                node.output = node.compute(*node.inputs)

            if type(node.output) == list:
                node.output == np.array(node.output)
        return operaion.output


sess = Session()
result = sess.run(operation=z,feed_dict={x:10})
result
