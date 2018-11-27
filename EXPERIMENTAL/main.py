import loader
from Assistant import *

light = Indicator()
_sr = SpeechRecognizer()
rh = ResponseHandler()
nc = NetworkCheck()
online = nc.check()
print(online)
#If wake word is detected, run processes
def runNetwork():
    light.on()
    
    text = _sr.recognize(online)
    print(text)
    """
    network = Seq2Seq()
    response = network.generateResponse(text)

    
    rh.process(response)

    
    
    return
    """
    light.off()
def test():
    print("Detected")
wake_word_detector = WakeWord()

wake_word_detector.run(callback=runNetwork)
