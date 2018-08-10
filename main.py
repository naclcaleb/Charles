access_token = ""




import wolframalpha as wolframalpha
import requests
import json
import os
import speech_recognition as sr
import sys
from datetime import datetime

import alarm
from WeatherMap import WeatherMap
from PyDictionary import PyDictionary
from Caleb_Computer import Caleb_Computer
from Memory import Memory
from Email import Email
from Contacts import Contacts
from Notifications import Notifications
import time
from SMS import SMS

contact_addr = ""
textMode = False
emailMode = False

appId = 'Wolfram App ID'

client = wolframalpha.Client(appId)

#Reset dialog file on startup
with open("/var/www/html/dialog.txt","w") as file:
  file.write("")

def Print(text):
  print(text)
  with open("/var/www/html/dialog.txt","a+") as file:
    file.write(text)

def SAY(text):
  os.system("./speakit.sh " + '"' + text + '"') 

msg = ""
def resolveListOrDict(variable):
  if isinstance(variable, list):
    return variable[0]['plaintext']
  else:
    return variable['plaintext']
  
def wolframsearch(text=''):
    res = client.query(text)
    if res["@success"] == 'false':
        return "Sorry. I don't have the ability to answer that"
    else:
        return resolveListOrDict(res['pod'][1]['subpod'])



      
def send():
    engine = pyttsx3.init()
    
    engine.setProperty('voice', 'english')
    global contact_addr
    global emailMode
    global textMode
    
    
    if "define " in msg.lower():
        engine.setProperty('voice','english')
        sub = msg[msg.lower().index("define ")+7:len(msg)]
        li = 0
        if " " in sub:
            li = sub.index(" ")
        else:
            li = len(sub)
        word = sub[0:li]
        d = PyDictionary()
        
        SAY(str(d.meaning(word)))
    elif "definition of " in msg.lower():
        engine.setProperty('voice','english')
        sub = msg[msg.lower().index("definition of ")+14:len(msg)]

        li = 0
        if " " in sub:
            li = sub.index(" ")
        else:
            li = len(sub)
        word = sub[0:li]
        d = PyDictionary()
        
        SAY(str(d.meaning(word)))
    elif msg.lower().replace("hey charles","").replace("charles","") == "":
      SAY("I do not have enough information to answer your request")
    else:
        r = requests.post("https://api.api.ai/v1/query", data=("{query:'" + msg.lower().replace("'","").replace("hey charles","").replace("charles","") + "',lang:'en',sessionId:'yaydevdiner'}"), headers={"Content-type":"application/json; charset=utf-8","Authorization":"Bearer " + access_token})
        obj = json.loads(r.text)
        
       
        
        if obj["result"]["speech"][0:9] == "setalarm(":
            timestr = obj["result"]["speech"][9:14]
            alarm.setalarm(timestr)
            SAY("Okay, setting alarm.")
        elif obj["result"]["speech"][0:10] == "stopalarm(":
            timestr = obj["result"]["speech"][10:15]
            alarm.stopalarm(timestr)
            SAY("Okay, stopping the alarm")
        elif obj["result"]["speech"] == "weather()":
            weather = WeatherMap()
            wtxt = weather.get("all")
            Print(wtxt)
            SAY(wtxt)
        elif obj["result"]["speech"] == "time()":
            t = datetime.now().strftime("%I:%M %p")
            SAY(t)
        elif obj["result"]["speech"] == "wolframalpha":
            query = obj["result"]["resolvedQuery"].lower().replace("hey charles","")
            query = query.replace("charles","")
            saytext = str(wolframsearch(query))
            saytext = saytext.replace("'","")
            Print(saytext)
            SAY(saytext)
        elif obj["result"]["speech"] == "setmem":
            mem = Memory()
            memstr = obj["result"]["resolvedQuery"].lower().replace("remember that ","")
            memstr = memstr.replace("you","{Charles}")
            memstr = memstr.replace("I", "You")
            memstr = memstr.replace("{Charles}","I")
            memstr = memstr.replace("hey charles","")
            memstr = memstr.replace("charles","")
            mem.send(memstr)
            SAY("Ok, remembering that")
        elif obj["result"]["speech"][0:6] == "email(":
            
            contact_name = obj["result"]['speech'][6:-1]
            srch = Contacts()
            contact_addr = srch.get([contact_name,1])
            Print(contact_addr)
            emailMode = True
            textMode = False
            SAY("Ok, what would you like to say?")
        elif obj["result"]["speech"][0:4] == "sms(":
            
            contact_name = obj["result"]["speech"][4:-1]
            srch = Contacts()
            contact_addr = srch.get([contact_name,2])
            Print(contact_addr)
            SAY("Ok, what would you like to say?")
            textMode = True
            emailMode = False
        else:
            SAY(obj["result"]['speech'])
        Print(obj["result"]["speech"])
    
    return emailMode
    engine.runAndWait()













mic_name = "USB PnP Sound Device: Audio (hw:1,0)"

sample_rate = 48000

device_id = 0

chunk_size = 2048

r = sr.Recognizer()
 

mic_list = sr.Microphone.list_microphone_names()
 
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
        break


def returnToActivation():
    Print("Restarting")
    Print(emailMode)

def trueOrFalse():
    global source
    global r
    audio = r.listen(source)
    try:
        txt = r.recognize_google(audio)
        Print(txt)
        if "yes" in txt or "yea" in txt:
            return True
        else:
            return False
    except:
        return False

def listenForText():
    global source
    global r
    audio = r.listen(source)
    try:
        txt = r.recognize_google(audio)
        return txt
    except:
        listenForText()

def checkEmail(e):
    global contact_addr
    global emailMode
    SAY("Ok, is this correct?")
    SAY(e)
    ans = trueOrFalse()
    if ans:
        eml = Email()
        eml.send([contact_addr,"From Charles",e])
        SAY("Ok, email sent")
        emailMode = False
    else:
        SAY("Ok, try again")
        newE = listenForText()
        Print(newE)
        checkEmail(newE)



def checkSMS(e):
    global contact_addr
    global textMode
    SAY("Ok, is this correct?")
    SAY(e)
    ans = trueOrFalse()
    if ans:
        sms = SMS()
        sms.send([contact_addr,e])
        SAY("Ok, text message sent")
        textMode = False
    else:
        SAY("Ok, try again")
        newE = listenForText()
        Print(newE)
        checkSMS(newE)


while True:
    
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source:
        n = Notifications()
        lst = n.get()
        if len(lst)>0:
            for i in range(0,len(lst)):
                Print(lst[i])
                SAY(lst[i])
                n.delete(i)
        r.adjust_for_ambient_noise(source)
        Print ("Say Something")
       
        audio = r.listen(source)
             
        try:
            text = r.recognize_google(audio)
            Print(text)
            
            msg = text.strip()
            Print(emailMode)
            if emailMode == True:
                Print("Email")
                checkEmail(msg)
            elif textMode == True:
                Print("SMS")
                checkSMS(msg)
            else:
                if "charles" in msg.lower():
                    send()
            
            returnToActivation()
         
        except sr.UnknownValueError:
            Print("Google Speech Recognition could not understand audio")
            returnToActivation()
        except sr.RequestError as e:
            Print("Could not request results from Google Speech Recognition service; {0}".format(e))
            returnToActivation()
