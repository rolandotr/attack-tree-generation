import os
import subprocess as sub
import shutil
def GenerateTrace(argv[1]):
    print(" TMPfix/"+lpsfile[0:-3]+"lps")
    #Saving Traces generated while encountered LogginginRem(Mallory,Client,Server,****) To /TMPfix, remove the others
    output = sub.getoutput('lps2lts --action=final -t '+lpsfile +" "+lpsfile[0:-3]+"lts")
    for line in output.splitlines():
        # if "Mallory, Client, Server" in line:
        shutil.move(line.split()[-1].replace("\'",""), "TMPfix/"+line.split()[-1].replace("\'",""))
        # else:
            # print(line)
            # os.remove(line.split()[-1].replace("\'",""))
            
    #again make sure we are in a good environnement or setting it up
    os.chdir("TMPfix/")
    try:
        os.remove("Tracelist.txt")
    except FileNotFoundError:
        print("first time Tracelist.txt is generated")
        
    #Storing in a list all output of tracepp of each TRT files as follow
    #Tracelist[Trace1,Trace2,Trace3,...,Tracen]
        
    fl=os.listdir()
    Tracelist=[]
    for file in fl:
        s=sub.getoutput('tracepp --format=states '+file)
        Tracelist.append(s)
    Traceid=0
    #printing them to file Tracelist.txt
    with open("Tracelist.txt",'w') as f:
        for element in Tracelist:
            print("this is an element")

            print("\n"+element+"\n")
            Traceid+=1
            print("we are here")
            f.writelines(str(Traceid)+ "\n"+element+"\n")
if __name__== '__main__':
    GenerateTrace()