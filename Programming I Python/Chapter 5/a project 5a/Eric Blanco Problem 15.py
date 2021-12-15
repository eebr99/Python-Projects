#Write a program that asks the user to enter five test scores. The program should display a
#letter grade for each score and the average test score.

def main():
    print('This program will take 5 test scores and calculate')
    print('and display the average and letter grade.')
    score1 = int(input('Enter the first test score: '))
    score2 = int(input('Enter the second test score: '))
    score3 = int(input('Enter the third test score: '))
    score4 = int(input('Enter the fourth test score: '))
    score5 = int(input('Enter the fifth test score: '))
    avg = calc_average(score1, score2, score3, score4, score5)
    grade = determine_grade(avg)
    print('Score\tLetter Grade')
    print(avg, '  ', grade)

def calc_average(a, b, c, d, e):
    avg = (a + b + c + d + e)/5
    return avg

def determine_grade(avg):
    if avg >= 90 and avg <= 100:
        grade = 'A'
    elif avg >= 80 and avg <= 89:
        grade = 'B'
    elif avg >= 70 and avg <= 79:
        grade = 'C'
    elif avg >= 60 and avg <= 69:
        grade = 'D'
    else:
        grade = 'F'
    return grade
    
main()
