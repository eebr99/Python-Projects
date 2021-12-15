import data

def main():
    vScore = 0
    iScore = 0
    total = 0
    lower = float(input('Enter the lowest score possible: '))
    upper = float(input('Enter the highest score possible: '))
    max = lower
    min = upper

#print comments are to check if data is being read correctly.    
    infile = open('testScores.txt', 'r')
    for line in infile:
#print('vScore = ', vScore)
#print('iScore = ', iScore)
        testScore = float(line)

        if data.validScore(lower, upper, testScore):
            vScore = vScore + 1
            total = total + testScore
            max = data.updateMax(max, testScore)
            min = data.updateMin(min, testScore)
            
        else:
#print('Invalid test score read.')
            iScore = iScore + 1

    infile.close()


    outfile = open('report.txt', 'w')
#outfile.write() requires a STRING
    outfile.write('The following report details some stats about the data provided:\n')
    outfile.write('' + '\n')
    outfile.write('The number of valid test scores is ' + str(vScore) + '\n')   
    outfile.write('The number of invalid test scores is ' + str(iScore) + '\n')         
    outfile.write('The highest valid test score is ' + str(max) + '\n')
    outfile.write('The lowest valid test score is ' + str(min) + '\n')
    outfile.write('The average of the valid test scores is ' + str(format(data.mean(total, vScore), '.1f')) + '\n')
    outfile.write('The midrange of the valid test scores is ' + str(format(data.midRange(max, min), '.1f')) + '\n')
    
    outfile.close()

    print('Report created.')

main()
