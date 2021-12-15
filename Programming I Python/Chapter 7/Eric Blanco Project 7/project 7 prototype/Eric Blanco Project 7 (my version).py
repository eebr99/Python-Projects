def main():
    import baseB #(module with all the functions necessary)

    infile = open('astros.txt', 'r')
    LofL = []
    temp = infile.readline()
    while temp != '':
        LofL.append(temp.split())
        #print(temp)
        temp = infile.readline()
        #print(temp)
    LofL = LofL[1:11]



    print(LofL)

    infile.close()

    outfile = open('report.txt', 'w')
    outfile.write('This report shows the battiing average, on-base %, slugging %, OPS, runs produced, and runs per plate appearances of each player and the team in general.' + '\n')
    outfile.write('' + '\n')
    index = 0
    while index < len(LofL):
        outfile.write(LofL[index][0] + '\n')
        outfile.write('Batting average: ' + str(format(baseB.bat_avg(LofL[index][3], LofL[index][1]), '.3f')) + '\n')
        index += 1
        outfile.write('' + '\n')
        
        
        







    print('Report created.')
    
main()
