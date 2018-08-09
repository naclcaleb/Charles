from Driver import Driver

class Memory(Driver):
    device_name = "memory"
    def send(self, data):
        with open("memory.mem", "a+") as file:
            file.write(str(data) + "\n")
    def get(self, req):
        with open("memory.mem", "r") as file:
            returned = ""
            memories = file.read()
            memories = memories.split("\n")
            ret_list = []
            for i in memories:
                if req.lower() in i.lower():
                    ret_list.append(i)
            returned = ", ".join(ret_list)
            return returned
    
