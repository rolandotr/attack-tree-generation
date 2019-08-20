import sys
import xml.etree.ElementTree as ET
from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser
from HelloListener import HelloListener
from McrlLexer import McrlLexer
from McrlParser import McrlParser
from McrlListener import McrlListener
import random
import numpy as np
from graphviz import Digraph
from elements import *
from algorithms import *
import os
import subprocess as sub
import shutil

#####Trace Generation#######

os.chdir("C:/Users/dnagumot/xampp/htdocs/attack_trees/Test")

def generateTrace(aDict):
# '''
# we generate traces for every action contained in the mcrl2 specification file. we do this to make sure we don't miss any action in the traces
# so the first things we have to do is to parse the mcrl2 file to gather the action and the parameter as we need those to generate the traces.'''

    ###we all compute the msf File ####        
    try:
        shutil.rmtree("msffile/")
    except FileNotFoundError:
        print("first time Tracelist.txt is generated")
    os.mkdir('msffile') 
    os.chdir("msffile/")              

    i=65
    for action in aDict.keys():
        #to label the variable, we use letter of alphabet+ number of variable
        if action != "final":
            i=65
            datatowrite=[]
            settype=sorted(set(aDict[action]), key=aDict[action].index)
            numbertypedict={element:0 for element in settype}
            for type in aDict[action]:
                numbertypedict[type]=numbertypedict[type]+1
            for type in numbertypedict.keys():
                variablelist=[]
                for x in range(numbertypedict[type]):
                    variablelist.append(chr(i)+str(x))
                i+=1
                datatowrite.append([type,variablelist])
            stringtowrite="<true*. exists "
            for element in datatowrite:
                for elem in element[1]:
                    stringtowrite+="".join(elem)+","
                stringtowrite=stringtowrite[:-1]
                stringtowrite+="".join(":"+str(element[0])+",")
            stringtowrite=stringtowrite[:-1]
            stringtowrite+="."
            stringtowrite+=" "+action+"("
            for element in datatowrite:
                for elem in element[1]:
                    stringtowrite+="".join(elem)+","
            stringtowrite=stringtowrite[:-1]
            stringtowrite+="). true*. final>true"
            print(stringtowrite)
            with open(action+".msf",'w')as f:
                f.write(stringtowrite)
                
    os.chdir("..")
    os.system('mcrl22lps '+sys.argv[1]+' ATM.lps')
    fl=os.listdir("msffile/")
    #### we compute all the pbesfile ####
    try:
        shutil.rmtree("pbesfile/")
    except FileNotFoundError:
        print("first time pbes.txt is generated")
    os.mkdir('pbesfile') 
    
    for element in fl:
        os.system('lps2pbes -c -f '+'msffile/'+element+' ATM.lps '+'pbesfile/'+element[:-4]+'.pbes')
      
    #### we compute all the new lpsfile #### 
    fl=os.listdir("pbesfile/")  

    try:
        shutil.rmtree("lpsfile/")
    except FileNotFoundError:
        print("first time pbes.txt is generated")
        
    os.mkdir('lpsfile')
    output=[]
    for element in fl:
        print('solving : ',element)
        print('pbessolve  -f '+'ATM.lps '+'pbesfile/'+element+' --evidence-file='+'lpsfile/'+element[:-4]+'lps')
        os.system('pbessolve  -f '+'ATM.lps '+'pbesfile/'+element +' --evidence-file='+'lpsfile/'+element[:-4]+'lps' )

    fl=os.listdir("lpsfile/") 
    print(fl)


    ##### trace generation like before but on lps containing evidences######
    try:
        shutil.rmtree("trcfiles/")
    except FileNotFoundError:
        print("first time trcfiles.txt is generated")       
    os.mkdir('trcfiles')
    for element in fl:
        output.append(sub.getoutput('lps2lts --action=final -t lpsfile/'+element))
        
    filetomove=[]  
    for file in os.listdir("lpsfile/"):
        if file.endswith(".trc"):
            filetomove.append(file) 

    
    for file in filetomove:
        shutil.move("lpsfile/"+file, "trcfiles/")  

            
    print("yo")
    try:
        os.remove("Tracelist.txt")
    except FileNotFoundError:
        print("first time Tracelist.txt is generated")
        
    #Storing in a list all output of tracepp of each TRT files as follow
    #Tracelist[Trace1,Trace2,Trace3,...,Tracen]
        
    fl=os.listdir('trcfiles/')
    Tracelist=[]
    for file in fl:
        s=sub.getoutput('tracepp --format=states '+'trcfiles/'+file)
        Tracelist.append(s)
    Traceid=0
    #printing them to file Tracelist.txt
    with open("Tracelist.txt",'w') as f:
        for element in Tracelist:
            # print("this is an element")

            # print("\n"+element+"\n")
            Traceid+=1
            # print("we are here")
            f.writelines(str(Traceid)+ "\n"+element+"\n")   

dot = Digraph(comment = 'Trace generated attack Tree')


def Verticedegree(U,V,E):
    
    listdegree=[]
    for vertice in U:
        degree=0 
        for edge in E:
            if vertice == edge[0]:
                degree +=1
        if [vertice,degree] not in listdegree:
            listdegree.append([vertice,degree]) 
            
    for vertice in V:
        degree=0 
        for edge in E:
            if vertice == edge[0]:
                degree +=1
        if [vertice,degree] not in listdegree:
            listdegree.append([vertice,degree])
    return listdegree
    
       
def pickmaxdegreeVertice(listdegree,Z):
    u=''
    max=0
    possibleu=[]
    for element in listdegree:
        if element[1]>max:
            max=element[1]
    for element in listdegree:
        
        if element[1]==max:
            possibleu.append(element[0])
    u=random.choice(possibleu)
    lowermax=1
    while u in Z:
        if len(possibleu)!=0:
            u=random.choice(possibleu)
            possibleu.remove(u)
        else:
            while len(possibleu)==0:
                for element in listdegree:
                    if element[1]==max-lowermax:
                        possibleu.append(element[0])
                lowermax+=1
    return u
        
        
def colorGraph(G, color, pos, c): 
    
    if color[pos] != -1 and color[pos] != c: 
        return False
    color[pos] = c 
    ans = True
    for i in range(0, len(G)): 
        if G[pos][i]: 
            if color[i] == -1: 
                ans &= colorGraph(G, color, i, 1-c) 
                
            if color[i] !=-1 and color[i] != 1-c: 
                return False
        
        if not ans: 
            return False
    
    return True
                                      
def buildgraph(X,Y,E):
    grapharray= np.zeros((len(X)+len(Y),len(X)+len(Y)))
    index=0
    for i in range(len(X)):
        indey=0
        for j in range(len(Y)):
            if [X[i],Y[j]] in E:
                grapharray[i,len(X)+j]=1
            indey+=1
        index+=1
    return(grapharray)
      
def isBipartite(X,Y,E):
    grapharray=buildgraph(X,Y,E)
    color = [-1] *(len(X)+len(Y))   
    pos = 0 
    return colorGraph(grapharray, color, pos, 1)  

def isConnected(graphG,vertice_encoutered=None,start_vertex=None):
    """ 
    The algorithm is the following : we pick a random vertice and we define a set containing him and all reachable vertice
    if len(set) len(graphG.Vertice) ===> graph is connected
    """
    
    if vertice_encoutered is None:
        vertice_encoutered = set()
    
    Vertices=[]
    Vertices.extend(graphG[0])
    Vertices.extend(graphG[1])
    if not start_vertex:
        start_vertex= random.choice(Vertices)
    vertice_encoutered.add(start_vertex)
    linkedvertice=[]
    for edge in graphG[2]:
        if start_vertex in edge:
            for action in edge:
                if action  != start_vertex:
                    linkedvertice.append(action)
                    
    if len(vertice_encoutered)!= len(Vertices):
        for vertice in linkedvertice:
            if vertice not in vertice_encoutered:
                if isConnected(graphG,vertice_encoutered,vertice):
                    return True
    else:
        return True
    return False
  
def Biclique(X,Y,E):
    # This fonction take as input 2 list of Vertice and a list of edge, it should be use after the Decomposition algorithm otherwise if the graph is not Connected, the output is random 
    Z=[]
    G=[X,Y,E]
    futurWprime=X
    futurW=Y
    newEdge=E

    while (isBipartite(G[0],G[1],G[2])==False )or (isConnected(G)==False):
        W=[]
        u=pickmaxdegreeVertice(Verticedegree(G[0],G[1],G[2]),Z) # we pick an action with a maximum degree in the graph     
        if u in G[0]:
            W=G[1]
            Wprime=G[0]
            newEdge=G[2]
        else:
            W=G[0]
            Wprime=G[1]
            newEdge=G[2]
        VerticetoremoveinW=[]
        edgetoRemove=[]
        for subtrace in W: # we want to remove the vertice u form the graph and his associated Edges if we found action are not linked)
            if[u,subtrace] not in G[2]:
                if subtrace not in VerticetoremoveinW:
                    VerticetoremoveinW.append(subtrace)
                for edge in E: #We remove edges linked to removed Vertices
                    if subtrace in edge:
                        edgetoRemove.append(edge)
   
        # we effectively remove the previously calculated vertices and edges
        for element in VerticetoremoveinW:
            W.remove(element)
        for element in edgetoRemove:
            newEdge.remove(element)
        # we want to remove isolated Vertices
        removeisolated=[]
        futurWprime=Wprime
        for vertice in Wprime:  # we compute the isolated Vertice 
            isisolated=True
            for edge in newEdge:
                if vertice in edge:
                    isisolated=False
            if isisolated:
                removeisolated.append(vertice)
        futurW=W
        for vertice in W: # we compute the isolated Vertice 
            isisolated=True
            for edge in newEdge:
                
                if vertice in edge:
                    isisolated=False
            if isisolated:
                removeisolated.append(vertice)   
        for element in removeisolated:  # we remove the isolated Vertice
            if element in futurW:
                futurW.remove(element)
            if element in futurWprime:
                futurWprime.remove(element)
        Z.append(u)
    return[futurWprime,futurW,newEdge]     
    
def getMaxEdgeCC(graphG):
   
    vertice_encoutered = set()
    
    Verticestoexplore=[]
    Verticestoexplore.extend(graphG[0])
    Verticestoexplore.extend(graphG[1])
    
    listofCC=[]
        
    sVerticestoexplore=set(Verticestoexplore)
    while sVerticestoexplore:
        # print("while1")
        n=sVerticestoexplore.pop()
        group={n}
        queue=[n]
        while queue:
            # print("while2")
            # print(queue)
            n=queue.pop(0)
            neighbour=[]
            for edge in graphG[2]:
                for vertice in edge:
                    if vertice not in vertice_encoutered and n in edge:
                        neighbour.append(vertice)
                        sVerticestoexplore.discard(vertice)
                        vertice_encoutered.add(vertice)
            group.update(neighbour)
            for element in neighbour:
                if element not in queue :
                    queue.append(element)
        listofCC.append(group)
    # print("listofCC")
    # print(listofCC)    
    # print("\n")
    return listofCC
    
def Decomposition(SPsem):
    print(SPsem)
    G=[[],[],[]]
    U=[]
    V=[]
    E=[]
    Unamed=[]
    Vnamed=[]
    for trace in SPsem:
        for i in range(1,len(trace)):
            if ' '.join(trace[0:i])+'l' not in Unamed:
                U.append(trace[0:i])
                Unamed.append(' '.join(trace[0:i])+'l')
            if ' '.join(trace[i:])+'r' not in Vnamed :   
                V.append(trace[i:])
                Vnamed.append(' '.join(trace[i:])+'r')
    index=0
    for subtrace1 in U:
        index2=0
        for subtrace2 in V:
            if subtrace1+subtrace2 in SPsem:
                if [Unamed[index],Vnamed[index2]] not in E:
                    E.append([Unamed[index],Vnamed[index2]])
            index2+=1
        index+=1
    #rebuild SPsem  
    
    if isConnected([Unamed,Vnamed,E]):
        Gprime=Biclique(Unamed,Vnamed,E)
    else:
        listofCC=getMaxEdgeCC([Unamed,Vnamed,E])
        maxedgegraph=[]
        for graph in listofCC:
            if len(list(graph)) > len(maxedgegraph):
                maxedgegraph=list(graph)
        Unamed=[]
        Vnamed=[]
        # print(E)
        newE=E.copy()
        for element in maxedgegraph:
            if element[-1] == 'l':
                Unamed.append(element)
            if element[-1] == 'r':
                Vnamed.append(element)
        index=0
        for subtrace1 in U:
            index2=0
        for subtrace2 in V:
            if subtrace1+subtrace2 in SPsem:
                if [Unamed[index],Vnamed[index2]] not in newE:
                    newE.append([Unamed[index],Vnamed[index2]])
        # print("voila les nouvelle edge")
        # print(newE)
        Gprime=Biclique(Unamed,Vnamed,newE)
        
            # if x for x in action[:-1].split().append(y for y in action2[:-1].split()) not in rebuildSpsem:
                # rebuildSpsem.append([action[:-1].split(),action2[:-1].split()])
     
    #eliminateredundant
    return [Gprime[0],Gprime[1]]
             
def buildtree(Filename):
    #this fonction take in input a xml File
    #we want a Sp sematic and a refinement to call Gen_bin_tree
    pilist=[]
    tree = ET.parse(Filename)  
    root = tree.getroot()
    #Spsem
    for elem in root: 
        E=[]
        for subelem in elem:
            E.append(list(subelem.attrib.values())[0].replace('-',""))
        pilist.append(E)

    #refinement specification
    #wi start with abstraction refinement
    #for that we define a dict containing action : [s,s']

    P=['e']
    # Pilisttest=[['a','a'],['b','a','a'],['b','a','c'],['a','c']]
    # casestudy=[['w','ec','l'],['b','l'],['x','l']]
    # Decomposition(casestudy)
    listdict=[]
    for elem in root: 
        E=[]
        predicatdict={} 
        # print(elem.tag)
        for action in elem:
            
            # print(action.tag)
            e=[]
            eprime=[]
            for s in action:
                # print(list(s.attrib.values()))
                # print(s)
                if len(list(s.attrib.values()))==0 :
                    
                    # print("i'm here")
                    # print(s.tag)
                    if s.tag =='e':
                        # print("ici")
                        for change in  s :
                            # print("ici pepe")
                            # print(change.tag)
                            e.append({list(change.attrib.values())[0]:list(change.attrib.values())[1]})
                    if s.tag =='eprime':
                        for change in  s :
                            # print("ici pepe")
                            # print(change.tag)
                            eprime.append({list(change.attrib.values())[0]:list(change.attrib.values())[1]})
            # print(list(action.attrib.values())[0].replace('-',""))
            # print("will be the key of ")
            # print(e)
            # print(eprime)
            predicatdict[list(action.attrib.values())[0].replace('-',"")]=[e,eprime]  
        listdict.append(predicatdict)
    listaction=[]
    for element in listdict:
        for action in element.keys():
            if [action,element[action][0],element[action][1]] not in listaction:
                listaction.append([action,element[action][0],element[action][1]])
    listaction.append(['e',[],[]])
    trueAr=[]
    for action1 in listaction:
        ARlist=[]
        ARlist.append(action1[0])
        for action2 in listaction:
            if all(elem in action2[1]  for elem in action1[1]) and all(elem in action2[2]  for elem in action1[2]):
                if (action1[0] and action2[0]) or (action1[0] == 'e'):
                    ARlist.append(action2[0])
        trueAr.append(ARlist)
    P=listaction
    print(P)

    pilist=convertListSeq(pilist)
    
    ### tree generation ###
    btree=genbintree(pilist,P)
    
    ### tree printing ###
    dot=Digraph(comment='Bin Tree', format='png')
    dot=visualizeTree(dot,btree,0)
    #print (dot.source)
    dot.render('Bin Tree.gv',view=True)
    
    ####optimised tree printing####
    opttree=genopttree(btree)
    dot=Digraph(comment='Opt Tree', format='png')
    dot=visualizeTree(dot,opttree,0)
    #print (dot.source)
    dot.render('Opt Tree.gv',view=True)
    
def mcrl2Parsing(Filename):
    # for a given Mcrl2 specification File, create an xml file containing all the action and the type associated to it, the return the dictionnary
    input = FileStream(Filename)
    lexer = McrlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = McrlParser(stream)
    ### parsing on redundant free traces ###
    tree = parser.mcrl()
    printer = McrlListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    actiondict=Buildtracedict("dict.xml") 
    return actiondict
def Buildtracedict(Filename):
    Actiondict={}
    tree = ET.parse(Filename)  
    root = tree.getroot()
    #Spsem
    for elem in root: 
        
        Actiondict["".join(elem.attrib.values())]=["".join(subelem.attrib.values()) for subelem in elem ]
    return Actiondict
    
def main(argv):
    actiondict=mcrl2Parsing(argv[1])
    generateTrace(actiondict)
    ##first round of parsing to generate tracelist###
    input = FileStream("Tracelist.txt")
    lexer = HelloLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    ### parsing on redundant-free traces ###
    tree = parser.r()
    printer = HelloListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print("second round of parsing")
    del printer
    del walker
    del input
    del lexer
    del stream
    del parser
    del tree
    input2 = FileStream("Tracelistfinal.txt")
    lexer2 = HelloLexer(input2)
    stream2 = CommonTokenStream(lexer2)
    parser2 = HelloParser(stream2)
    tree2 = parser2.r()
    printer2 = HelloListener()
    walker2 = ParseTreeWalker()
    walker2.walk(printer2, tree2)
    print("\n\n\n",os.getcwd())
    buildtree("filename.xml")
if __name__ == '__main__':

    main(sys.argv)