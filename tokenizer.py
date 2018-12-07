def tokenize(string):
    tokens = []
    indx = 0
    for i in range(len(string)):
        if string[i] in " ,.?!":
            if string[indx:i]!='':
                tokens.append(string[indx:i])
            tokens.append(string[i])
            indx = i+1
        if i == len(string):
            if string[indx:i]!='':
                tokens.append(string[indx:i])
            break
    return tokens

