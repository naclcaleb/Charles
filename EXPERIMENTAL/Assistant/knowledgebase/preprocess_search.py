from PyDictionary import PyDictionary

d = PyDictionary()


def prepare(keywords):
    ret_arr = keywords

    for i in keywords:
        syns = d.synonym(i)
        if type(syns) == "list":
            for j in syns:
                ret_arr.append(j)
        else:
            continue
    return ret_arr
