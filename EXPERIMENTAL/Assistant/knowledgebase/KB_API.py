import KB_Backend
import wolfram_request as wr

class KB:
    def __init__(self):
        self.on = True
    def search(self, keywords):
        with open("/home/pi/Charles_main/Assistant/knowledgebase/knowledge.base","r") as file:
            #Search through knowledge file
            facts = []
            raw_text = file.read()
            knowledges = raw_text.split("\n")

            knowledges_with_ranks = []
            for i in knowledges:
                knowledges_with_ranks.append([i,0])
            for i in range(len(knowledges_with_ranks)):
                key, value = knowledges_with_ranks[i]

                for j in keywords:
                    if j in key.split(" "):
                        knowledges_with_ranks[i][1] += 1


            MAGIC_NUM = int(len(keywords)/3)

            for i in knowledges_with_ranks:
                if i[1] >= MAGIC_NUM:
                    facts.append(i[0])


            #Search Wolfram Alpha
            wolfram_fact = wr.wolframRequest(" ".join(keywords))

            if wolfram_fact != "Wolfram|Alpha did not understand your input" and wolfram_fact != "No short answer available":
                facts.append(wolfram_fact)

            return facts
    def input_with_facts(self, input, facts):
        ret_str = input
        for i in facts:
            ret_str+="<FACT>" + i + "</FACT>"
        return ret_str

    def sendUpdateReq(self, indx, data):
        KB_Backend.requestUpdate(indx, data)
