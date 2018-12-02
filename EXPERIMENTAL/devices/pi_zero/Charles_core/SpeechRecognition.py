import speech_recognition as sr
r = sr.Recognizer()
class SpeechRecognizer:
    def __init__(self):
        global r
    def recognize(self, online=True):
        global r
        with sr.Microphone() as source:
            print(source)
            r.adjust_for_ambient_noise(source, duration = 1)
            audio = r.listen(source)
            try:
                if online:
                    return r.recognize_google(audio)
                else:
                    
                    return r.recognize_sphinx(audio)
            except sr.UnknownValueError:
                
                return False
            except sr.RequestError as e:
                print("Internet is down")
                return False
