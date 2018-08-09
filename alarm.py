from datetime import datetime
import os

def setalarm(t):
    hr12 = datetime.strptime(t,"%H:%M")
    with open('time.txt','a') as file:
        file.write("," + hr12.strftime("%I:%M %p"))
   
def stopalarm(t):
    hr12 = datetime.strptime(t,"%H:%M")
    original = ""
    print(hr12.strftime("%I:%M %p"))
    with open('time.txt','r') as file:
        original = file.read()
    original = original.replace(hr12.strftime("%I:%M %p") + ",","")
    original = original.replace("," + hr12.strftime("%I:%M %p"),"")
    with open('time.txt','w+') as file:
        print(original)
        file.write(original)
    
def changealarm(t1,t2):
    hr12 = datetime.strptime(t1,"%H:%M")
    hr12_b = datetime.strptime(t2,"%H:%M")
    with open('time.txt','rw') as file:
        original = file.read()
        original.replace(hr12,hr12_b)
        file.write(original)
