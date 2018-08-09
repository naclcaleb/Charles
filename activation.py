import sounddevice as sd
import numpy as np
import os
import sys

def wakeword():
    wake_word = "charles"

mic_name = "USB PnP Sound Device: Audio (hw:1,0)"

sample_rate = 48000

device_id = 0

chunk_size = 2048

r = sr.Recognizer()
 

mic_list = sr.Microphone.list_microphone_names()
 
for i, microphone_name in enumerate(mic_list):
    print(microphone_name)
    if microphone_name == mic_name:
        print(i)
        device_id = i
        break


def transfer():
    os.system("sudo python3 main.py")
    sys.exit()
    
def returnToActivation():
    os.system("sudo python3 activation.py")
    sys.exit()
 
with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                        chunk_size = chunk_size) as source:
    
    r.adjust_for_ambient_noise(source)
    print ("Say Something")
   
    audio = r.listen(source)
         
    try:
        text = r.recognize_google(audio)
        print(text)
        if wake_word in text.lower():
            transfer()
        else:
            returnToActivation()
     
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        returnToActivation()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        returnToActivation()


duration = 1  # seconds
threshold = 8

def checkVolume(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print ("|" * int(volume_norm))
    if volume_norm >= threshold:
        transfer()

def transfer():
    os.system("sudo python3 wakeword.py")
    sys.exit()
    
    
while True:
    with sd.Stream(callback=checkVolume):
        sd.sleep(duration * 1000)
