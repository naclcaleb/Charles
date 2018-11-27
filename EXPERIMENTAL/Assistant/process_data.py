newFile = open("data/dataset_1.txt","a+")


with open("data/BNCSplitWordsCorpus.txt", "r") as file:
    lines = file.read().split("\n")
    for i in range(len(lines)):
        if i%2 == 0:
            newFile.write("\n" + lines[i])
        else:
            newFile.write("\t" + lines[i])
newFile.close()
