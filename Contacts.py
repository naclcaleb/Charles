from Driver import Driver

class Contacts(Driver):
    device_name = "contact_book"
    def send(self, data):
        with open("contacts.list","a+") as file:
            file.write(data[0] + "," + data[1] + "\n")
    def get(self,data):
        with open("contacts.list","r") as file:
            contacts = file.read()
            contacts = contacts.split("\n")
            ret_data = ""
            for i in contacts:
                contact_info = i.split(",")
                contact_name = contact_info[0]
                if data[0].lower() == contact_name.lower():
                    ret_data = contact_info[data[1]]
                    break
            return ret_data
    def get_from_email(self, data):
        with open("contacts.list","r") as file:
            contacts = file.read()
            contacts = contacts.split("\n")
            ret_data = ""
            for i in contacts:
                contact_info = i.split(",")
                contact_name = contact_info[1]
                if data[0].lower() == contact_name.lower():
                    ret_data = contact_info[data[1]]
                    break
            return ret_data
