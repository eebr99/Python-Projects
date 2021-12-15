def main():
    infile = open('data.txt','r')
    LofL =[]
    temp = infile.readline()
    while temp!='':
        LofL.append(temp.split())
        temp = infile.readline()
    print(LofL)
    print(LofL[2][1])
main()
