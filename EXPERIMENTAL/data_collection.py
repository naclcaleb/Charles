from Assistant import *
import tokenizer
kb = KB()
_sr = SpeechRecognizer()
c = True
while c:
    txt = _sr.recognize(online=False)
    with open("training_data/dataset_1.txt","a+") as data_file:
        print(txt)
        if txt:
            keywords = tokenizer.tokenize(txt)
            facts = kb.search(keywords)
            _input_ = kb.input_with_facts(txt, facts)
            data_file.write(("\n" + _input_ + "\t").encode("utf-8"))
            print(_input_)
        else:
            print("Failed")
            continue
        response = str(raw_input("Enter the appropriate response: "))
        data_file.write(response.encode("utf-8"))
        
