# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:40:10 2019

@author: Dinesh Nagumothu

Note: class Sequence was initially named as Vertex and hence if there is something represented in vertex consider it as a sequence which is a list of nodes with side
"""

from elements import *
from helpers import *
from FileParser import *
Eps=Sequence([Node('Eps')])

#Convert a list to a Seauence Object
def convertListSeq(pilist):
    listSeq=[]
    for row in pilist:
        tempSeq=[]
        for action in row:
            tempSeq.append(Node(action))
        listSeq.append(Sequence(tempSeq))
    return listSeq
#Remove the letter used to split into Two subgraph into decomposition
def removeLastLetter(U):
    tempList=[]
    for element in U:
        tempList.append(element[:-1].split())
    return tempList

def genbintree(graphs, P):
    #function to generate the binary tree
    display(graphs,'graph input to genbintree') #display the graph which is given as input to genbintree function
    b1=singleActionTrace(graphs) #if the input graph is single action trace
    if(b1):
        #give the output as b1 which is the actual node in the form of a tree
        print ('Single action trace found with b1=',b1.getLabel())
        if (len(graphs)==1):
            return Tree(b1)
        graphs.remove(b1) #remove b1 from the graph
        print ('\n',b1.getLabel(), 'is removed from graphs') #confirmation message that b1 is removed from the input graph
        display(graphs,'New Graph') #display the graph after b1 is removed
        t2=genbintree(graphs,P) #call genbintree again with the removed node b1
        print ('Tree=',t2.top.getLabel()) #print the top of tree
        Eps,XlabelString=Refinement_Spec(P,['OR',b1.getLabel(),t2.top.getLabel()])
        P.append(Eps)
        b=Tree(Sequence([Node(Eps[0])]),[Tree(b1),t2],'OR',XlabelString) #make a tree with vertex eps on one side and the output from b1 on other side along with the appropriate relation
        print ('B1 Tree for the node',b1.getLabel(),'=',b.top.getLabel(),' is the top &',b.child) #print confirmation
        if(b):
            #if a tree has been made, return b else return false
            return b
        else:
            return False
    else:
        #if the graph is not single action trace, then execute this block
        print('-----Decomposition--------------')
        SPSem=[]
        for seq in graphs:
            SPSem.append(seq.getNodes())
        (Gl,Gr)=Decomposition(SPSem) #decompose the graph first
        Gl=removeLastLetter(Gl)
        Gr=removeLastLetter(Gr)
        Gl=convertListSeq(Gl)
        Gr=convertListSeq(Gr)
        print ('Graph decomposed as')
        display(Gl,'Gl') #display the decomposed graphs gl
        display(Gr,'Gr') #display the decomposed graphs gr
        
        #make a cartesian product
        GlGr=cartesian_product(Gl,Gr)
        print (GlGr)
        if (checkEquals(GlGr,graphs)):
            # if the cartesian product of the decomposed graph is equal to the actual graph
            t1=genbintree(Gl,P) #create the left tree as genbintree from gl
            print ('Top of returned tree 1=',t1.top.getLabel()) #print confirmation
            t2=genbintree(Gr,P) # create the right tree as genbintree from gr
            print ('Top of returned tree 2=',t2.top.getLabel()) #print confirmation
            Eps,XlabelString=Refinement_Spec(P,['SAND',t1.top.getLabel(),t2.top.getLabel()])
            P.append(Eps)
            b=Tree(Sequence([Node(Eps[0])]),[t1,t2],'SAND',XlabelString) #make a tree by adding the relation as SAND
            print ('Tree is: top=',b.top.getLabel(),'child=',b.child[0].top,'&',b.child[1].top,'rel=',b.relation) #print confirmation
            if(b):
                #if a tree has been made, return b else return false
                return b
            else:
                return False
        else:
            #if the cartesian product is not equal to that of the input graph then 
            t1=genbintree(GlGr,P) #perform genbintree to the cartesian product and 
            graphs.remove(GlGr) #remove GlGr from graphs and 
            t2=genbintree(graphs,P)#
            Eps,XlabelString=Refinement_Spec(P,['OR',t1.top.getLabel(),t2.top.getLabel()])
            P.append(Eps)
            b=Tree(Sequence([Node(Eps[0])]),[t1,t2],'OR',XlabelString)#create a tree with t1 and t2 as child ana Eps as tree top
            if(b):
                #if a tree has been made, return b else return false
                return b
            else:
                return False
    return False

def genopttree(t):
    #function to generate the optimised tree
    print ('input to gen-opt-tree',end='=')
    displayTree(t)
    #display the tree which is given as input to the function every time
    print ()#dummy print function to create a new line
    if (singleNodeTree(t)):
        #if the tree contains single node ,i.e. no children then return the tree
        print ('This is a Single Node Tree',t.top.getLabel())
        return t
    tk=[]
    relation=t.relation #get the relation of the tree if it has one and store it in relation variable
    for tree in t.child:
        #for every individual child (tree) in list of children
        t1=genopttree(tree) #call the gen-opt-tree again and store the result in t1(which is a tree)
        tk.append(t1) #append the output tree to tk
    print ('tk=')
    #display tk which is list of output trees of the child
    for tree in tk:
        print (tree.top.getLabel(),end=',')
    print ()
    
    opt=True #set the optimised flag as True. If the flag is true, tree is optimised
    seq=[] #create a list to save the sequence
    for tree in tk:
        #for each tree in tk
        print ('Current Tree=', tree.top.getLabel()) #print the tree top of the current tree
        if (singleNodeTree(tree)):
            #if the tree has single node, then there is no need to optimise and hence appended to the sequence
            seq.append(tree)
        elif (tree.top.getLabel()==t.top.getLabel() and tree.relation==t.relation):
            #if the top of the parent tree and its child tree are same and has same relation, they can be optimised and hence appended to the sequence 
            for child in tree.child:
                #optimised-hence append all children to the seq which satisfies the condition
                seq.append(child)
        else:
            #else the optimisation is not performed and hence change the flag as false
            opt=False
    
    #print the seq which is the children to the output tree
    print ('seq',end='=')
    for tree in seq:
        print (tree.top.getLabel(),end=',')
    print ('relation=',relation) #along with the relation
    print ('opt=',opt) # and optimisation flag
    print ()
    
    print ('Tree top-',t.top.getLabel())
    
    if (opt):
        #if the input tree is optimised then return the tree with seq as child
        return Tree(t.top,seq,relation,t.XlabelString)
    else:
        #if the tree is not optimised, then return the tree with tk as child
        return Tree(t.top,tk,relation,t.XlabelString)

