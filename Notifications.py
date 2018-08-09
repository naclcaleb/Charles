from Driver import Driver

class Notifications(Driver):
    device_name = "notifications"
    def send(self, data):
        with open("notifications.notify","a+") as file:
            file.write(data)
    def get(self, req=""):
        notifications = []
        with open("notifications.notify","r") as file:
            txt = file.read()
            notifications = txt.split("\n")
            
        return notifications
    def delete(self, indx):
        notifications = []
        with open("notifications.notify","r") as file:
            txt = file.read()
            notifications = txt.split("\n")
        notifications[indx] = ""
        with open("notifications.notify","w+") as file:
            newContent = ""
            for i in notifications:
                if i!="":
                    newContent += i + "\n"
            newContent = newContent[0:len(newContent)-2]
            file.write(newContent)
        
