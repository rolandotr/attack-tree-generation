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
from pprint import pprint
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter.ttk import Progressbar


#####Trace Generation#######

#os.chdir("C:/Users/dnagumot/xampp/htdocs/attack_trees/attack-tree-generation/Test")
log_file = open("logfile.txt","w")


def generateTrace(aDict,frame):
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
    print("Creating Trace-generation Formula ")
    sys.stdout.flush()
    log_file.write("12%\n")
    ###Frame output
    frame.label=Label(frame, text = 'Creating Trace-generation Formula',font =('Verdana', 12))
    frame.label.grid(row=6, column=2, sticky=W)
    frame.progress_bar['value']=12
    frame.update_idletasks()

    ###Frame output
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
    print("Solving Formula ")
    sys.stdout.flush()
    log_file.write("25%\n")
    ###Frame output
    frame.label=Label(frame, text = 'Solving Formula',font =('Verdana', 12))
    frame.label.grid(row=7, column=2, sticky=W)
    frame.progress_bar['value']=25
    frame.update_idletasks()
    ###Frame output
    for element in fl:
        print('solving : ',element)
        print('pbessolve  -f '+'ATM.lps '+'pbesfile/'+element+' --evidence-file='+'lpsfile/'+element[:-4]+'lps')
        os.system('pbessolve  -f '+'ATM.lps '+'pbesfile/'+element +' --evidence-file='+'lpsfile/'+element[:-4]+'lps' )

    fl=os.listdir("lpsfile/")
    print(fl)

    print("Trace Generation")
    sys.stdout.flush()
    log_file.write("45%\n")
    ###Frame output
    frame.label=Label(frame, text = 'Trace Generation',font =('Verdana', 12))
    frame.label.grid(row=8, column=2, sticky=W)
    frame.progress_bar['value']=45
    frame.update_idletasks()
    ###Frame output
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

    print("\n\n")
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
    print("Traces Generation Done ")
    sys.stdout.flush()
    log_file.write("50%\n")
    ###Frame output
    frame.label=Label(frame, text = 'Trace Generation Done',font =('Verdana', 12))
    frame.label.grid(row=9, column=2, sticky=W)
    frame.progress_bar['value']=50
    frame.update_idletasks()
    ###Frame output
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

def getGraphLabels(P):
    graphs=[]
    for attack in P:
        attackLabels=[]
        for action in attack.actions:
           label=action.label
           #if hasattr(action,'params'):
           #   label+='@'+action.params
           attackLabels.append(label)
        graphs.append(attackLabels)
    return graphs

def convertAttackToStrings(d):
    graphs=[]
    for attack in d:
       actionLabels=[]
       for action in attack.actions:
          actionLabels.append(action.label)
       graphs.append(actionLabels)
    return graphs
def getAttacksFromLabels(U,d):
    returnAttacks=[]
    for actionLabels in U:
       actionsInAttack=[]
       actionLabelsInAttack=[]
       for labels in actionLabels:
          for attack in d:
             for action in attack.actions:
                if(action.label==labels and action.label not in actionLabelsInAttack):
                   actionsInAttack.append(action)
                   actionLabelsInAttack.append(labels)
       returnAttacks.append(Attack(actionsInAttack))
    return returnAttacks

def Decomposition2(d):
    print('Decomposition New 2:')
    print(d)
    if(len(d)==1 and len(d[0].actions)==1):
       return d
    flag=True
    for attack in d:
       if (len(attack.actions)!=1):
          flag=False
    if flag==True:
       return d
    #This is an attack. Converting it to strings
    SPsem=convertAttackToStrings(d);
    print (SPsem)

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
    #print ('Unamed', Unamed)
    #print ('Vnamed', Vnamed)
    for subtrace1 in U:
        index2=0
        for subtrace2 in V:
            if subtrace1+subtrace2 in SPsem:
                if [Unamed[index],Vnamed[index2]] not in E:
                    E.append([Unamed[index],Vnamed[index2]])
            index2+=1
        index+=1
    #rebuild SPsem
    #print ('Edges', E)
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
    UVDot=[]
    Unew=removeLastLetter(Gprime[0])
    print ('Left',Unew)
    Vnew=removeLastLetter(Gprime[1])
    print ('Right',Vnew)

    for unew in Unew:
       for vnew in Vnew:
          UVDot.append([unew,vnew])
    #print ('UVDot',UVDot)

    for i in range (0, len(UVDot)):
       jlist=[]
       for j in range (0, len(UVDot[i])):
          splitter=UVDot[i][j].split()
          for item in splitter:
             jlist.append(item)
       UVDot[i]=jlist

    #print ('UVDotNow',UVDot)

    #print ('UVDot New',UVDot)
    UVDotTuple=[tuple(lst) for lst in UVDot]
    SPsemTuple=[tuple(lst) for lst in SPsem]

    if(set(UVDotTuple)!=set(SPsemTuple)):
       return d
    else:
       ilist=[]
       for item in Unew:
          splitter=item.split();
          ilist.append(splitter)
          #for i in splitter:
          #   ilist.append(i)
       Unew=ilist
       print ('Unew', Unew)
       #print ('Vnew', Vnew)
       dUnew=getAttacksFromLabels(Unew,d)
       print (dUnew)

       ilist=[]
       for item in Vnew:
          splitter=item.split();
          ilist.append(splitter)
       Vnew=ilist
       print ('Vnew', Vnew)
       dVnew=getAttacksFromLabels(Vnew,d)
       print ('Vnew',dVnew)
       return (dUnew,dVnew)
       #SPLeft=Decomposition2(dUnew)
       #SPRight=Decomposition2(dVnew)
    #print ('Left',Gprime[0])
    #print ('Right',Gprime[1])
    #return [Gprime[0],Gprime[1]]
       #return (SPLeft,SPRight)


def Decomposition(SPsem):
    print('Decomposition New:')
    print(SPsem)

    G=[[],[],[]]
    U=[]
    V=[]
    E=[]
    Unamed=[]
    Vnamed=[]

    returnTraces=[]
    traceListFlag=False
    for trace in SPsem:
        #print (trace, type(trace))
        if(isinstance(trace,list)!=True):
           print ('Not a list')
           traceListFlag=True
        else:
           returnTraces.append(trace)
    if (traceListFlag==True):
        #print ('Return Traces',returnTraces)
        return SPsem
    for trace in SPsem:
        for i in range(1,len(trace)):
            if ' '.join(trace[0:i])+'l' not in Unamed:
                U.append(trace[0:i])
                Unamed.append(' '.join(trace[0:i])+'l')
            if ' '.join(trace[i:])+'r' not in Vnamed :
                V.append(trace[i:])
                Vnamed.append(' '.join(trace[i:])+'r')
    index=0
    #print ('Unamed', Unamed)
    #print ('Vnamed', Vnamed)
    for subtrace1 in U:
        index2=0
        for subtrace2 in V:
            if subtrace1+subtrace2 in SPsem:
                if [Unamed[index],Vnamed[index2]] not in E:
                    E.append([Unamed[index],Vnamed[index2]])
            index2+=1
        index+=1
    #rebuild SPsem
    #print ('Edges', E)
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
    UVDot=[]
    Unew=removeLastLetter(Gprime[0])
    print ('Left',Unew)
    Vnew=removeLastLetter(Gprime[1])
    print ('Right',Vnew)

    for unew in Unew:
       for vnew in Vnew:
          UVDot.append([unew,vnew])
    #print ('UVDot',UVDot)

    for i in range (0, len(UVDot)):
       jlist=[]
       for j in range (0, len(UVDot[i])):
          splitter=UVDot[i][j].split()
          for item in splitter:
             jlist.append(item)
       UVDot[i]=jlist

    #print ('UVDotNow',UVDot)

    #print ('UVDot New',UVDot)
    UVDotTuple=[tuple(lst) for lst in UVDot]
    SPsemTuple=[tuple(lst) for lst in SPsem]

    if(set(UVDotTuple)!=set(SPsemTuple)):
       return SPsem
    else:
       ilist=[]
       for item in Unew:
          if ' ' in item:
             splitter=item.split();
             ilist.append(splitter)
          else:
             ilist.append(item)
          #for i in splitter:
          #   ilist.append(i)
       Unew=ilist

       ilist=[]
       for item in Vnew:
          splitter=item.split();
          for i in splitter:
             ilist.append(i)
       Vnew=ilist
       print ('Unew', Unew)
       print ('Vnew', Vnew)
       SPLeft=Decomposition(Unew)
       SPRight=Decomposition(Vnew)
    #print ('Left',Gprime[0])
    #print ('Right',Gprime[1])
    #return [Gprime[0],Gprime[1]]
       return [SPLeft,SPRight]


def removeLastLetter(U):
    tempList=[]
    for element in U:
        tempList.append(element[:-1])
    return tempList





def buildtree(Filename,frame):
    #this fonction take in input a xml File
    #we want a Sp sematic and a refinement to call Gen_bin_tree
    pilist=[]
    tree = ET.parse(Filename)
    root = tree.getroot()
    #Spsem
    for elem in root:
        #print ('Elem-',elem)

        E=[]
        for subelem in elem:
            #print ('Sub elem-',subelem.attrib)
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
            #print('Action Tag',action.attrib)
            e=[]
            eprime=[]
            for s in action:
                # print(list(s.attrib.values()))
                #print('S',s)
                if len(list(s.attrib.values()))==0 :

                    # print("i'm here")
                    #print('S Tag',s.tag)
                    if s.tag =='e':
                        # print("ici")
                        for change in  s :
                            # print("ici pepe")
                            # print(change.tag)
                            e.append({list(change.attrib.values())[0]:list(change.attrib.values())[1]})
                    if s.tag =='eprime':
                        for change in  s :
                            # print("ici pepe")
                            #print('Change Tag',change.attrib)
                            eprime.append({list(change.attrib.values())[0]:list(change.attrib.values())[1]})
            # print(list(action.attrib.values())[0].replace('-',""))
            # print("will be the key of ")
            # print(e)
            # print(eprime)
            predicatdict[list(action.attrib.values())[0].replace('-',"")]=[e,eprime]
        listdict.append(predicatdict)
    print ('List Dict')
    pprint (listdict)
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
    pilist2=pilist
    print(pilist2)

    pilist=convertListSeq(pilist)

    print('Changing init knows ---- ')
    #listdict[2]['exploiting'][1][1]['init_knows1']=listdict[2]['exploiting'][1][1]['init_knows']
    #del listdict[2]['exploiting'][1][1]['init_knows']
    #print (listdict[2]['loggingInRem'])
    print('Changed init knows ---- ')

    stores1=Predicate('stores',['psw1'])
    knows1=Predicate('knows',['psw1'])
    locatedM=Predicate('located',['Mallory','Server'])
    exploiting=Action('exploiting',[],[stores1,knows1])
    logging1=Action('loggingInRem1',[],[locatedM],'psw1')
    A1=Attack([exploiting,logging1])
    knows=Predicate('knows',['psw'])
    bruteforcing=Action('bruteforcing',[],[knows])
    logging=Action('loggingInRem',[],[locatedM],'psw')
    A2=Attack([bruteforcing,logging])
    locatedA=Predicate('located',['Alice','Server'])
    start=Action('start',[],[locatedA])
    eaves=Action('eavesdropping',[],[knows])
    A3=Attack([start,eaves,logging])
    #A3=Attack([eaves,logging])
    dFixed=[A1,A2,A3]
    P=[stores1,knows1,locatedM,knows,locatedA]
    ## tree generation ###
    #d=convertListDict(listdict)
    d=convertDict(pilist2,listdict)

    print ("d")
    print (d)

    print("\n\n\n")

    print('Fixed Attacks')
    for attack in dFixed:
       print (attack)
       for action in attack.actions:
          print(action.label)
          if hasattr(action,'params'):
             print ('Params:',action.params)
          for event in action.eprime:
            print(event.key,event.params)

    print('After Conversion')
    for attack in d:
       print (attack)
       for action in attack.actions:
          print(action.label)
          if hasattr(action,'params'):
             print ('Params:',action.params)
          for event in action.eprime:
            print(event.key,event.params)

    #sys.exit()
    print("\n")

    print("Building Tree" )
    sys.stdout.flush()
    log_file.write("80%\n")

    ###Frame output
    frame.label=Label(frame, text = 'Building Tree',font =('Verdana', 12))
    frame.label.grid(row=10, column=2, sticky=W)
    frame.progress_bar['value']=80
    frame.update_idletasks()
    ###Frame output

    tree=genminmaxtree(d,P)

    #btree=genbintree(pilist,P)

    print("Tree Built " )
    log_file.write("100%\n")
    sys.stdout.flush()
    log_file.close();
    ### tree printing ###
    dot=Digraph(comment='Min Max Tree', graph_attr={'nodesep':'2','ranksep':'1.2'}, format='jpg')
    dot=visualizeTree(dot,tree)
    print (dot.source)
    dot.render('Min Max Tree.gv', view=True)



def convertDict(pilist,listdict):
    print ("Converting Dictionary")
    actionNames=[]
    actionDicts=[]
    ePredicates=[]

    eprimeCommonNumber=[]
    eprimeKeys=[]
    eprimeValues=[]
    eprimePredicates=[]

    actionObjects=[]
    print (pilist)
    for attack in pilist:
       for action in attack:
          for attackDict in listdict:
             if action in attackDict.keys():
                if(action not in actionNames):
                   actionNames.append(action)
                   actionDicts.append(attackDict[action])
                   #print (action, attackDict[action])
    print ('Action Dicts',actionDicts)
    for idx,actionPredicate in enumerate(actionDicts):
       e=actionPredicate[0]

       eprime=actionPredicate[1]
       eprimeactionPredicates=[]
       for predicate in eprime:
          for predicateKey in predicate.keys():
             if predicateKey not in eprimeKeys:
                p=Predicate(predicateKey,[predicate[predicateKey]])
                eprimePredicates.append(p)
                eprimeKeys.append(predicateKey)
                eprimeValues.append(predicate[predicateKey])
                eprimeCommonNumber.append(1)
                eprimeactionPredicates.append(p)
             else:
                eprimeIndex=eprimeKeys.index(predicateKey)
                if (eprimeValues[eprimeIndex]==predicate[predicateKey]):
                   eprimeactionPredicates.append(eprimePredicates[eprimeIndex])
                else:
                   p=Predicate(predicateKey,[predicate[predicateKey]])
                   eprimePredicates.append(p)
                   eprimeKeys.append(predicateKey+str(eprimeCommonNumber[eprimeIndex]))
                   eprimeValues.append(predicate[predicateKey])
                   eprimeactionPredicates.append(p)
                   eprimeCommonNumber[eprimeIndex]+=1
       actionObjects.append(Action(actionNames[idx],[],eprimeactionPredicates))
    print ("Action Objects",actionObjects)

    d=[]
    for attack in pilist:
       actionsInAttack=[]
       for action in attack:
          actionIndex=actionNames.index(action)
          actionsInAttack.append(actionObjects[actionIndex])
       d.append(Attack(actionsInAttack))
    return d


def convertListDict(listdict):
    d=[]
    actionLabels=[]
    eventNodes=[]
    allevents=[]
    eventkeys=[]
    allactions=[]
    print ('Converting List Dict')
    #print(len(listdict))
    for dict in listdict:
       #pprint(dict)
       actionObjects=[]
       for key in dict.keys():
          #print(keys)
          if (key not in actionLabels):
            #create a new action
            #actionLabels.append(key)
            #print (dict[key])
            e=[];eprime=[]
            for event in dict[key][1]:
               print (event)
               for eventkey in event.keys():
                   if(eventkey not in eventkeys):
                      eventkeys.append(eventkey)
                      eventNodes.append(event[eventkey])
                      eventObject=Predicate(eventkey,event[eventkey])
                      eprime.append(eventObject)
                      allevents.append(eventObject)
                   else:
                      indices=[i for i, x in enumerate(eventkeys) if x == eventkey]
                      matched=False
                      for i in indices:
                        if(eventNodes[i]==event[eventkey]):
                           matched=True
                           eprime.append(allevents[i])
                      if(matched==False):
                         eventObject=Predicate(eventkey,event[eventkey])
                         allevents.append(eventObject)
                         eprime.append(eventObject)
            print('Length of each action:',len(eprime))
            actionObject=Action(key,e,eprime)
            allactions.append(actionObject)
            actionObjects.append(actionObject)
            actionLabels.append(key)
          else:
             index=actionLabels.index(key)
             actionObjects.append(allactions[index])
       print('Length of Action Objects',len(actionObjects))
       d.append(actionObjects)
    return d

def mcrl2Parsing(Filename):
    # for a given Mcrl2 specification File, create an xml file containing all the action and the type associated to it, the return the dictionnary
    input = FileStream(Filename) #Read input from the file
    lexer = McrlLexer(input) #Create a lexer object from the input
    stream = CommonTokenStream(lexer) # Create an ANTLR streaming object from the lexer
    parser = McrlParser(stream) #Create an MCRL parser spec
    #print ("Parser",parser)
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

def main(argv,frame):
    print("Mcrl2 parsing\n")
    print (argv)
    log_file.write("0% \n")
    sys.stdout.flush()
    #frame.label=Label(frame, text = 'Mcrl2 parsing',font =('Verdana', 12))
    #frame.label.grid(row=4, column=2, sticky=W)
    #frame.update_idletasks()
    actiondict=mcrl2Parsing(argv[1])
    print("generating Traces")
    sys.stdout.flush()
    log_file.write("10% \n")
    frame.label=Label(frame, text = 'Generating Traces',font =('Verdana', 12))
    frame.label.grid(row=5, column=2, sticky=W)
    frame.progress_bar['value']=10
    frame.update_idletasks()
    generateTrace(actiondict,frame)
    ##first round of parsing to generate tracelist###
    print("first round of parsing")
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
    shutil.rmtree("lpsfile/")
    shutil.rmtree("msffile/")
    shutil.rmtree("pbesfile/")
    shutil.rmtree("trcfiles/")
    buildtree("filename.xml",frame)
    frame.label=Label(frame, text = 'Attack Tree Generated',font =('Verdana', 15))
    frame.label.grid(row=14, column=2, sticky=W)
    frame.progress_bar['value']=100

    return True

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Generation of Attack Trees")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)
        self.master.geometry("800x500+100+100")
        self.label=Label(self, text = 'Select Specification File Here',font =('Verdana', 15))
        self.label.grid(row=1, column=2, sticky=W)


        self.button = Button(self, text="Browse", command=self.load_file, width=10)
        self.button.grid(row=2, column=2, sticky=W)


    def load_file(self):
        fname = askopenfilename(filetypes=(("Specification file", "*.mcrl2"),))
        print (self)
        if fname:
            self.progress_bar=Progressbar(self, orient='horizontal', length=300, mode='determinate')
            self.progress_bar.grid(row=3, column=2, sticky=W)
            if(len(sys.argv)<2):
                sys.argv.append(fname)
            else:
                sys.argv[1]=fname
            try:
                main(sys.argv,self)
                #self.button.destroy();

            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'. Please Try Again!" % fname)
            return

if __name__ == "__main__":
    MyFrame().mainloop()
    #main(sys.argv)
