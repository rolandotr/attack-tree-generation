# -*- coding: utf-8 -*-
"""
@author: Dinesh Nagumothu
@desc: It has got 4 classes. Node, Sequence and Tree

Note: class Sequence was initially named as Vertex and hence if there is something represented in vertex consider it as a sequence which is a list of nodes with side
"""


class Node:
    #a node in the graph (input graph). These nodes consitutes a Sequence
    def __init__(self,label):
        self.label=label
class Sequence:
#    sequence is formed by nodes and they usually have sides (left or right)
#    they can be initialized with a list of nodes and (or) side of the node
#    The label of the vertex can be fetched by getLabel() function
    side=''
    def __init__(self,nodes,side=None):
        self.nodes=nodes
        if side is not None:
            self.side=side
    def getNodes(self):
        listNodes=[]
        for node in self.nodes:
            listNodes.append(node.label)
        return listNodes
    def graphLength(self):
        return len(self.nodes);
    def getLabel(self):
        label=''
        for node in self.nodes:
            label+=node.label
        if self.side!='':
            label+='-'
        label+=self.side
        return label

##For Min-Max-Tree

class Predicate:
   def __init__(self,key, params):
      self.key=key
      self.params=params

class Action:
    def __init__(self, label, e,eprime, params=None, decompositionLabel=None):
       self.label=label
       self.e=e
       self.eprime=eprime
       if params is not None:
          self.params=params

class Attack:
    def __init__(self, actions):
       self.actions=actions

##For Min-Max-Tree
      
class Tree:
    #A tree usually has a top sequence and may have children and relation
    def __init__(self,top,child=None,relation=None,XlabelString=None):
        self.top=top
        if child is not None:
            self.child=child
        if relation is not None:
            self.relation=relation
        if XlabelString is not None:
            self.XlabelString=XlabelString
        else :
            self.XlabelString= ""
