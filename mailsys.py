import imapclient
from Contacts import Contacts
import pyzmail
from Notifications import Notifications
import time

UIDs = []

def loadMail():
    global UIDs
    imapObj = imapclient.IMAPClient('imap.gmail.com',ssl=True)
    imapObj.login('example@gmail.com','example_password')
    imapObj.select_folder("INBOX",readonly=False)
    UIDs = imapObj.search(["UNSEEN"])
    imapObj.set_flags(UIDs,"\SEEN")
def getContactList():
    imapObj = imapclient.IMAPClient('imap.gmail.com',ssl=True)
    imapObj.login('example@gmail.com','example_password')
    imapObj.select_folder("INBOX",readonly=False)
    global UIDs
    contacts = []
    if len(UIDs) >0:
        for i in UIDs:
            
            raw = imapObj.fetch(i,['BODY[]','FLAGS'])
            
            msg = pyzmail.PyzMessage.factory(raw[i][b'BODY[]'])
            c = Contacts()
            print(msg.get_addresses('from')[0][1])
            name = c.get_from_email([msg.get_addresses('from')[0][1],0])
            if not (name in contacts):
                contacts.append(name)
    else:
        time.sleep(1)
    UIDs = []
    return contacts
def setNotifications():
    loadMail()
    contacts = getContactList()
    n = Notifications()
    print(contacts)
    if len(contacts) == 1:
        n.send("You have a new email from " + contacts[0])
    elif len(contacts) > 1:
        lastitem = contacts.pop()
        s = ", ".join(contacts) + " and " + lastitem
    
        n.send("You have new emails from " + s)
    else:
        print("None")
        
while True:
    try:
        setNotifications()
    except:
        continue
