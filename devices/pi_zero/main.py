from Charles_core import *

charles = Charles()
light = Indicator()
_sr = SpeechRecognizer()
voice = Voice()

nc = NetworkCheck()
online = nc.check()
print(online)

#If wake word is detected, run processes
def runNetwork():
    light.on()
    
    text = _sr.recognize(online)
    
    response = charles.default_request(text)
    
    voice.speak(response)
    
    light.off()
def test():
    print("Detected")
wake_word_detector = WakeWord()

wake_word_detector.run(callback=runNetwork)
