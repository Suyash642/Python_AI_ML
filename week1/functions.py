#function for full name
def getname():
    return 'Suyash Bidkar'

#function for total marks
def getmarks(m1, m2, m3, m4, m5):
    total = m1+ m2+ m3+ m4+ m5
    return total

#function for percentage
def getpercentage(total):
    return (total/500)*100

#function for grades
def getgrades(percentage):
    if percentage >= 95:
        return 'A'
    elif percentage >= 85 and percentage < 95:
        return 'B'
    elif percentage >= 75 and percentage < 85:
        return 'C'
    elif percentage >= 65 and percentage < 75:
        return 'D'
    else:
        return 'Fail'

#function for student details
def getdetails():
    #marks of 5 subjects
    sub1_marks = 90
    sub2_marks = 95
    sub3_marks = 99
    sub4_marks = 98
    sub5_marks = 95
    #calling functions
    name = getname()
    score = getmarks(sub1_marks,sub2_marks,sub3_marks,sub4_marks,sub5_marks)
    percentage = getpercentage(score)
    grades= getgrades(percentage)
    #printing details
    print(f'Student Name: {name} \nScore: {score} \nPercentage: {percentage} \nGrades: {grades}\n')

if __name__ == "__main__":
    getdetails()