from collections import Counter

def readListFF(name):
# Read list of genes from file
    f = open(name, 'r')
    out = [line.strip() for line in f]
    return out
    f.close()

def outInFile(name, l):
# Write list of genes into file
    f = open(name, 'w')
    for index in l:
        f.write(index + '\n')
    f.close()  

def main():
    name = 'geneList.txt'
    name_w = 'geneList_out.txt'
    outInFile(name_w, set(readListFF(name))) 
if __name__=='__main__':
    main()
