import re
class ResponseHandler:
    def __init__(self):
        pass
    def process(self, response):
        #There are a few special cases, with more being added regularly.
        #First, there can be <CMD></CMD> commands. These commands must be detected and processed.
        cmds = []
        try:
            start = response.index("<CMD>")
            end = reponse.index("</CMD>")
            cmds.append([start,end])
        except:
            pass
        for i in cmds:
            cmd_text = response[i[0]:i[1]]
    def handleCommand(self, cmd):
        pass