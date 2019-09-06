
"""
@author: Dinesh Nagumothu
@desc: It has got functions like bipartite, findIsolated, getMaxDegree, getDegree, splitVertices, 
checkEquals, singleActionTrace, display, singleNodeTree, displayTree

Note: class Sequence was initially named as Vertex and hence if there is something represented in vertex consider it as a sequence which is a list of nodes with side
"""

from graphviz import Digraph

def bipartite(G,E):
    #Find if the graph is bipartite or not. If the graph is bipartite return True else return false 
    for vertex in G:
        # for every vertex in the graph
        count=0 # initiate count with 0
        for edge in E:
            #for every edge in E
            count+=edge.count(vertex) #Update count in edge
        if (count<2):
            #print ('graph not bipartite\n') #if count not equal to 2, the graph is bipartite
            return False
    #print ('graph bipartite\n')
    return True #if the degree of all the vertices of the graph is equal to 2, the graph is not bipartite

def findIsolated(G,E):
    #find the isolated vertices from the given graph and edges
    isolatedVertices=[] #create an empty list for vertices
    edgeVertices=[] #create an empty list for vertices in edges
    for edge in E:
        # for every edge in E
        for e in edge:
            # for each vertex in the Edge
            edgeVertices.append(e) #Append those vertices to a list to find flatten all the edges
    
    for vertex in G:
        #for every vertex in the graph
        if (vertex not in edgeVertices):
            #if the vertex is not in the above considered edge vertices, we can consider it as an isolated vertex
            isolatedVertices.append(vertex) #append the isolated vertex to the graph
    return (isolatedVertices) #return the isolated vertices
    

def getMaxDegree(G,E):
    #FUNCTION to find the maximum degree and vertices with maximum degree
    maxCount=0
    maxDegree=[]
    degrees=[]
    sortedDegree=[]
    for vertex in G:
        count=0
        for edge in E:
            count+=edge.count(vertex)
        degrees.append([vertex,count])
        if (count>maxCount):
            maxCount=count
    degrees.sort(key = lambda x: x[1], reverse=True) 
    for vertex in G:
        count=0
        for edge in E:
            count+=edge.count(vertex)
        if (count==maxCount):
            maxDegree.append(vertex)
    for degree in degrees:
        sortedDegree.append(degree[0])
    return (maxCount,sortedDegree)

def getDegree(V,E):
    #function to find the degree of a particular vertex
    count=0
    for edge in E:
        count+=edge.count(V)
    return count;

def splitVertices(G):
    #function to split the vertices into left and right one
    U=[];V=[]
    for vertex in G:
        if (vertex.side=='l'):
            U.append(vertex)
        else:
            V.append(vertex)
    return (U,V)

def checkEquals(GlGr, graphs):
    #function to check if the nodes in the two graphs are equal or not (True if Equal and False if unequal)
    print (graphs)
    tempSPGraph=[]
    for vertexList in GlGr:
        tempNodes=[]
        for node in vertexList[0].nodes:
            tempNodes.append(node.label)
        for node in vertexList[1].nodes:
            tempNodes.append(node.label)
        tempSPGraph.append(set(tempNodes))

    spnodes=[]
    for sp in graphs:
        nodes=[]
        for node in sp.nodes:
            nodes.append(node.label)
        spnodes.append(set(nodes))
    equals=True
    for i in spnodes:
        if i not in tempSPGraph:
            equals=False
            break;
    print (equals)
    return equals

def singleActionTrace(G):
    #function to verify if the graph has single action trace or not. Return the vertex if true or return false
    for vertex in G:
        if(vertex.graphLength()==1):
            return vertex
    return False

def display(graphs,title):
    #this function is to display the vertices along with a heading
    print (title,':',end=',')
    for vertex in graphs:
        print (vertex.getLabel(),end=',')
    print('\n') 

def singleNodeTree(tree):
    #function to verify if tree has any child nodes. True if there is no child and false if a child is present
    if(hasattr(tree,'child')):
        return False
    return True

def displayTree(tree):
    print (tree.top.getLabel(),end=',')
    if (hasattr(tree,'relation')):
        print (tree.relation,end='[')
    if (hasattr(tree,'child')):
        for child in tree.child:
            displayTree(child)
        print (']',end=',')
        
def getInter(dictlista1,dictlista2):

    # print("==========INTER FONCTION=======")
    # print("\n")
    # print("list 1")
    # print(dictlista1)
    # print("list 2")
    # print(dictlista2)
    interlist=[action for action in dictlista1 if action in dictlista2]
    # print("result :")
    # print(interlist)
    return interlist
    
def getUnion(dictlista1,dictlista2):

    interlist=[]
    for action in dictlista1:
        if action not in interlist:
            interlist.append(action)
    for action in dictlista2:
        if action not in interlist:
            interlist.append(action)
    return interlist

def Refinement_Spec(listaction,refinement):
    a2=[]
    a1=[]
    # print("\n")
    # print("we are in the refinement specification fonction\n")
    # print(refinement)
    for Action in listaction:
        if Action[0] == refinement[1]:
            a1=Action
        if Action[0] == refinement[2]:
            a2=Action
    if refinement[0]=="OR":
        String1 = ""
        String2 = ""
        for adict in getInter(a1[1],a2[1]):
            String1+=" "+''.join('{}{}'.format(key, val) for key, val in adict.items())
        for adict in getInter(a1[2],a2[2]):
            String2+=" "+''.join('{}{}'.format(key, val) for key, val in adict.items())
        if String1 == "":
            String1 = "Ø" 
        if String2 == "":
            String2 = "Ø" 
        XlabelString=String1.replace("[","(").replace("]",")")+" , "+String2.replace("[","(").replace("]",")")
        if refinement[1]==refinement[2]:
            return [refinement[1],getInter(a1[1],a2[1]),getInter(a1[2],a2[2])],XlabelString
        else:
            return ["Eps",getInter(a1[1],a2[1]),getInter(a1[2],a2[2])],XlabelString
            
    if refinement[0]=="SAND":
        String1 = ""
        String2 = ""
        for adict in getUnion(a1[1],a2[1]):
            String1+=" "+''.join('{}{}'.format(key, val) for key, val in adict.items())
        for adict in getUnion(a1[2],a2[2]):
            String2+=" "+''.join('{}{}'.format(key, val) for key, val in adict.items())
        if String1 == "":
            String1 = "Ø" 
        if String2 == "":
            String2 = "Ø" 
        XlabelString=String1.replace("[","(").replace("]",")")+" , "+String2.replace("[","(").replace("]",")")
        if refinement[1]==refinement[2]:
            return [refinement[1],getUnion(a1[1],a2[1]),getUnion(a1[2],a2[2])],XlabelString
        else:
            return ["Eps",getUnion(a1[1],a2[1]),getUnion(a1[2],a2[2])],XlabelString
            
            
###########################Visualization Functions######################
def visualizeTree(dot,tree,Epscount):
    if(singleNodeTree(tree)):
        #if the tree didn't have any further children, then return dot after creating the node with label
        dot.node(tree.top.getLabel(),tree.top.getLabel(),xlabel=tree.XlabelString)
        return dot
    topVertexName=tree.top.getLabel() #topVertexName is the name of the node for dot language
    topVertexLabel=topVertexName #topVertexLabel represents the label in the dot language
    if (topVertexName=='Eps'):
        #if the tree has the top node as 'Eps' change the name as 'Eps' followed by a count variable 'EpsCount'
        Epscount+=1 #Increment Eps count by 1
        topVertexName+=str(Epscount)
        topVertexLabel='ε' #Label as greek symbol
    dot.node(topVertexName,topVertexLabel,xlabel=tree.XlabelString) #add the node to dot file
    
    #edgeLabels=[]
    childLabels=[]
    childCount=0
    for child in tree.child:
        #Every child can be a different tree and hence call visualize tree again which fetches the dot file after visualization
        dot=visualizeTree(dot,child,Epscount) #pass child as a tree and Epscount with updated count
        childLabel=child.top.getLabel() #child label is the label of the child tree, if the node is 
        if (childLabel=='Eps'):
            childLabel+=str(Epscount+1) #if the child label is Eps increase the Epscount by 1
        if (tree.relation=='SAND'):
            dot.node('SAND'+str(Epscount)+','+str(childCount), '',shape='point')
            dot.edge(topVertexName,'SAND'+str(Epscount)+','+str(childCount),arrowhead='none')
            dot.edge('SAND'+str(Epscount)+','+str(childCount),childLabel)
            if(childCount<len(tree.child)-1):
                dot.edge('SAND'+str(Epscount)+','+str(childCount),'SAND'+str(Epscount)+','+str(childCount+1),constraint='false',arrowhead='normal')
        else:
            dot.edge(topVertexName,childLabel)
        childLabels.append(childLabel)
        childCount+=1
    
        
#        for i in range(len(childLabels)-1):
#            dot.edge(childLabels[i],childLabels[i+1])
    return dot

def visualizeTree2(dot,tree,treeCount):
    if(singleNodeTree(tree)):
        #if the tree didn't have any further children, then return dot after creating the node with label
        treeCount+=1
        dot.node('Tree'+str(treeCount),tree.top.getLabel())
        return (dot,treeCount)
    topVertexLabel=tree.top.getLabel()
    treeCount+=1
    thisTreeCount=treeCount
    dot.node('Tree'+str(treeCount),topVertexLabel) #add the node to dot file
    
    childCount=0
    for child in tree.child:
        (dot,treeCount)=visualizeTree2(dot,child,treeCount)
        childCount+=1
        print("Tree Count",treeCount)
        dot.edge('Tree'+str(thisTreeCount),'Tree'+str(treeCount))
    return (dot,thisTreeCount)
        
        
            
###########################Set Functions#################################
def cartesian_product(U,V):
    prod=[] #let prod be the resultant set that stores the cartesian product
    for u in U:
        #consider each vertex in the left hand side
        for v in V:
            #consider each vertex on the right hand side. Make a pair and append it to the prod list declared above.
            prod.append([u,v])
    #return the cartesian product
    return prod

def union(lst1, lst2): 
    #function to find the union of two lists.
    #first convert them to sets and perform union operation and finally change it back to List.
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 

