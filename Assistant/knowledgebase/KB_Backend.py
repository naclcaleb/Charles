class KB_Backend:
    permissions = {
    "read-only":[[0,21]],
    "read/write":[[22,23]]
    }
    def __init__(self):
        pass
    def load_local_facts(self):
        with open("knowledge.base","r") as knowledge_file:
            local_facts = knowledge_file.read().split("\n")
            return local_facts
    def requestUpdate(self, indx, data):
        facts = self.load_local_facts()
        for i in self.permissions["read-only"]:
            if i[0]<=indx and indx<=i[1]:
                return False
        for i in self.permissions["read/write"]:
            if i[0]<=indx and indx<=i[1]:
                facts[indx] = data
        with open("knowledge.base","w") as knowledge_file:
            knowledge = "\n".join(facts)
            knowledge_file.write(knowledge)
        return True
