# Generated from Hello.g4 by ANTLR 4.7.2
from antlr4 import *
import os 
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser
import xml.etree.cElementTree as ET
initial =  None  #value used to determine if we are in a status entitiy representing an initial state
finalstateValue=""#value used to determine if we are in a status entitiy representing an final state
Tracelist=[]#List used to store all step of one trace
stateVector=[]# containing all information about a trace (initial state, (state,action), final state)
TupleNamelist=[]# containing all Tuplename inside one trace
ActionNameList=[]# containing all Action inside one trace
TraceIdList=[]# containing all Traceid found in a file
changeperactionpertraces=[]
listT=[]
listZ=[]
strtype=""
        
            
#fonction to determine given two list, if the second contain subtrace of the first.
def containsubtrace(Trace,testtrace): 

    result =  all(elem in testtrace  for elem in Trace) 
 
    if result:  
        return True
    else :
        return False
def substitution(listT,strtype,listZ):
    abstractlist=[]
    # print(abstractlist)
    # print("we are in substitution")
    for element in listZ:
        for value in list(element) :
            # print(value)
            if value in listT:
                abstractlist.append(strtype)
            else:
                abstractlist.append(value)
    # print(abstractlist)
    return abstractlist

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    
    # Enter a parse tree produced by HelloParser#r.
    def enterR(self, ctx:HelloParser.RContext):
        
        pass

    # Exit a parse tree produced by HelloParser#r.
    # when we exit the parse tree, ze have all informations to remove traces
    def exitR(self, ctx:HelloParser.RContext):
    
        Filea = ET.Element("Filea")
        # Traceid = ET.SubElement(Filea, "Traceid")
        # Action = ET.SubElement(Traceid,"Action")
        # e = ET.SubElement(Traceid,"e")
        # eprime= ET.SubElement(Traceid,"eprime")
        
        ###Building the xml attack File
        global changeperactionpertraces
        global Tracelist
        global stateVector 
        print(Tracelist)
        print(stateVector)
        counter=1
        for element in changeperactionpertraces:
            Attack_Pattern=ET.SubElement(Filea,"Attack_Pattern",Id=str(counter))
            counter+=1
            for actions in element.keys():
                if str(actions) !="-final":
                    Action=ET.SubElement(Attack_Pattern,"Action",Action=str(actions))
                    if len(element[actions])!=0:

                        # Tuplename=element[actions][0][0],value=str(element[actions][0][2])
                        if len(element[actions][0][2])!=0:
                            e=ET.SubElement(Action,"e")
                            for valuelista in element[actions]:
                                ET.SubElement(e,"Change" ,Tuplename=str(valuelista[0]),value=str(substitution(['psw1','psw2'],"cred",valuelista[2])))
                        else:
                            e=ET.SubElement(Action,"e",value="none")
                            # Tuplename=str(element[actions][0][0]),value=str(element[actions][0][1])
                        if len(element[actions][0][1])!=0:
                            eprime=ET.SubElement(Action,"eprime")
                            for valuelista in element[actions]:
                                ET.SubElement(eprime,"Change" ,Tuplename=str(valuelista[0]),value=str(substitution(['psw1','psw2'],"Cred",valuelista[1])))
                        else:
                            eprime=ET.SubElement(Action,"eprime",value="none")
                        
        # ET.SubElement(doc, "field1", name="blah").text = "some value1"
        # ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
        
        tree = ET.ElementTree(Filea)
        os.remove("filename.xml")
        tree.write("filename.xml")
            
            
            
        global TraceIdList
        subtracelist= []
        ActionTracekept =[]
        for trace in stateVector:
            Tracelist.append(trace[1])
        # print("\n Here all all traces found in TraceList.txt with ANTLR4 \n")
        # print(Tracelist)
        # print("\n")
        Trace=[]
        for testtrace in Tracelist:
            if testtrace not in Trace:
                Trace.append(testtrace)
        for testtrace in Tracelist:
            if testtrace not in Trace:
                Trace.append(testtrace)
        # print(Trace)    
        print(Tracelist)
        for element1 in Tracelist:
            # print("\n \n============= "+str(Trace)+"\n we test element"+str(element1))
            # print("\n")
            for element2 in Tracelist:
                
                # print("avec"+str(element2))
                # print("\n")
                if element1 != element2:
                    if len(element2)<len(element1):
                        if containsubtrace(element2,element1):
                            # print(Trace)
                            # print("Trying to remove"+str(element1))
                            try:
                                Trace.remove(element1)
                                # print("element removed")
                            except ValueError:
                                # print("valeur deja enlever")
                                continue
                    else:
                        if containsubtrace(element1,element2):
                            
                            # print("Trying to remove"+str(element2))
                            try:
                                Trace.remove(element2)
                                # print("element removed")
                            except ValueError:
                                continue
              
        # print("\n we only Kept:")
        # print(Trace)
        # print("corresponding to Trace ID:")
        TracetoKeep=[]
        TraceToRemove=[]
        for element1 in Trace:
            for Traces in stateVector:
                if element1 == Traces[1]:
                    TracetoKeep.append(list(Traces[0])[0])
        # print(TracetoKeep)
        #print(TracetoKeep)
        with open("Tracelist.txt",'r') as f:
            tracesintext=[]
            traceintext=[]
            tracetokeeptext=[]
            index=0
            for line in f:
                SameTrace=True
                while SameTrace:
                    
                        try:
                            if int(line)!=1:
                                traceintext=[]
                                
                                traceintext.append(line)
                                tracesintext.append(traceintext)
                                if  str(int(line)) in TracetoKeep:
                                    tracetokeeptext.append(traceintext)
                            else: 
                                traceintext=[]
                                traceintext.append(line)
                                tracesintext.append(traceintext)
                                if  str(int(line)) in TracetoKeep:
                                    tracetokeeptext.append(traceintext)
                            SameTrace=False
                                
                            break
                        except ValueError:
                            traceintext.append(line)
                            SameTrace=False
        # print("\n")
        # print("we will write in a new file :")
        newtracecount=1

        with open("Tracelistfinal.txt",'w') as f:
            for element in tracetokeeptext:
                f.writelines(str(newtracecount)+"\n")
                f.writelines(element[1:]) 
                newtracecount+=1
        # for element in tracetokeeptext:
            # print(element)
            # print("\n")
        global finalstateValue
        
        
        global TupleNamelist
        global ActionNameList
        global TraceIdList
        global listT
        global listZ
        global strtype
        initial =  None  #value used to determine if we are in a status entitiy representing an initial state
        finalstateValue=""#value used to determine if we are in a status entitiy representing an final state
        Tracelist=[]#List used to store all step of one trace
        stateVector=[]# containing all information about a trace (initial state, (state,action), final state)
        TupleNamelist=[]# containing all Tuplename inside one trace
        ActionNameList=[]# containing all Action inside one trace
        TraceIdList=[]# containing all Traceid found in a file
        changeperactionpertraces=[]
        listT=[]
        listZ=[]
        strtype=""    
        pass
    # Enter a parse tree produced by HelloParser#traces.
    def enterTraces(self, ctx:HelloParser.TracesContext):
        counter=0
        global changeperactionpertraces
        changeperaction={}
        for element in ctx.trace():   

            if element.trans()!=None:
                Tuplelistafter=[]
                Tuplelist=[]
                #we build the list containing all state value before an action
                for p in element.status().tupleallDecl():
                    Valuelist=[]
                    for el in p.tupledecl():
                        Valuelist.append([ele.getText() for ele in el.Value()])
                    Tuplelist.append([p.Tuplename().getText(),Valuelist])
                    
                #we build the list containing all state value before an action    
                for p in ctx.trace()[counter+1].status().tupleallDecl():
                    Valuelist=[]
                    for el in p.tupledecl():
                        Valuelist.append([ele.getText() for ele in el.Value()])
                    Tuplelistafter.append([p.Tuplename().getText(),Valuelist])
                    
                ActionUpdate=[]
                for Tuplebefore,Tupleafter in zip(Tuplelist,Tuplelistafter):
                      
                    first_set = set(map(tuple, Tuplebefore[1]))
                    secnd_set = set(map(tuple, Tupleafter[1]))
                    e=list(secnd_set-first_set)
                    eprime=list(first_set - secnd_set)
                    if len(e)==0:
                        if len(eprime)==0:
                            continue
                    else:
                        ActionUpdate.append([Tuplebefore[0],e,eprime])              
                changeperaction[element.trans().ActionName().getText()]=ActionUpdate
                
                
            counter+=1
        changeperactionpertraces.append(changeperaction)     
        pass

    # Exit a parse tree produced by HelloParser#traces.
    def exitTraces(self, ctx:HelloParser.TracesContext):
        global ActionNameList
        global stateVector
        global TupleNamelist
        global TraceIdList
        print(ActionNameList)
        TraceIdList.append(ctx.traceid().getText())
        stateVector.append([{ctx.traceid().getText():TupleNamelist},ActionNameList])
        TupleNamelist=[]
        ActionNameList=[]
        
        pass



    # Enter a parse tree produced by HelloParser#traceid.
    def enterTraceid(self, ctx:HelloParser.TraceidContext):
        pass

    # Exit a parse tree produced by HelloParser#traceid.
    def exitTraceid(self, ctx:HelloParser.TraceidContext):
        pass


    # Enter a parse tree produced by HelloParser#trace.
    def enterTrace(self, ctx:HelloParser.TraceContext):
        global TupleNamelist
        TupleNamelist=[]
        if ctx.trans()==None:
            for p in ctx.status().tupleallDecl():
                Valuelist=[]
                for el in p.tupledecl():
                   Valuelist.append([ele.getText() for ele in el.Value()])
                TupleNamelist.append([p.Tuplename().getText(),Valuelist])   
                
                    
        pass

    # Exit a parse tree produced by HelloParser#trace.
    def exitTrace(self, ctx:HelloParser.TraceContext):
      
        pass


    # Enter a parse tree produced by HelloParser#status.
    def enterStatus(self, ctx:HelloParser.StatusContext):
        pass

    # Exit a parse tree produced by HelloParser#status.
    def exitStatus(self, ctx:HelloParser.StatusContext):
        pass


    # Enter a parse tree produced by HelloParser#tupleallDecl.
    def enterTupleallDecl(self, ctx:HelloParser.TupleallDeclContext):
        pass

    # Exit a parse tree produced by HelloParser#tupleallDecl.
    def exitTupleallDecl(self, ctx:HelloParser.TupleallDeclContext):
        pass


    # Enter a parse tree produced by HelloParser#tupledecl.
    def enterTupledecl(self, ctx:HelloParser.TupledeclContext):
        pass

    # Exit a parse tree produced by HelloParser#tupledecl.
    def exitTupledecl(self, ctx:HelloParser.TupledeclContext):
        pass


    # Enter a parse tree produced by HelloParser#trans.
    def enterTrans(self, ctx:HelloParser.TransContext):
        global ActionNameList
        ActionNameList.append(str(ctx.ActionName()))
        
        pass

    # Exit a parse tree produced by HelloParser#trans.
    def exitTrans(self, ctx:HelloParser.TransContext):
        pass
            
