import csv

count = 0

def writeHeader() :
    with open('newOut.txt', 'w') as f:
        f.write("row\tsentence\twordIndex\tform\tlemma"
                + "\tupostag\txpostag\tfeats\thead\tdeprel\tdeps\tmisc\n")

def writeChunk(currSentence, lines) :
    with open('newOut.txt', 'a') as f:
        for line in lines :
            newLine = str(count) + "\t" + ' '.join(currSentence) + "\t" + line
            print newLine
            f.write(newLine)

with open("out.txt",'r') as file :
    writeHeader()
    currSentence = []
    lines = []
    for line in file:
        cols = line[:-1].split("\t")
        print cols
        if len(cols) == 1:
            # Reset sentence
            writeChunk(currSentence, lines)            
            currSentence = []
            lines = []
            count = count + 1
        else :
            currSentence.append(cols[1])
            lines.append(line)
