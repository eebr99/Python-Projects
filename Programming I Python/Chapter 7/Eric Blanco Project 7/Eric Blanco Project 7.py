import baseB

def main():
    infile = open('Astros.txt', 'r') #imported the corrected file, that has the white space
    infile.readline()                 #character between last name and first initial removed.
    raw_stats = []
    calcs = []
    for line in infile:
        raw_stats.append(line.split())

    raw_stats.append(['* Houston Astros *', '578', '69', '138', '25', '0', '25', '66',
                      '61', '137', '2', '2'])

    size = len(raw_stats)

    for count in range(size):
        record = []
        record.append(raw_stats[count][0])
        record.append(baseB.bat_avg(raw_stats, count))
        record.append(baseB.onBase(raw_stats, count))
        record.append(baseB.slug(raw_stats, count))
        record.append(baseB.OPS(baseB.onBase(raw_stats, count), baseB.slug(raw_stats, count)))
        record.append(baseB.runs_prod(raw_stats, count))
        record.append(baseB.runs_per_plate(raw_stats, count))
        
        calcs.append(record)

    calcs.sort()#(key=lambda x:x[3], reverse = True)
    #print(calcs)

    infile.close()

    outfile = open('report.txt', 'w')

    outfile.write('This report shows the batting average, on-base %, slugging %, OPS,\n')
    outfile.write('runs produced, and runs per plate appearance of the team and each\n')
    outfile.write('individual player.' + '\n')
    outfile.write('' + '\n')

    index = 0
    while index < len(calcs):
        outfile.write(calcs[index][0] + '\n')
        outfile.write('Batting Average: ' + calcs[index][1] + '\n')
        outfile.write('On-Base %: ' + calcs[index][2] + '\n')
        outfile.write('Slugging %: ' + calcs[index][3] + '\n')
        outfile.write('OPS: ' + calcs[index][4] + '\n')
        outfile.write('Runs Produced: ' + calcs[index][5] + '\n')
        outfile.write('Runs per Plate Appearance: ' + calcs[index][6] + '\n')
        index += 1
        outfile.write('*********************************' + '\n')
        outfile.write('' + '\n')

    outfile.close()

    print('Report created.')

main()
