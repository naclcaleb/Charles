import snowboydecoder
import sys
import signal

interrupted = False
def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted



class WakeWord:
    def __init__(self):
        pass
    def run(self, callback):
        signal.signal(signal.SIGINT, signal_handler)
        detector = snowboydecoder.HotwordDetector("/home/pi/Charles_main/Assistant/wake.pmdl",
                                                   sensitivity=0.4)
        detector.start(detected_callback=callback,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

        detector.terminate()

    def default_callback(self):
        print("Wake word detected")
